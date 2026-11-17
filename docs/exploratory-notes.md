# Exploratory session notes

A targeted browser replay used Playwright with Chromium 148.0.7778.96 on macOS on 17 November 2026. Each investigation began with a fresh checkout.

## Charter 1 · Compare the displayed and confirmed amounts

- Applied `SAVE10` on the candidate. The discount showed $5.00 while the total stayed at $55.00.
- Submitted the demo order. The confirmation showed $50.00.
- Recorded the pre-submit view as [QA-01 evidence](evidence/qa-01-stale-total.png). The automated check fails at the displayed total, so the confirmation discrepancy was verified in this replay.

## Charter 2 · Try a second submission

- Clicked **Place demo order** once on a fresh candidate and saw `FS-0001`.
- Clicked again and saw `FS-0002`. The automated check catches the enabled button. The replay establishes the visible consequence.
- Captured [the second confirmation](evidence/qa-02-second-order.png).

## Charter 3 · Navigate and submit with the keyboard

- On the reference, used Tab to reach the code field, typed `  save10  `, then used Tab and Enter to apply it.
- Verified that the total read $50.00. Pressed Tab and Enter to place the order and observed `FS-0001` at $50.00. The submit button became disabled.
- This session checked focus order and activation for the documented keyboard path. Screen reader behavior, zoom, and narrow layouts were not assessed.

See the [regression summary](evidence/run-summary.md) for the scope of the automated runs.
