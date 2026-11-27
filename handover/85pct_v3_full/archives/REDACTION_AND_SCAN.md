# Redaction and credential scan of the archives on this branch

The repository `leviathan-devops/plutus-vision` is PUBLIC. The operator asked for everything to be pushed (M-63). His account identifiers from the session context are not published.

## Redaction

| Original | Replaced by | Where it occurs |
|---|---|---|
| the operator's e-mail address | `<operator-email>` | session context in the transcripts |
| the e-mail's local part (also his Pinebox Cloud workers.dev subdomain) | `<operator-handle>` | transcripts; his uploaded Pinebox package docs; the test bench's `stages/cloud.sh` |
| his claude.ai organization id (GitHub-connect URL) | `<org-id>` | transcripts |
| cloud environment ids `env_01...` | `<env-id>` | transcripts (environment tool results) |
| scheduled-task ids `trig_01...` | `<trigger-id>` | transcripts (check-in scheduling) |

**Scope of the replacement:**
- applied to every TEXT file inside the archives that contained one of these strings;
- binary files carried none;
- verified afterwards: no occurrence left;
- nothing else in the files was changed.

The session id in the transcripts is the same one every commit trailer of this repository already carries, so it is not replaced.

The unredacted originals exist only in the archives delivered privately to the operator (chat file upload). Their SHA-256 sums are listed below for reference.

## Credential scan (before the push)

**Patterns searched** inside every archive (unpacked):
- `sk-ant-...`, `sk-...` (32+);
- `ghp_...`, `github_pat_...`;
- Slack `xox*-`;
- private-key blocks;
- Google `AIza...`;
- AWS `AKIA...`.

**Result** (per archive, from the build log):
- no API key, token or private key;
- the only AWS-pattern hit is `AKIAIOSFODNN7EXAMPLE`, the documented AWS example key, inside a public npm package (`@aws-sdk` type declarations) of the uploaded aether backend.
- The OpenCode key used by the sidecar was never in any file: it is injected by the network proxy.

**Inside the zips:** GitHub's own secret scanning does not look inside zip files, so this scan is the check of record.

## Build log of the redaction and the scan

```
== B redacted copies for the public branches
70_4_TRANSCRIPTS_REDACTED.zip: 54 files redacted, identifiers left 0
INPUTS_REDACTED.zip: 36 files redacted, identifiers left 0
70_6_SCRATCHPAD_REDACTED.zip: 0 files redacted, identifiers left 0
70_7_TESTBENCH_STATE_REDACTED.zip: 1 files redacted, identifiers left 0
85_4_TRANSCRIPTS_REDACTED.zip: 57 files redacted, identifiers left 0
85_6_SCRATCHPAD_REDACTED.zip: 1 files redacted, identifiers left 0
85_7_TESTBENCH_STATE_REDACTED.zip: 1 files redacted, identifiers left 0
== B scan of the redacted copies for credentials (text inside the zips)
70_4_TRANSCRIPTS_REDACTED.zip: credential hits 1, AWS keys other than the documented example 0
70_6_SCRATCHPAD_REDACTED.zip: credential hits 0, AWS keys other than the documented example 0
70_7_TESTBENCH_STATE_REDACTED.zip: credential hits 0, AWS keys other than the documented example 0
85_4_TRANSCRIPTS_REDACTED.zip: credential hits 1, AWS keys other than the documented example 0
85_6_SCRATCHPAD_REDACTED.zip: credential hits 0, AWS keys other than the documented example 0
85_7_TESTBENCH_STATE_REDACTED.zip: credential hits 0, AWS keys other than the documented example 0
INPUTS_REDACTED.zip: credential hits 0, AWS keys other than the documented example 0
BUILD_DONE
```

## SHA-256 of the UNREDACTED originals (delivered privately, not in git)

```
80acd43279b7dcee41442039ed03e33cf3f02bf880a4f13a96386bbd7dd31faa  PLUTUS_VISION_85pct_V3__4_TRANSCRIPTS.zip
d9ddce89eccb73d3e87f74a5bcd322d8d63775a8eb5b9f9746cf4c7306f64d57  PLUTUS_VISION_85pct_V3__5_INPUTS.zip
c0072f79e07e2e60a03ce3671e47da1a02e9604644631e753748acbc6dfa1b07  PLUTUS_VISION_85pct_V3__6_SCRATCHPAD.zip
69a561fa8e75d3ab4f8a92fc8e10d3dea45ea89d4cf8147f3a6e0bea0b7cf44d  PLUTUS_VISION_85pct_V3__7_TESTBENCH_STATE.zip
```
