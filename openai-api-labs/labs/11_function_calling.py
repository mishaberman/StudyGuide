from live_setup import require_live
require_live()

"""
Lab 11 — Manual function/tool calling with Responses API. Requires API credits.
The MODEL requests a tool. YOUR PYTHON executes the function.
"""
import json
import os
from dotenv import load_dotenv
from openai import OpenAI

def get_account_status(customer_id: str):
    print(f"TOOL EXECUTED: get_account_status({customer_id})")
    return {"customer_id": customer_id, "status": "active", "plan": "enterprise", "api_enabled": True}

def main():
    load_dotenv()
    client = OpenAI()
    model = os.environ["OPENAI_MODEL"]
    tools = [{
        "type": "function",
        "name": "get_account_status",
        "description": "Look up whether a customer account is active and API-enabled.",
        "parameters": {
            "type": "object",
            "properties": {"customer_id": {"type": "string", "description": "Customer ID such as c123"}},
            "required": ["customer_id"],
            "additionalProperties": False,
        },
    }]
    input_items = [{"role": "user", "content": "Customer c123 says their API stopped working. Check whether their account is active, then explain what you found."}]
    for _ in range(4):
        response = client.responses.create(model=model, input=input_items, tools=tools)
        if response.status != "completed":
            raise RuntimeError(f"Incomplete response: {response.status}")
        input_items += response.output
        calls = [item for item in response.output if item.type == "function_call"]
        if not calls:
            print(response.output_text)
            return
        for item in calls:
            if item.name != "get_account_status":
                raise ValueError(f"Unexpected tool requested: {item.name}")
            arguments = json.loads(item.arguments)
            if not isinstance(arguments, dict) or set(arguments) != {"customer_id"}:
                raise ValueError("Expected only customer_id")
            if arguments["customer_id"] != "c123":
                raise ValueError("Only synthetic account c123 is available")
            result = get_account_status(arguments["customer_id"])
            input_items.append({"type": "function_call_output", "call_id": item.call_id,
                                "output": json.dumps(result)})
    raise RuntimeError("Tool round limit reached")

if __name__ == "__main__":
    main()
