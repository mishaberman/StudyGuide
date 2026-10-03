"""
Lab 18 — Debug me. Runs offline.

This file is intentionally runtime-fragile but syntactically valid.
Before fixing, identify the exact input that breaks each helper.
"""

def average_latency(records):
    # BUG 1: assumes every record has latency.
    values = [float(record["latency"]) for record in records]
    # BUG 2: empty list can divide by zero.
    return sum(values) / len(values)


def failure_rate(records):
    # BUG 3: status may be a numeric string, causing comparison TypeError.
    failures = sum(1 for record in records if record["status"] >= 400)
    return failures / len(records)


cases = [
    [],
    [{"status": 200}],
    [{"status": "500", "latency": "2.0"}],
    [{"status": 200, "latency": "banana"}],
]

for i, records in enumerate(cases, start=1):
    print(f"\nCASE {i}: {records}")
    try:
        print("average_latency:", average_latency(records))
    except Exception as exc:
        print("average_latency ERROR:", type(exc).__name__, exc)
    try:
        print("failure_rate:", failure_rate(records))
    except Exception as exc:
        print("failure_rate ERROR:", type(exc).__name__, exc)
