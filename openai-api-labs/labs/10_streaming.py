from live_setup import require_live
require_live()

"""Lab 10 — Streaming Responses API text. Requires API credits."""
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()
model = os.environ["OPENAI_MODEL"]
stream = client.responses.create(
    model=model,
    input="Explain a systematic way to troubleshoot HTTP 500 errors.",
    stream=True,
)
for event in stream:
    if event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)
    elif event.type == "response.completed":
        print("\n\n[response completed]")
    elif event.type == "error":
        print("\n[stream error]", event)
