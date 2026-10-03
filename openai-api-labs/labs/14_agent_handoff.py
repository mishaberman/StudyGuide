import os
from live_setup import require_live
require_live()

"""Lab 14 — Multi-agent routing with handoffs. Requires API credits."""
from dotenv import load_dotenv
from agents import Agent, Runner

load_dotenv()
billing_agent = Agent(model=os.environ["OPENAI_MODEL"], name="Billing Specialist", handoff_description="Handles billing and credit issues.", instructions="Resolve billing questions concisely.")
api_agent = Agent(model=os.environ["OPENAI_MODEL"], name="API Support Specialist", handoff_description="Handles API errors, authentication, rate limits and integrations.", instructions="Troubleshoot technical API issues.")
triage_agent = Agent(model=os.environ["OPENAI_MODEL"], name="Support Triage", instructions="Route the customer to the correct specialist.", handoffs=[billing_agent, api_agent])
result = Runner.run_sync(triage_agent, "My requests are returning HTTP 401. Can you help?", max_turns=4)
print(result.final_output)
print("Final agent:", result.last_agent.name)
