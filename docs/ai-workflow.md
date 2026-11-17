# AI-assisted QA workflow

The root [AGENTS.md](../AGENTS.md) gives Codex project-wide guidance. The [.codex/agents](../.codex/agents) directory defines three project-scoped subagents. Open the repo root in a local Codex client, enable project settings if prompted by that client, and use a new session after changing an agent definition. See the [Codex subagents documentation](https://learn.chatgpt.com/docs/agent-configuration/subagents).

| Agent | Use it to | Example request |
| --- | --- | --- |
| `qa_test_designer` | Review coverage before a run | “Use the qa_test_designer subagent to compare R1–R6 with the eight cases and propose two high-value gaps.” |
| `qa_defect_triage` | Verify and explain a failure | “Use the qa_defect_triage subagent to rerun CK02 on the candidate and draft a report from the result.” |
| `qa_release_reviewer` | Evaluate release evidence | “Use the qa_release_reviewer subagent to check the candidate against the exit criteria and identify what needs retesting.” |

Ask for one role at a time when the next step depends on its findings. Compare every draft to the actual assertion, trace, or observation before relying on it. Playwright reports pass or fail from assertions. The release decision belongs to the reviewer. The demo and CI do not require an AI account or API key.

AI assistance was used to scaffold the portfolio. The packaged evidence records actual browser runs against intentionally seeded behavior. It does not represent employment or production QA experience.
