"""Hardened adaptation of an earlier personal API-log practice exercise."""
import json
import math
from labs.common import ROOT

def analyze(lines):
    valid, errors = [], []
    for number, line in enumerate(lines, 1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
            if not isinstance(row, dict):
                raise ValueError('Expected an object')
            raw_status = row.get('status')
            if isinstance(raw_status, bool):
                raise ValueError('Boolean status')
            status = int(str(raw_status))
            if not 100 <= status <= 599:
                raise ValueError('Status outside HTTP range')
            latency = None
            raw = row.get('latency_ms')
            if raw is not None and raw != '':
                if isinstance(raw, bool):
                    raise ValueError('Boolean latency')
                latency = float(raw)
                if not math.isfinite(latency) or latency < 0:
                    raise ValueError('Latency must be finite and nonnegative')
            valid.append((status, latency))
        except (ValueError, TypeError, OverflowError) as exc:
            errors.append({'line': number, 'reason': str(exc)})
    latencies = sorted(v for _,v in valid if v is not None)
    return {'valid': len(valid), 'rejected': errors,
            'error_rate': sum(s>=400 for s,_ in valid)/len(valid) if valid else None,
            'latency_samples': len(latencies),
            'p95_ms': latencies[math.ceil(.95*len(latencies))-1] if latencies else None}

if __name__ == '__main__':
    print(json.dumps(analyze((ROOT/'fixtures/requests.jsonl').read_text().splitlines()), indent=2))
