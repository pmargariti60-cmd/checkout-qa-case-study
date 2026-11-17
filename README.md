# Checkout QA Case Study

A QA portfolio project for a simulated storefront release. It covers requirement review, risk-based test design, browser automation, defect reporting, and a release decision backed by reproducible evidence.

**Release decision:** Hold the candidate. An accepted discount leaves the advertised total stale, and a confirmed order can be submitted again. The lower-priority code-entry defect is documented separately. All three defects were deliberately seeded for this exercise.

[Review the release decision](docs/release-decision.md) · [See the run evidence](docs/evidence/run-summary.md) · [Read the test plan](docs/test-plan.md)

## Run the case study locally

Use Python 3.9 or newer. CI uses Python 3.12. From the repository root:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m playwright install chromium
python -m pytest -q
```

On Windows PowerShell, replace the first two commands with `py -m venv .venv` and `.\.venv\Scripts\Activate.ps1`. On Linux, use `python -m playwright install --with-deps chromium` to install browser system dependencies as well.

The tests start and stop a local server automatically. The default reference build should pass all eight checks. To replay the candidate:

```sh
python -m pytest -q --build candidate --tracing retain-on-failure --screenshot only-on-failure --output test-results/browser --junitxml=test-results/candidate.xml
```

The candidate should finish with five passes and three assertion failures and exit with code 1. Compare the failed case IDs and assertions to the [run summary](docs/evidence/run-summary.md). To inspect a trace, run `python -m playwright show-trace` followed by its `trace.zip` path under `test-results/browser/`.

### Explore in a browser

Run `python -m http.server 8000 --bind 127.0.0.1 --directory demo` and open:

- Reference at `http://127.0.0.1:8000/`
- Candidate at `http://127.0.0.1:8000/?build=candidate`

Both start with a $50.00 item and $5.00 shipping. Use `SAVE10` for a $5.00 discount. Reload for a fresh checkout. This is a simulation with fixtures and no payment or backend.

## Review the portfolio

- [Requirements](docs/requirements.md) define the expected behavior.
- [Test plan and manual cases](docs/test-plan.md) map requirements, risks, and checks.
- [Exploratory notes](docs/exploratory-notes.md) record a keyboard check and a repeat submission investigation.
- [Defect reports](docs/defects.md) include severity, steps, and screenshots.
- [Release decision](docs/release-decision.md) states the hold criteria and retest scope.
- [QA manifesto](MANIFESTO.md) describes the team's working principles for this exercise.
- [AI workflow](docs/ai-workflow.md) shows how to use the three Codex agents included in this repo.

The [GitHub Actions workflow](.github/workflows/checkout.yml) runs the reference regression suite on pushes and pull requests and uploads test artifacts. Candidate replay is a separate local exercise.

## Publish to GitHub

Extract the project if you received a ZIP. Open the extracted `checkout-qa-case-study` folder in Codex and read the [GitHub handoff](docs/github-handoff.md). The workflow, hidden configuration files, and evidence are already included.
