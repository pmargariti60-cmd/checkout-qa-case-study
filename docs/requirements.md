# Checkout requirements

Field Supply is a fictional retailer. A fresh checkout contains one $50.00 bag and $5.00 shipping. All amounts are USD. The two fixtures share the same requirements.

- **R1 · Initial summary.** A fresh checkout shows a $0.00 discount and a $55.00 total.
- **R2 · Valid discount.** `SAVE10` applies 10% to the $50.00 merchandise subtotal. Shipping stays $5.00. Show a $5.00 discount, a $50.00 total, and confirmation that the code was applied.
- **R3 · Code entry.** Ignore leading and trailing spaces and letter case when matching the code.
- **R4 · Invalid or repeated code.** An unknown code shows a clear message and preserves the current discount. Applying `SAVE10` again keeps the discount at $5.00.
- **R5 · Order confirmation.** The first submission shows a reference and the amount for the current order.
- **R6 · Single submission.** After confirmation, the shopper cannot submit the same checkout again during that page session.

Checkout state is in memory and resets on reload. The simulation covers browser behavior only. Inventory, tax, authentication, payment, and backend idempotency are outside scope.
