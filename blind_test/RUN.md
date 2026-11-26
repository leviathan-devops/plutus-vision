# Plutus Vision — run package for a blind test (S5) — one command per week / pair -> one Pine script

You are a fresh reviewer. You render weeks you were given, look at the chart, and count by the rules at the end. You did not build this; do not excuse anything.

## 1. Bring the test bench up (Pinebox = the only test environment)
```
cd /home/user/plutus-vision
export PATH=$HOME/.local/bin:$PATH XDG_RUNTIME_DIR=/run/user/0
pinebox list --session plutus-main | grep -q '"alive":true' || tools/pinebox-bootstrap.sh     # or: pinebox up --session <your-own-name> --adapter xvfb
```
Use your OWN session name if another reviewer shares the machine (`pinebox up --session blind-A --adapter xvfb`); `tools/pb` reads the session `plutus-main` — set `S=` in a copy if you use another.

## 2. One command -> one Pine (v6)
```
cd e1_tool && python3 plutus.py MONDAY PAIR            # PAIR = DXY | EURUSD | GBPUSD ; MONDAY = YYYY-MM-DD of the week's Monday (Feb 2026 .. Nov 2 2026)
# -> e1_tool/out/PLUTUS_<PAIR>_<MONDAY>.pine   (zones, shape chain, setups as data; toggles: show_ip show_lv show_lsz show_opt show_sd show_ltf show_lq show_lq4 show_far show_e2 show_e3)
```
Inputs it reads: TradingView bars in the Pinebox bar store and the option-expiry file `sidecar/out/<MONDAY>.json`; nothing dated after Monday 02:00 New York (check: `python3 tools/leak_check.py PAIR:MONDAY`).
The first run of a week harvests the sealed V1's order blocks / liquidity bands through the Pinebox engine (about a minute, needs Pinebox up); later runs use the cache.

## 3. Render and look
```
tools/e1render PAIR MONDAY 1H show_lv=false show_lq=false                       # -> evidence/e1tool_PAIR_1H_MONDAY.png  (E1TAG=_x adds a suffix)
tools/e1render PAIR MONDAY 1H show_lv=false show_lq=false show_e2=false show_e3=false   # zones only
```
OPEN every frame you cite. A render that printed `"boxes":0` failed. For 15m / 30m frames of an old week use the Backtest tab:
`tools/pb export FILE PAIR 15m` -> `pinebox backtest --session S --op create --name N --symbol PAIR --start <Friday of the week>T20:00 --end <a week later> --tf 15m` -> `tools/pb bt-keep "<script title>"` -> wait 25 s -> `tools/pb goto FROM TO bt` -> `pinebox shot --session S --out F.png`.
Exact numbers (never a verdict): `python3 tools/research/fills.py PAIR MONDAY` prints the day map, every setup (entry / SL / TP) and what the week's 15m candles did to it.

## 4. Counting rules (goal prompt section 7, G1) — per week and pair
- Write BEFORE looking at the setups: every clean zone-to-zone move of the week visible on the 1H chart (the obvious trades).
- E1 = zones that reacted / (zones reached + obvious reaction points of the week that have no zone). A reaction = sharp rejection OR consolidation in / around the zone; a zone crossed like paper is wrong. Flag bloated, bunched, floating or missing zones.
- E2 = days right / 5: forecast shape + direction + key zone vs that day's candles.
- E3 = obvious trades caught / obvious trades that existed; caught = a setup in that direction at that zone that filled and reached TP before SL. Name every stopped-out setup.
- Report the three percentages per map, the lists behind them, and anything on the chart that hides the candles.
