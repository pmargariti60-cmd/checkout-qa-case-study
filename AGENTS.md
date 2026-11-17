# Repository instructions for AI contributors

Read the [manifesto](MANIFESTO.md) and the [requirements](docs/requirements.md) before changing tests or evaluating release readiness.

- Run `python -m pytest -q` using the repository's virtual environment. Add `--build candidate` to replay the known defects. Preserve requirement-based assertions and fresh browser state.
- Treat [published evidence](docs/evidence/run-summary.md) as historical. Label new run results with the build and browser actually tested. Keep hypotheses distinct from observations.
- The candidate deliberately contains QA-01, QA-02, and QA-03. Preserve the exhibit unless the task explicitly asks to build a fixed candidate.
- Report any checks you could not execute. Keep claims scoped to the simulated checkout.
- Look in `.codex/agents/` for the custom roles and [the AI workflow](docs/ai-workflow.md) for prompts.
