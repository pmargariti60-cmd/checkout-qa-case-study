# Test plan

**Objective.** Determine whether a shopper sees the correct amount and can place exactly one demo order per checkout session.

**Priority.** Incorrect totals and repeat submissions are release blockers. Code entry and ambiguous feedback are next because shoppers need to know whether savings applied.

**Setup.** Use a fresh page for every case. Run on local headless Chromium for regression, then compare the reference and candidate using identical data. The procedures below also work as a manual checklist.

| Case | Requirement | Actions | Expected result |
| --- | --- | --- | --- |
| CK01 | R1 | Open a fresh checkout. | Discount $0.00, total $55.00. |
| CK02 | R2 | Apply `SAVE10`. | Apply confirmation, $5.00 discount, $50.00 total. |
| CK03 | R3 | Apply `  save10  ` with two spaces on each side. | Code accepted and $5.00 discount applied. |
| CK04 | R4 | Apply `EXPIRED` on a fresh page. | Rejection message, $0.00 discount, $55.00 total. |
| CK05 | R4, R5 | Apply `SAVE10` twice and submit. | $5.00 discount and first-order confirmation for $50.00. |
| CK06 | R5 | Submit with no discount. | Confirmation shows `FS-0001` and $55.00. |
| CK07 | R6 | Submit once and check the order button. | First confirmation stays visible and the order button is disabled. |
| CK08 | R4 | Apply `SAVE10`, then `EXPIRED`. | Rejection explicitly says `SAVE10` remains applied. The $5.00 discount stays. |

After CK07 fails, click again on the candidate and record whether the confirmation changes. Check keyboard entry and zoom or narrow layouts as exploratory work. This exercise records a keyboard check. A broad accessibility audit and Firefox, WebKit, and real-device coverage are outside the decision.

**Exit criteria.** All checks pass on the proposed release build, with CK03 eligible for an explicit product deferral. The two blocking defects must also pass manual retest.
