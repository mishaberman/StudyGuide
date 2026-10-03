import argparse
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def arguments(description):
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--live', action='store_true', help='Make billable API calls')
    return parser.parse_args()


def connection():
    from dotenv import load_dotenv
    from anthropic import Anthropic
    load_dotenv(ROOT / '.env')
    model = os.getenv('ANTHROPIC_MODEL')
    if not os.getenv('ANTHROPIC_API_KEY') or not model:
        raise SystemExit('Set ANTHROPIC_API_KEY and ANTHROPIC_MODEL in .env; see README.')
    return Anthropic(timeout=30.0, max_retries=2), model


def text_of(message):
    return ''.join(b.text for b in message.content if b.type == 'text')


def require_complete(message):
    if message.stop_reason != 'end_turn':
        raise RuntimeError(f'Incomplete or nonstandard response: {message.stop_reason}')
