# GitHub handoff

1. Extract the ZIP and open the `checkout-qa-case-study` folder in Codex. Keep the hidden `.github` and `.codex` directories.
2. Review the [README](../README.md) and [AI workflow](ai-workflow.md) and reproduce at least one candidate failure. Be ready to explain how its behavior affected the release decision.
3. Sign in to GitHub with the account that should own the repo. Use GitHub Desktop to add the local folder, create a repository when prompted, and choose **Publish repository**. Choose the intended owner and visibility.
4. On GitHub, confirm that the root README renders and that **Actions → Checkout regression** completed successfully. If a run failed, open the job and download its test artifacts for diagnosis.

## Publish with Codex and GitHub CLI

If `gh` is installed and signed in to the intended account, ask Codex to verify the account with `gh auth status` and publish the project under the requested visibility. From the repo root, the equivalent commands for a new public portfolio repo are:

```sh
git init -b main
git add .
git diff --cached --stat
git commit -m "Add checkout QA portfolio case study"
gh repo create checkout-qa-case-study --public --source=. --remote=origin --push
```

Use `--private` if desired. Git needs a commit identity on first use. The project package has no preconfigured remote or account credentials.

**Suggested GitHub description:** QA portfolio case study with a checkout demo, Playwright regression, reproducible defects, a release decision, and Codex QA agents.

**Suggested topics:** `quality-assurance`, `playwright`, `pytest`, `github-actions`, `portfolio`
