# 03 — DECISION CHAIN (append-only; one decision per row: what, why, alternatives rejected)

| # | date | decision | why | rejected |
|---|---|---|---|---|
| D-01 | 2026-11-25 | Run Pinebox in LOCAL placement on an Xvfb display in this container (`pinebox up --adapter xvfb`) | The cloud placement needs the operator's Mac/Orca; local is the same page, engine and bar store, and I can capture and drive it | spawn-cloud-* (no Orca here) |
| D-02 | 2026-11-25 | Memory lives in `memory/*.md` (source of truth) + OmniGraph mirror; old October context files archived, not deleted | Operator order L-13; old files described a finished build with a stale phase gate | Keep the Semantica graph as primary (needs pip install each reset) |
| D-03 | 2026-11-25 | Readers (subagents) extract canon/handover/oracles into digest files; I write the indicator and judge every frame myself | L-06 "use them freely just don't delegate primary responsibilities" | Read 32k lines first-hand (context cost, 10-15 compactions) |
| D-04 | 2026-11-25 | Test weeks are Feb 2026 onward only | L-09 | Sampling from 2025 |
| D-05 | 2026-11-25 | Web pillars come from a sidecar (aether framework + OpenCode Go Muse Spark 1.3) that fetches DATED pages (as of the Monday anchor) and writes one JSON per week per pair; the Pine indicator reads it as inputs. Price pillars are computed in Pine | L-08/L-09/L-11; Pine cannot fetch; R-02 "one JSON per week" | Price-only E1 (operator rejected) |
| D-06 | 2026-11-25 | Anchor = Monday 02:00 New York time (= London 07:00), the canon's analysis time; a week's forecast is frozen at the first bar at/after it and uses only bars closed before it | L-05 + canon; mechanically checkable | Sunday open; Monday 00:00 UTC |
| D-07 | 2026-11-25 | Golden week (Jul 6-10) is the development oracle; the other report weeks and random weeks are held out and scored once, not tuned on | L-02: accuracy must be uniform; tuning on the test weeks is the failure he describes | Tune per week |
