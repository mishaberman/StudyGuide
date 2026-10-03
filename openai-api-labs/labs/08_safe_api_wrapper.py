from live_setup import require_live
require_live()

"""Lab 08 — Keep network calls in one wrapper. Requires API credits."""
import os
from dotenv import load_dotenv
from openai import OpenAI, AuthenticationError, RateLimitError, APIConnectionError, APIError

def create_client():
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is missing")
    return OpenAI()

def call_openai(client, prompt, model):
    response = client.responses.create(model=model, input=prompt)
    return response.output_text

def main():
    load_dotenv()
    model = os.environ["OPENAI_MODEL"]
    prompt = "Explain HTTP 401 vs 403 vs 429 for a support engineer."
    try:
        client = create_client()
        print(call_openai(client, prompt, model))
    except AuthenticationError as exc:
        print("Authentication error:", exc)
    except RateLimitError as exc:
        print("Rate/quota error:", exc)
    except APIConnectionError as exc:
        print("Connection error:", exc)
    except APIError as exc:
        print("OpenAI API error:", exc)

if __name__ == "__main__":
    main()
