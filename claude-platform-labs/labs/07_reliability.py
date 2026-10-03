"""An offline retry decision exercise. No sleep, no HTTP calls."""
import random

def retry_delay(status, attempt, retry_after=None, random_value=None):
    if attempt < 0:
        raise ValueError('attempt must be nonnegative')
    if status not in {408, 409, 429, 500, 502, 503, 504, 529} or attempt >= 3:
        return None
    if retry_after is not None:
        # Numeric seconds only in this teaching example; a real header can also be a date.
        return max(0.0, float(retry_after))
    jitter = random.random() if random_value is None else random_value
    return min(8.0, 2**attempt) * jitter

if __name__ == '__main__':
    for status in (401, 403, 429, 500, 529):
        print(status, [retry_delay(status, i, random_value=0.5) for i in range(4)])
    print('None = stop. The API SDK already retries; avoid adding a second retry layer blindly.')
    print('Retries of side-effecting tools require idempotency or reconciliation.')
