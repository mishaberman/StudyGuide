"""Lab 05 — Pure deterministic metrics. Runs offline."""
import math

def nearest_rank_percentile(values, percentile):
    if not values:
        return None
    ordered = sorted(values)
    rank = math.ceil((percentile / 100) * len(ordered))
    return ordered[max(rank - 1, 0)]

def calculate_metrics(records):
    total = len(records)
    failures = sum(1 for r in records if r["status"] >= 400)
    latencies = [r["latency"] for r in records if r.get("latency") is not None]
    return {
        "total": total,
        "failures": failures,
        "error_rate": failures / total if total else 0.0,
        "average_latency": sum(latencies) / len(latencies) if latencies else None,
        "p95_latency": nearest_rank_percentile(latencies, 95),
    }

sample = [
    {"status": 200, "latency": 1.0},
    {"status": 500, "latency": 4.0},
    {"status": 200, "latency": 2.0},
]
print(calculate_metrics(sample))
print(calculate_metrics([]))
