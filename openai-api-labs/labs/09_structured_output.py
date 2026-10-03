from live_setup import require_live
require_live()

"""Lab 09 — Structured output with Pydantic. Requires API credits."""
import os
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel

class TicketAnalysis(BaseModel):
    category: str
    severity: str
    likely_cause: str
    should_escalate: bool

def main():
    load_dotenv()
    client = OpenAI()
    model = os.environ["OPENAI_MODEL"]
    ticket = "Customer says every API request started returning HTTP 401 this morning. It worked yesterday."
    response = client.responses.parse(
        model=model,
        input=[
            {"role": "system", "content": "You are a concise technical support engineer."},
            {"role": "user", "content": ticket},
        ],
        text_format=TicketAnalysis,
    )
    analysis = response.output_parsed
    if analysis is None:
        raise RuntimeError("No parsed result: inspect refusal or incomplete output")
    print(analysis.model_dump_json(indent=2))

if __name__ == "__main__":
    main()
