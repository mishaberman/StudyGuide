"""Explicit opt-in for billable examples. No credential values are printed."""
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

def require_live():
    if '--live' not in sys.argv:
        raise SystemExit('Live example: add --live after configuring .env. API billing applies.')
    load_dotenv(Path(__file__).resolve().parents[1] / '.env')
    if not os.getenv('OPENAI_API_KEY') or not os.getenv('OPENAI_MODEL'):
        raise SystemExit('Set OPENAI_API_KEY and OPENAI_MODEL in .env. Values are not displayed.')
    # Keep teaching traces local by default; enable intentionally when learning tracing.
    os.environ.setdefault('OPENAI_AGENTS_DISABLE_TRACING', '1')
