"""Lab 16 — Practice the API boundary WITHOUT credits."""
def fake_call_openai(prompt, model="fake-model"):
    print("FAKE NETWORK WRAPPER")
    print("Model:", model)
    print("Prompt:", prompt)
    return {"summary": "High error rate dominated by HTTP 429.", "recommended_action": "Check account rate limits and recent traffic change."}

def build_prompt(metrics):
    return "Analyze these deterministic API metrics and give support recommendations:\n" + str(metrics)

def main():
    metrics = {"total_requests": 100, "error_rate": 0.22, "p95_latency": 4.7}
    result = fake_call_openai(build_prompt(metrics))
    print("\nRESULT:", result)

if __name__ == "__main__":
    main()
