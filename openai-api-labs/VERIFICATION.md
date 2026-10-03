# Publication checks

October 3, 2026; Python 3.12.

- All Python files passed syntax compilation.
- Eleven offline scripts (00–06 and 16–19) completed successfully, including the deliberately broken lab that catches and prints its exercise errors.
- Four analyzer unit tests passed; the original micro-tests also passed.
- OpenAI and Agents SDK imports were checked against the pinned direct dependency versions.
- The manual tool example has a four-round bound and accepts only the synthetic account c123.
- Live examples require an explicit `--live` flag, API key and model selection.

No paid API calls, live model outputs, live streaming, agent handoffs, or live session runs were verified. GitHub CI is supplied but has not yet run at the time this record was written. These are educational examples, not a production support system.

The full analyzer rejects non-object records and invalid HTTP status values. Missing, invalid, negative, boolean, and nonfinite optional latency values become absent samples. Earlier introductory numeric-conversion labs remain small demonstrations with narrower assumptions. Lab 18 is intentionally faulty.
