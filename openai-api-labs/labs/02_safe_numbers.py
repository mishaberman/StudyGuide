"""Lab 02 — Defensive numeric conversion. Runs offline."""
def safe_float(value):
    if value is None or value == "":
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None

samples = [2.4, "2.4", "", None, "banana", 0, "0"]
for sample in samples:
    print(f"input={sample!r:>10} -> output={safe_float(sample)!r}")
