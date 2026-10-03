# OpenAI API Practice Labs

Twenty small Python exercises covering API troubleshooting, defensive parsing, Responses API calls, structured output, streaming, tools, and the Agents SDK. Synthetic fixtures only. Adapted from personal study exercises; private recruiting materials and employer content are excluded.

Independent, AI-assisted learning project. Not an official OpenAI course, an interview question bank, or a production service.

## Start in VS Code

Open this folder in VS Code. Python 3.12 is recommended. In the terminal:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python labs/01_python_data_structures.py
python labs/03_argparse_demo.py "Explain HTTP 429"
python labs/06_full_offline_analyzer.py fixtures/requests_messy.jsonl
python labs/17_micro_tests.py
python -m unittest discover -s tests -v
```

On Windows, create with `py -3.12 -m venv .venv` and use `.venv\Scripts\python.exe` in place of `python`. Choose the `.venv` with **Python: Select Interpreter**. VS Code launch configurations are included.

## Lab map

| Labs | Topic | Network |
|---|---|---|
| 00 | Environment and SDK import check | None |
| 01–06 | Data structures, numeric conversion, CLI, JSONL, metrics, analyzer | None |
| 07–11 | Responses, error handling, structured output, streaming, tool calls | Explicit `--live` required |
| 12–15 | Basic agent, function tool, handoffs, conversation session | Explicit `--live` required |
| 16–19 | Fake client, tests, deliberate debugging, CSV parsing | None |

## Live examples

Copy `.env.example` to `.env`; enter your own API key and an available model ID. Never commit the real file. The examples fail early without `--live` and both settings.

```bash
python labs/07_basic_response.py --live
python labs/09_structured_output.py --live
python labs/11_function_calling.py --live
python labs/13_agent_with_tool.py --live
```

API billing applies. Model compatibility and access vary. No live API request was made during publication checks. Agents SDK tracing is disabled by default in the shared setup helper. Session lab 15 demonstrates conversation continuity in a local SQLite session, not long-term personalized memory or tenant isolation.

## Learn by changing the examples

1. Predict the output before each run.
2. Add malformed JSON, a non-object row, missing latency, or `NaN` to a copy of the fixture.
3. Explain which records were rejected and which optional values became missing.
4. Explain the difference between valid structured output and a factually correct answer.
5. Trace the manual tool loop: model call, validated arguments, Python execution, matching call ID, next model call.
6. Compare that control flow with the Agents SDK tool example.

`18_debug_me.py` intentionally prints caught errors. It is a debugging exercise, not production-quality utility code. The keyword, numeric, and metrics examples are deliberately small; each documents its assumptions. Empty datasets report no observed error rate (`None` in the analyzer) rather than proof of zero errors.

## Scope and provenance

Reworked from earlier personal, AI-assisted practice examples. The public version fixes an outdated tool decorator, requires explicit live execution and model selection, adds input validation and a bounded manual tool loop, and documents what was actually checked. The code is educational; it does not establish prior customer deployment or production performance.

The account/status tools return synthetic records. They do not access real accounts or implement production authorization. Do not use this as a customer-support service without authentication, tenant isolation, observability, privacy controls, and an evaluation plan.

## References

- [Responses API](https://developers.openai.com/api/docs/guides/responses)
- [Function calling](https://developers.openai.com/api/docs/guides/function-calling)
- [Agent definitions](https://developers.openai.com/api/docs/guides/agents/define-agents)

See `VERIFICATION.md` for publication checks. Contributions should include the learner problem, a reproducible example, and evidence of the fix. Never include credentials, private customer data, or employer/recruiter documents.
