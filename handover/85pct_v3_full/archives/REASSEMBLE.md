# Archives on this branch - how to reassemble and verify

This branch is a self-contained handover (operator M-63 / ruling L-59, verbatim in `memory/12` and `memory/04` on the branch `AGENT`):
- the branch's tree IS the repository at the handover (code, memory, evidence frames, OmniGraph, sidecar data);
- its history IS the git history of that line.

The parts below are what was NOT in git: session transcripts, the uploaded inputs, the scratchpad, the test-bench state, the OmniGraph archive.

GitHub refuses files over 100 MiB, so every archive is split into pieces of at most 95 MiB (`<archive>.zip.part00`, `.part01`, ...).

**Reassemble one archive:**

    cat <archive>.zip.part* > <archive>.zip
    sha256sum -c SHA256SUMS --ignore-missing     # the whole-archive hash must match
    unzip <archive>.zip -d <somewhere>

`SHA256SUMS` lists every piece and every reassembled archive.

**Public-repository note:** this repository is PUBLIC.
- The transcripts, inputs, scratchpad and test-bench parts on this branch are REDACTED copies; see `REDACTION_AND_SCAN.md`.
- The unredacted originals were delivered to the operator privately (chat file upload) and are not in git.


## Files on this branch

| Archive (reassembled) | Pieces | Bytes |
|---|---|---|
| `PLUTUS_VISION_85pct_V3__4_TRANSCRIPTS_REDACTED.zip` | 3 | 235565045 |
| `PLUTUS_VISION_85pct_V3__5_INPUTS_REDACTED.zip` | 1 | 82485316 |
| `PLUTUS_VISION_85pct_V3__6_SCRATCHPAD_REDACTED.zip` | 1 | 70059655 |
| `PLUTUS_VISION_85pct_V3__7_TESTBENCH_STATE_REDACTED.zip` | 1 | 16284895 |
| `PLUTUS_VISION_85pct_V3__8_OMNIGRAPH.zip` | 1 | 2583026 |
