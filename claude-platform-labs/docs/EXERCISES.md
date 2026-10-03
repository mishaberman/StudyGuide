# Practice by predicting, changing, and teaching

For every lab: predict the output, run it, change one input, explain the result to a beginner, then explain the engineering trade-off to a developer.

| Lab | Challenge | Hint / success check |
|---|---|---|
| Messages | Reduce output budget and handle incomplete output | Check `stop_reason`; do not silently accept truncation |
| Streaming | Explain a failure after the first text chunk | UI must label partial output; retrying can duplicate visible text |
| Structured | Add a new category and update fixtures | Schema validity does not prove the chosen category is right |
| Tools | Add a `streaming` catalog item; try an unknown tool | Only allowlisted functions execute; never use `eval` on a tool name |
| Evaluation | Add two negation cases without patching only exact strings | Preserve a held-out set; report individual failures and sample size |
| MCP | Add a second read-only tool and inspect discovery | It must appear in `list_tools`; server logic remains independently testable |
| Reliability | Add support for an HTTP-date Retry-After header | Respect deadlines; do not retry 401 forever; avoid nested SDK retries |
| Freshness | Attach affected lesson IDs and a review owner to each changed field | A detected change opens review; it does not auto-approve rewritten content |
| Agent SDK | Explain how you would safely add a read-only catalog tool | Explicit allowlist, scoped data, permissions; no bypass mode |
| Logs | Add negative latency, null row, and empty input | Rejection counts and sample denominators remain clear |

## Deliberate debugging exercise

Write a function that averages `float(row['latency_ms'])` across every row. Test it with an empty list, missing field, `banana`, `NaN`, and a negative number. Explain why avoiding an exception alone is not sufficient: `NaN` can silently poison metrics.

## Instructor assessment

Record a five-minute explanation of lab 4. Watch it without sound: is the cursor pointing at the step being described? Listen without video: can a learner follow the concept? Cut unnecessary implementation detail, then record again.

## Beyond this repository

Provider comparison exercise: choose first-party API, Bedrock, Vertex, or Foundry. Before porting, verify identity setup, endpoint, model identifier, region, quotas, feature parity, billing, and network controls in that provider's current docs. This repository does not claim cloud deployments have been completed.

Memory exercise: design a tenant-scoped store for learning preferences. Specify consent, retention, deletion, and protection against instructions embedded in remembered text. Distinguish this persistent state from merely resending conversation history.

Skills exercise: explain how reusable task instructions differ from a callable tool or an MCP server. Draft the outline of a lesson-review procedure; do not treat instructions as authorization to execute arbitrary code.
