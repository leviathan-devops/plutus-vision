// model.ts — the aether (pi-durable) wiring and THE ONE model function, `modelStep`.
// Everything model-enabled in the sidecar goes through `modelStep`; nothing else talks to the gateway.
//
// Runtime: the framework at AETHER_HOME (aether_agent_backend_v2) = @earendil-works/pi-durable Harness
// (durable tasks, conversations, committed transcript) + pi-ai's opencode-go provider. The wiring mirrors
// AETHER_HOME/src/aether-durable-harness.ts steps 1-6 (models -> storage -> registry -> Harness.open -> root -> resume).
// It does NOT call AetherDurableHarness.run(): that entry is text-only, edit-bound (needs promptFilePath) and
// installs the coding tools; an image-transcription step must carry an image and must have no tools.
import * as fs from "node:fs";
import * as path from "node:path";
import { CACHE, SidecarError, sha, writeJson, readJson } from "./lib.ts";

export const AETHER_HOME = process.env.AETHER_HOME ?? "/home/user/inputs/aether/aether_agent_backend_v2";
const NM = `${AETHER_HOME}/node_modules/@earendil-works`;
/** Same pin as AETHER_DEFAULT_MODEL in the aether harness. */
export const MODEL = { provider: "opencode-go", modelId: "muse-spark-1.3-contributor" };
export const EFFORT = "high";
/** Responses API base; pi-ai appends `/responses`. */
export const GATEWAY_BASE = "https://opencode.ai/inference/go/openai/v1";

export type ModelRequest = { kind: string; prompt: string; imagePath?: string };
export type ModelResult = { key: string; text: string; cached: boolean };
export const stats = { calls: 0, cached: 0 };

export async function openSidecarHarness(storagePath: string, tasks: (D: any) => any[]) {
  const { BACKGROUND_CONTEXT: ctx } = await import(`${NM}/chord/dist/context/index.js`);
  const piai = await import(`${NM}/pi-ai/dist/index.js`);
  const { opencodeGoProvider } = await import(`${NM}/pi-ai/dist/providers/opencode-go.js`);
  const D = await import(`${NM}/pi-durable/dist/index.js`);
  const { openNodeSqliteStorage } = await import(`${NM}/pi-durable/dist/storage/sqlite/node.js`);

  // The key is injected by the network proxy; the process only ever holds this literal.
  process.env.OPENCODE_API_KEY = "proxy-injected";
  const models = piai.createModels();
  const go = opencodeGoProvider(); // adds the x-opencode-session header from the conversation's session id
  const k = go.auth.apiKey;
  models.setProvider({ ...go, auth: { ...go.auth, apiKey: { ...k, resolve: async (a: unknown) => {
    const r = await k.resolve(a);
    return r ? { ...r, auth: { ...r.auth, baseUrl: GATEWAY_BASE } } : r;
  } } } });

  fs.mkdirSync(path.dirname(storagePath), { recursive: true });
  const storage = await openNodeSqliteStorage(storagePath);
  const registry = D.createRegistry();
  const defs = tasks(D);
  registry.install(D.defineExtension({ name: "plutus-sidecar", tasks: defs }));
  const reports: string[] = [];
  const harness = await D.Harness.open(storage, { models, registry,
    settings: { stream: { timeoutMs: 600_000 }, retry: { maxRetries: 3 } },
    onReport: (e: unknown) => { reports.push(String(e)); } }, ctx);
  // No extensions selected -> the model is offered NO tools and no system sections: a pure transcription step.
  const root = await harness.root(ctx, { agent: { model: MODEL, thinkingLevel: EFFORT, extensions: [] } });
  return { D, ctx, harness, root, defs, reports };
}

function cacheFile(key: string) { return path.join(CACHE, "reads", `${key}.json`); }

/**
 * THE MODEL STEP. Deterministic cache first (key = model + effort + prompt + image bytes); on a miss, one fresh
 * task-owned conversation (no shared context between reads -> the reads are independent), one input, one answer.
 * `rt` is the durable task runtime of the calling phase.
 */
export async function modelStep(rt: any, ctx: any, req: ModelRequest): Promise<ModelResult> {
  const img = req.imagePath ? fs.readFileSync(req.imagePath) : undefined;
  const key = sha(JSON.stringify([MODEL.modelId, EFFORT, req.kind, req.prompt, img ? sha(img) : null]));
  const cf = cacheFile(key);
  if (fs.existsSync(cf)) { stats.cached++; return { key, text: readJson(cf).text, cached: true }; }
  if (process.env.SIDECAR_NO_MODEL) throw new SidecarError("MODEL_CACHE_MISS", `${req.kind}: no cached read ${key} and SIDECAR_NO_MODEL is set`);

  const content: unknown[] = [{ type: "text", text: req.prompt }];
  if (img) content.push({ type: "image", data: img.toString("base64"), mimeType: "image/png" });
  let convId: unknown;
  await rt.commit(async (tx: any) => { convId = (await tx.createConversation({ ownership: { kind: "task", taskId: rt.taskId } })).id; return undefined; }, ctx);
  const conv = await rt.conversation(convId, ctx);
  const sub = await conv.submit({ type: "input", content, requestId: `read:${key}` }, ctx);
  const settled = await sub.wait(ctx);
  if (settled.status !== "done") throw new SidecarError("MODEL_STEP_FAILED", `${req.kind}: ${settled.reason ?? settled.status} ${JSON.stringify(settled.detail ?? "").slice(0, 300)}`, 4);
  let rec: any;
  await rt.commit(async (tx: any) => { rec = await tx.entry(settled.answer); return undefined; }, ctx);
  const parts = (rec?.model?.[0]?.content ?? []) as { type?: string; text?: string }[];
  const text = parts.filter((p) => p.type === "text").map((p) => String(p.text ?? "")).join("");
  if (!text.trim()) throw new SidecarError("MODEL_STEP_FAILED", `${req.kind}: the answer carried no text`, 4);
  stats.calls++;
  writeJson(cf, { key, kind: req.kind, model: MODEL.modelId, effort: EFFORT, gateway: `${GATEWAY_BASE}/responses`,
    prompt_sha256: sha(req.prompt), image: req.imagePath ? path.relative(path.resolve(CACHE, ".."), req.imagePath) : null,
    image_sha256: img ? sha(img) : null, text });
  return { key, text, cached: false };
}

/** Run model steps with bounded concurrency, results in input order. */
export async function modelSteps(rt: any, ctx: any, reqs: ModelRequest[], conc = 3): Promise<ModelResult[]> {
  const out: ModelResult[] = new Array(reqs.length);
  let next = 0;
  await Promise.all(Array.from({ length: Math.min(conc, reqs.length) }, async () => {
    while (next < reqs.length) { const i = next++; out[i] = await modelStep(rt, ctx, reqs[i]); }
  }));
  return out;
}
