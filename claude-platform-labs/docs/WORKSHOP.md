# From a model response to a trustworthy workflow

Audience: technical sellers who can run Python but are new to tool use. Outcome: independently explain and run a read-only tool loop, then identify a failure using an evaluation case.

## 45-minute facilitator plan

| Time | Activity | Evidence of learning |
|---|---|---|
| 0–5 | Ask learners to predict whether a model can know a private workshop catalog | Learner identifies missing external data |
| 5–10 | Run lab 1; locate prompt, response, usage, and stop reason | Learner points to each field |
| 10–20 | Trace lab 4: request → tool call → local validation → result → answer | Learner identifies where execution happens |
| 20–28 | Learners add one catalog entry and query it; try an unknown slug | Working lookup and an explained failure |
| 28–35 | Run lab 5; inspect the negation case that breaks a keyword baseline | Learner explains what aggregate accuracy hides |
| 35–40 | Run lab 6; explain tool schema versus MCP transport | Learner distinguishes API tool calls and MCP |
| 40–45 | Teach-back and exit task | Learner demonstrates without reading a script |

## Demo narrative

Start with the business problem: a seller needs accurate prerequisite information during a workshop. The model cannot reliably invent our private catalog. A narrow lookup provides authoritative data. The application decides which function is allowed, checks its arguments, and returns the result. Then the model can explain it conversationally.

Pause on the `tool_use_id`: the result must answer the correct call. Ask the audience what would happen if it referred to a different call. Point out the iteration budget; a broken model/tool interaction must terminate.

When showing evaluation, explain that the offline version measures deterministic keyword baselines, not Claude. The live version uses the same labeled cases with Claude. Seven cases are a smoke test, not a representative production benchmark. Add ambiguous requests, out-of-distribution examples, adversarial text, and independent review before making quality claims.

## Demo failure recovery

- Authentication failure: check environment variable presence without displaying its value; verify the account and model access.
- Rate limit: explain concurrency and token limits; use the offline lab to preserve the learning objective.
- Broken model response: inspect stop reason and request ID. Do not imply partial output is a successful result.
- MCP issue: run `python -m labs.06_mcp` independently to isolate transport/tool discovery from model behavior.
- Install failure: use a known working machine or walk through checked-in fixtures, explicitly labeling the fallback.

## Teach the teacher

Ask another instructor to deliver the tool lab with no help. Score 0–2 on: accurate explanation; learner participation; independent task completion; recovery from an unknown slug; honest limitations. Require no zero and at least 8/10 before solo delivery. This is a proposed teaching rubric, not an employer's assessment.

Measure first successful run, completion without instructor help, time to recover from a broken example, and repeat usage after one week. Track satisfaction as a secondary signal. Compare pre/post skill checks; do not attribute revenue changes to one class without a credible design.
