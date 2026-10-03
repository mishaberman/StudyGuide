"""Lab 00 — Environment check. Runs WITHOUT API credits."""
import os
import sys
from dotenv import load_dotenv

print("Python executable:", sys.executable)
print("Python version:", sys.version.split()[0])

load_dotenv()
print("OPENAI_API_KEY:", "loaded (secret not displayed)" if os.getenv("OPENAI_API_KEY") else "not loaded")

try:
    from openai import OpenAI  # noqa: F401
    print("openai package: import OK")
except Exception as exc:
    print("openai package: IMPORT FAILED", type(exc).__name__, exc)

try:
    from agents import Agent, Runner  # noqa: F401
    print("openai-agents package: import OK")
except Exception as exc:
    print("openai-agents package: IMPORT FAILED", type(exc).__name__, exc)
