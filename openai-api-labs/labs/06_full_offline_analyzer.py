"""
Lab 06 — Full offline analyzer. Highest-value offline practice.
Run:
python 06_full_offline_analyzer.py ../fixtures/requests_messy.jsonl
"""
import argparse
import json
import math
import time

def parse_args():
    parser = argparse.ArgumentParser(description="Analyze API request logs.")
    parser.add_argument("file")
    return parser.parse_args()

def load_jsonl(path):
    records, failures = [], []
    with open(path, "r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as exc:
                failures.append({"line": line_number, "stage": "parse", "error": str(exc)})
    return records, failures

def safe_int(value):
    if value is None or value == "":
        return None
    try:
        result = int(str(value))
        return result if 100 <= result <= 599 else None
    except (TypeError, ValueError, OverflowError):
        return None

def safe_float(value):
    if value is None or value == "":
        return None
    try:
        result = float(value)
        return result if not isinstance(value, bool) and math.isfinite(result) and result >= 0 else None
    except (TypeError, ValueError, OverflowError):
        return None

def normalize_records(records):
    normalized, failures = [], []
    for index, record in enumerate(records):
        if not isinstance(record, dict):
            failures.append({"record_index": index, "stage": "normalize", "error": "Expected an object"})
            continue
        status = safe_int(record.get("status"))
        latency = safe_float(record.get("latency"))
        if status is None:
            failures.append({"record_index": index, "stage": "normalize", "error": "Missing or invalid status"})
            continue
        normalized.append({"customer_id": record.get("customer_id"), "status": status, "latency": latency})
    return normalized, failures

def nearest_rank_percentile(values, percentile):
    if not 0 < percentile <= 100:
        raise ValueError("percentile must be between 0 (exclusive) and 100")
    if not values:
        return None
    ordered = sorted(values)
    rank = math.ceil((percentile / 100) * len(ordered))
    return ordered[max(rank - 1, 0)]

def calculate_metrics(records):
    total = len(records)
    failures = sum(1 for r in records if r["status"] >= 400)
    latencies = [r["latency"] for r in records if r["latency"] is not None]
    return {
        "total_requests": total,
        "failed_requests": failures,
        "error_rate": failures / total if total else None,
        "average_latency": sum(latencies) / len(latencies) if latencies else None,
        "p95_latency": nearest_rank_percentile(latencies, 95),
        "latency_samples": len(latencies),
    }

def main():
    start = time.perf_counter()
    args = parse_args()
    raw_records, parse_failures = load_jsonl(args.file)
    records, normalize_failures = normalize_records(raw_records)
    metrics = calculate_metrics(records)
    output = {
        "metrics": metrics,
        "failures": parse_failures + normalize_failures,
        "elapsed_seconds": time.perf_counter() - start,
    }
    print(json.dumps(output, indent=2))

if __name__ == "__main__":
    main()
