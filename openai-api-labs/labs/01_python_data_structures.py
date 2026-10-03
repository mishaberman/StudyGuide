"""Lab 01 — Dictionaries, lists and optional fields. Runs offline."""
record = {"customer_id": "c123", "status": 429, "latency": "2.4"}

print("Whole record:", record)
print("Required field:", record["status"])
print("Existing optional:", record.get("latency"))
print("Missing optional:", record.get("message"))
print("Missing with default:", record.get("message", "No message"))

# Uncomment to intentionally trigger KeyError:
# print(record["message"])

latencies = [1.2, 2.4, 0.8]
latencies.append(3.1)
for index, latency in enumerate(latencies, start=1):
    print(f"Latency #{index}: {latency}")
