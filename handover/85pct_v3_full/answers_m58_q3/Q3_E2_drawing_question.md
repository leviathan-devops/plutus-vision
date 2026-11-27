# Q3 — How should the forecast shape chain be drawn?

Three pictures:

1. **Your library** (`your_library_GBPUSD_Feb26-Mar3_shape_boxes.png`, GBPUSD 15m, 26 Feb - 3 Mar 2026): one labelled box per shape - RECOVERY SURGE, PIERCING WHIPLASH, SWING SCALPS, PIERCING BREAKOUT SURGE, RECOVERY, WHIPLASH. Each box is drawn around the move: its **height = the price range that shape traded**, its **width = the hours it lasted**. There is no zigzag line. Your Macro Shape Library PDF is drawn the same way.
2. **Mine today on a range week** (`mine_now_EURUSD_Oct5_range_week.png`): five identical day boxes "SS 80%" and a yellow zigzag that touches the floor and the ceiling once a day. The zigzag is a template: the code draws one swing every two sessions between the two range bounds. It does not know when or where a swing will turn. That is the "generalized, watered-down line" you saw. Actual price broke above it on Tuesday (1.1277) and below it on Wednesday (1.1165), at times the line does not show.
3. **Mine on the golden week** (`mine_now_DXY_Jul6_golden_week.png`): here the chain is right (range, retest up, breakdown, whiplash), so the same kind of line looks accurate.

With the daily anchoring you approved, the map can be rebuilt every morning at London open from the data up to that moment. The question is what the forecast should draw:

- **Option A - your library style.** Labelled boxes per shape, forecast. Example for Tuesday: "SWING SCALPS - Tue London to NY - between floor 1.1171 and ceiling 1.1249". Example for a breakout day: "BREAKOUT SURGE - Wed NY - from 1.1171 down to the next zone 1.1150". No line.
- **Option B - today's style, honest.** A day box plus a line that only goes from the morning's price to that session's target zone (one leg for London, one for NY), redrawn every morning. No invented swings.
- **Option C - both.** Shape boxes (A) with the session legs (B) inside them.

**Q3a.** A, B or C?
**Q3b.** Inside a SWING SCALPS shape: should the forecast draw the individual swings (when and where each one turns), or only the box (floor, ceiling and the hours)? Your library boxes show only the box.
