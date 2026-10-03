"""
Lab 03 — argparse. Runs offline.
Try:
python 03_argparse_demo.py "Explain HTTP 429"
python 03_argparse_demo.py "Explain HTTP 429" --model your-model-id --tag urgent --tag api
"""
import argparse
import json

def parse_args():
    parser = argparse.ArgumentParser(description="Demo CLI for support analysis.")
    parser.add_argument("prompt", help="Support prompt/question.")
    parser.add_argument("--model", default="your-model-id", help="Model ID.")
    parser.add_argument("--tag", action="append", default=[], help="Repeatable tag.")
    return parser.parse_args()

def main():
    args = parse_args()
    output = {"prompt": args.prompt, "model": args.model, "tags": args.tag}
    print(json.dumps(output, indent=2))

if __name__ == "__main__":
    main()
