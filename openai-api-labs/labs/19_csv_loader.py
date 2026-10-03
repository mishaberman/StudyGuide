"""
Lab 19 — CSV parsing + normalization. Runs offline.
Run:
python 19_csv_loader.py ../fixtures/requests.csv
"""
import argparse
import csv
import json


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    return parser.parse_args()


def safe_int(value):
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def safe_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def load_csv(path):
    with open(path, newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def normalize(records):
    output = []
    for record in records:
        output.append({
            "customer_id": record.get("customer_id"),
            "status": safe_int(record.get("status")),
            "latency": safe_float(record.get("latency")),
            "endpoint": record.get("endpoint"),
        })
    return output


def main():
    args = parse_args()
    raw = load_csv(args.file)
    print("RAW CSV VALUES (mostly strings):")
    print(json.dumps(raw[:2], indent=2))
    print("\nNORMALIZED:")
    print(json.dumps(normalize(raw)[:2], indent=2))


if __name__ == "__main__":
    main()
