# Candidate defect reports

All findings are deliberately seeded defects reproduced against the local candidate. Start each reproduction on a fresh candidate checkout at `/?build=candidate`. Setup and commands are in the [README](../README.md).

## QA-01 · Total stays at $55.00 after applying SAVE10

**Severity:** High · **Disposition:** Blocks release · **Requirement:** R2 · **Case:** CK02

1. Open the candidate checkout.
2. Enter `SAVE10` and activate **Apply code**.
3. Compare the discount and total in the order summary.

**Expected.** The order summary shows a $5.00 discount and a $50.00 total.  
**Actual.** The code is accepted and the discount shows $5.00. The total stays at $55.00.  
**Impact.** The shopper sees an incorrect price before committing. The demo confirmation uses $50.00, so the two views disagree. This exercise does not involve a payment.

[Candidate screenshot](evidence/qa-01-stale-total.png) · [Run summary](evidence/run-summary.md)

## QA-02 · Shopper can submit again after confirmation

**Severity:** High · **Disposition:** Blocks release · **Requirement:** R6 · **Case:** CK07

1. Open the candidate checkout.
2. Click **Place demo order** and observe reference `FS-0001`.
3. Click **Place demo order** again.

**Expected.** The second submission is unavailable and the original confirmation remains.  
**Actual.** The button remains enabled. The second click changes the confirmation to `FS-0002`.  
**Impact.** A single checkout can produce two simulated order references. In a real checkout, a similar UI failure would require backend investigation before drawing conclusions about duplication or charging.

[Second-submission screenshot](evidence/qa-02-second-order.png) · [Run summary](evidence/run-summary.md)

## QA-03 · Lowercase promo code is rejected

**Severity:** Medium · **Disposition:** Fix or obtain an explicit deferral · **Requirement:** R3 · **Case:** CK03

1. Open the candidate checkout.
2. Enter `  save10  ` with two spaces on each side.
3. Activate **Apply code**.

**Expected.** The normalized code is accepted and the $5.00 discount appears.  
**Actual.** The candidate displays “Code not recognized.” The discount stays at $0.00.  
**Impact.** Shoppers can lose an eligible discount when typing the code in lowercase. Uppercase `SAVE10` is accepted.

[Candidate screenshot](evidence/qa-03-code-rejected.png) · [Run summary](evidence/run-summary.md)
