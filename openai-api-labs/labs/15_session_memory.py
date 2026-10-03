import os
from live_setup import require_live
require_live()

"""Lab 15 — Session memory. Requires API credits."""
from dotenv import load_dotenv
from agents import Agent, Runner, SQLiteSession

load_dotenv()
agent = Agent(model=os.environ["OPENAI_MODEL"],name="Support Engineer", instructions="Help troubleshoot concisely and remember what the customer already tested.")
session = SQLiteSession("practice_customer_session")
first = Runner.run_sync(agent, "My API returns 401. I already confirmed the endpoint URL.", session=session, max_turns=4)
print("TURN 1:", first.final_output)
second = Runner.run_sync(agent, "What should I check next?", session=session, max_turns=4)
print("TURN 2:", second.final_output)
