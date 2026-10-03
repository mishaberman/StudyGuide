"""Lab 17 — Tiny deterministic tests. Runs offline."""
import math

def safe_float(value):
    if value is None or value == "":
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None

def nearest_rank_percentile(values, p):
    if not values:
        return None
    ordered = sorted(values)
    rank = math.ceil((p / 100) * len(ordered))
    return ordered[max(rank - 1, 0)]

assert safe_float("2.5") == 2.5
assert safe_float("") is None
assert safe_float(None) is None
assert safe_float("banana") is None
assert nearest_rank_percentile([], 95) is None
assert nearest_rank_percentile([1, 2, 3, 4, 5], 95) == 5
print("All tests passed.")
