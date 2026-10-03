"""Lab 04 — JSONL loader with per-line failure recording. Runs offline."""
import argparse
import json

def parse_args():
    parser = argparse.ArgumentParser()
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
                failures.append({"line": line_number, "error": str(exc)})
    return records, failures

def main():
    args = parse_args()
    records, failures = load_jsonl(args.file)
    print("Valid records:", len(records))
    print("Parsing failures:", len(failures))
    print(json.dumps(failures, indent=2))

if __name__ == "__main__":
    main()
