import os
from live_setup import require_live
require_live()

"""Lab 12 — Basic Agents SDK. Requires API credits."""
from dotenv import load_dotenv
from agents import Agent, Runner

load_dotenv()
agent = Agent(model=os.environ["OPENAI_MODEL"],
    name="API Support Engineer",
    instructions="You are a concise technical support engineer. Identify likely cause, evidence to gather, and next steps.",
)
result = Runner.run_sync(agent, "Customer reports HTTP 429 errors after traffic increased 5x.", max_turns=4)
print(result.final_output)
