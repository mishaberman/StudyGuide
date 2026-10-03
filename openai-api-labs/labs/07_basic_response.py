from live_setup import require_live
require_live()

"""Lab 07 — Basic Responses API. Requires API credits."""
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
MODEL = os.environ["OPENAI_MODEL"]
client = OpenAI()

prompt = """
A customer reports repeated HTTP 429 responses.
Explain the likely category of problem and list three things a support engineer should check.
"""

print("Model:", MODEL)
print("Sending request...")
response = client.responses.create(model=MODEL, input=prompt)
print("Request completed.\n")
print(response.output_text)
