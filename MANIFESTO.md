# QA Manifesto

1. **Start with user impact.** Prioritize failures that change a total, create a duplicate order, or leave the customer unsure what happened.
2. **Agree on expected behavior before testing it.** Link each case to a requirement and record product questions when the expected outcome is unclear.
3. **Make reports reproducible.** Include the build, data, steps, expected result, actual result, and the evidence a teammate needs to repeat the observation.
4. **Automate predictable checks.** Use deterministic fixtures and stable assertions for regression coverage. Use exploratory sessions for interactions the suite may miss.
5. **State the limits of a release decision.** Identify what ran, what failed, what remains outside scope, and what evidence would change the recommendation.
6. **Review AI output against evidence.** Use agents for coverage ideas and draft triage. A human verifies material claims, sets severity, and owns sign-off.
