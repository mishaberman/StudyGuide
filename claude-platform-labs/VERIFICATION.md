# Verification record

Creation date: October 3, 2026.

- Python 3.12; direct dependency versions are in `requirements.txt`.
- **11 offline tests passed** in the authoring environment.
- All ten lab entry points completed in their default offline/local mode.
- Actual Anthropic SDK request serialization, structured response parsing, and a two-response tool cycle were exercised with a mock HTTP transport. No model was called in those tests.
- A real local FastMCP client discovered `lookup_workshop` and retrieved its synthetic record.
- Tool allowlisting, argument validation, round limits, incomplete responses, retry decisions, content changes, and malformed/nonfinite log values were checked.
- Agent SDK options were instantiated with tools disabled; the Agent SDK model runtime was not run live.
- The restricted authoring sandbox stalled on the local MCP check; the same check and full suite completed outside that sandbox. This was an execution-environment limitation observed here.

## Not yet verified

Live model outputs, live streaming, provider-specific model availability, cloud-provider deployments, API billing behavior, and GitHub-hosted CI have not been tested. The CI workflow is supplied for future execution. No claim is made that this is production-ready.

Before presenting live: run labs 1–4 with `--live`, use a model available to your account, test an unknown slug, and rehearse the offline fallback. Record your observed outputs and dates separately. Do not replace this verification record with claims you have not checked.
