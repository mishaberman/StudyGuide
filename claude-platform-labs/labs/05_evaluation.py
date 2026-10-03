"""Compare two deliberately simple offline baselines, or evaluate Claude live."""
import importlib
import json
from labs.common import ROOT, arguments, connection

def baseline(text, version):
    text = text.lower()
    if '401' in text or (version == 2 and 'invalid api key' in text):
        return 'authentication'
    if '429' in text or (version == 2 and 'too many requests' in text):
        return 'rate_limit'
    return 'other'

def evaluate(predict, cases):
    rows = []
    for case in cases:
        try:
            prediction = predict(case['text'])
            rows.append({'id': case['id'], 'expected': case['expected'], 'actual': prediction,
                         'passed': prediction == case['expected']})
        except Exception as exc:
            rows.append({'id': case['id'], 'passed': False, 'error_type': type(exc).__name__})
    return {'total': len(rows), 'passed': sum(r['passed'] for r in rows),
            'accuracy': sum(r['passed'] for r in rows)/len(rows) if rows else None, 'rows': rows}

if __name__ == '__main__':
    cases = json.loads((ROOT/'fixtures/eval_cases.json').read_text())
    if arguments(__doc__).live:
        client, model = connection()
        classify = importlib.import_module('labs.03_structured').classify
        print(json.dumps(evaluate(lambda t: classify(client, model, t).category, cases), indent=2))
    else:
        for version in (1, 2):
            print('OFFLINE KEYWORD BASELINE', version)
            print(json.dumps(evaluate(lambda t: baseline(t, version), cases), indent=2))
