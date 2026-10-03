# Claude Platform Teaching Labs

Ten small Python labs for learning to explain, demonstrate, troubleshoot, and evaluate AI integrations. Each uses synthetic data. Start offline; opt in to billable model calls with `--live`.

This is an independent, AI-assisted educational project, not an official Anthropic course or a production service. Offline fixture results are not evidence of model quality. Live model behavior has not been verified in the authoring environment. See `VERIFICATION.md` for checks actually performed.

## Start in Visual Studio Code

Requirements: Python 3.12 recommended, VS Code, and Microsoft's Python extension. Unzip this folder, choose **File > Open Folder**, and open the terminal in this folder.

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m labs.04_tool_loop
python -m labs.05_evaluation
python -m labs.06_mcp
python -m pytest -q
```

Windows PowerShell: create with `py -3.12 -m venv .venv`, then use `.venv\Scripts\python.exe` in place of `python` in the commands above. Activation is optional.

In VS Code, run **Python: Select Interpreter** and choose this folder's `.venv`. Use Run and Debug to select a provided launch configuration. Run modules from the project root; do not run the files by path, because they import `labs.common`.

## Optional live calls

Copy `.env.example` to `.env`. Set an API key and a model ID available in your Claude Console. The project deliberately does not guess your model access. Never paste keys into code or chat.

```bash
python -m labs.01_messages --live
python -m labs.02_streaming --live
python -m labs.03_structured --live
python -m labs.04_tool_loop --live
python -m labs.05_evaluation --live
python -m labs.09_agent_sdk --live
```

Live labs use the API account's billing and limits. The evaluation makes seven classification requests; the tool loop permits up to four model rounds. Set a Console budget appropriate for practice. A Claude consumer subscription is not a substitute for configuring API credentials for these examples. Structured-output model support and account availability must be checked against the current docs. The Agent SDK may require its bundled native binary to be supported on your machine.

## Learning path

| Lab | Run module | What you should be able to teach | Mode |
|---|---|---|---|
| 1 | `labs.01_messages` | Request, content blocks, stop reason, token usage | Offline illustration / live |
| 2 | `labs.02_streaming` | First-text latency versus completion; partial failure | Offline illustration / live |
| 3 | `labs.03_structured` | Schema validity versus factual correctness | Offline fixture / live |
| 4 | `labs.04_tool_loop` | Model proposes; application validates and executes | Local tool execution / live loop |
| 5 | `labs.05_evaluation` | Labeled cases, failures, regressions, denominator | Offline baselines / live |
| 6 | `labs.06_mcp` | Discover and call a tool through MCP | Real local protocol, no LLM |
| 7 | `labs.07_reliability` | Permanent errors, backoff, retry budgets | Offline |
| 8 | `labs.08_content_freshness` | Detect curriculum drift and assign review | Synthetic snapshots |
| 9 | `labs.09_agent_sdk` | Managed loop versus manual loop; explicit tools | Offline plan / optional live |
| 10 | `labs.10_log_analyzer` | Robust parsing, rejection counts, p95 | Offline |

Read `docs/WORKSHOP.md` for a 45-minute facilitator plan and `docs/EXERCISES.md` for challenges and answer hints.

## Architecture and teaching boundaries

Labs 1–5 call the first-party Claude API in live mode. Lab 4 executes only a read-only, allowlisted local lookup. Lab 6 demonstrates MCP discovery and invocation using a real in-process client/server, without connecting it to Claude. Lab 9 demonstrates the Agent SDK separately with no tools enabled. These are deliberately distinct teaching units, not a claim of a deployed end-to-end MCP agent.

No tenant authentication, production monitoring, persistent user memory, cloud-provider deployment, or production-grade prompt-injection defense is implemented. Prompt instructions are not a security boundary. A real system needs server-side authorization, data isolation, observability, and idempotency for side effects.

## Maintenance and contribution

Before updating SDK versions: run the offline tests, run the opt-in live smoke checks with synthetic data, update `VERIFICATION.md`, and review affected lesson instructions. Direct dependencies are pinned to versions tested during creation; transitive dependencies are not fully locked. CI is offline only.

Contributions should include the learner problem, a minimal reproducible example, expected behavior, and a test for substantive logic changes. Avoid credentials, employer data, recruiter packets, and private customer examples.

## Attribution

Created with AI assistance as a personal learning and teaching project. The log-analysis lab adapts a prior personal API troubleshooting practice exercise; it was rewritten to reject non-object records, booleans, nonfinite values, and invalid status codes. No employer implementation or proprietary interview prompt is included. A new practice repository is a portfolio artifact; it does not imply past production adoption or an accepted contribution to someone else's open-source project.

## Official references

- [Messages API](https://platform.claude.com/docs/en/build-with-claude/working-with-messages)
- [Structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)
- [Tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works)
- [Python SDK](https://github.com/anthropics/anthropic-sdk-python)
- [Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview)
- [FastMCP client](https://gofastmcp.com/clients/client)
- [MCP specification](https://modelcontextprotocol.io/specification/latest)

Reference review date: October 3, 2026. Verify current model availability before a live workshop.
