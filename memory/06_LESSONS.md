# 06 — LESSONS (append-only: mistakes, measured surprises, things that cost time)

- LS-01 (2026-10-12) I told the operator Ars Umbris was "macOS-only, cannot run". The README said "tested on macOS only, Linux may work". Do not turn "untested" into "impossible"; try it.
- LS-02 (2026-11-25) I told the operator past option boards / analyst notes are "no longer online". Wrong: investinglive keeps every dated FX-option-expiry post for 2026. Check before asserting something does not exist.
- LS-03 (earlier sessions) My OHLC-only lab forecaster scored below "always range" and my E1 reconstruction showed no edge vs shifted baselines. Cause: zones chosen by proximity, no zone state, no external pillars. Do not repeat proximity-only zone selection.
- LS-04 The previous agents were rejected for: script-graded "passes" with a chart that did not react; caps to hide 33-57 junk zones (R-37); hardcoded per-week values; relabelling instead of root-causing. Any of these = failure.
- LS-05 Pinebox on a root container: needs iproute2 (`ss`), x11-utils (`xdpyinfo`), Chromium `--no-sandbox` wrapper. `pinebox up` refuses by name; read the token, fix the cause.
- LS-06 The ECC GateGuard hook denies the first write to a new directory's first file and the first Bash call; siblings pass afterwards. Present the facts once, retry.
- LS-07 `update_environment` rejects the whole call if one host is unacceptable (web.archive.org / tradingview / bare apex duplicates were in the rejected set). Send a minimal exact list.
- LS-08 (2026-11-25) Eight parallel high-effort reader agents hit the 5-hour usage limit and four died with nothing written. Run <= 2-3 agents at once, narrow scope, and have each write its file incrementally (partial file first) so a kill leaves something.
- LS-09 vela-pinets: `x[1]` inside an `if`/function-local block returns x[0]. Read history ONLY at global scope into named series (close1 = close[1]) and use those. The anchor assert caught this; keep the assert forever.
- LS-10 First Write to a brand-new file path costs a full resend when the gate denies it: first-touch new files with a one-line placeholder, then write the real content.
- LS-11 Pine `for i = a to b` counts DOWN when a > b. Guard every loop whose bounds can cross.
