import os
from live_setup import require_live
require_live()

"""Lab 13 — Agent + scoped Python tool. Requires API credits."""
from dotenv import load_dotenv
from agents import Agent, Runner
from agents import function_tool

load_dotenv()

@function_tool
def get_recent_errors(customer_id: str) -> str:
    """Return fake recent API-error information for a customer."""
    print(f"TOOL CALLED for {customer_id}")
    return "Last 10 minutes: 17 HTTP 429 errors, 0 HTTP 500 errors, account active, traffic increased 8x."

agent = Agent(
    model=os.environ["OPENAI_MODEL"],
    name="Support Engineer",
    instructions="Diagnose API support issues. Use the recent-error tool when it helps. Explain likely cause, evidence, and next steps.",
    tools=[get_recent_errors],
)
result = Runner.run_sync(agent, "Customer c456 says the API suddenly stopped working under heavy traffic.", max_turns=4)
print(result.final_output)
