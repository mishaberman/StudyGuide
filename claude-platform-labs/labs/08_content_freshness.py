"""Detect changes to a checked-in API contract snapshot for curriculum maintenance."""
import hashlib
import json
from labs.common import ROOT

def digest(content):
    return hashlib.sha256(json.dumps(content, sort_keys=True).encode()).hexdigest()

def compare(before, after):
    changed = [key for key in sorted(set(before)|set(after)) if before.get(key) != after.get(key)]
    return {'changed': changed, 'needs_human_review': bool(changed),
            'before_sha256': digest(before), 'after_sha256': digest(after)}

if __name__ == '__main__':
    before = json.loads((ROOT/'fixtures/contract_before.json').read_text())
    after = json.loads((ROOT/'fixtures/contract_after.json').read_text())
    print(json.dumps(compare(before, after), indent=2))
    print('SYNTHETIC SNAPSHOTS: no live documentation monitoring occurred.')
