import importlib.util
from pathlib import Path
import unittest

spec=importlib.util.spec_from_file_location('analyzer',Path(__file__).resolve().parents[1]/'labs/06_full_offline_analyzer.py')
analyzer=importlib.util.module_from_spec(spec)
spec.loader.exec_module(analyzer)

class AnalyzerTests(unittest.TestCase):
    def test_invalid_shapes_and_statuses(self):
        rows,errors=analyzer.normalize_records([[],None,{'status':True},{'status':'200.5'},{'status':700}])
        self.assertEqual(rows,[])
        self.assertEqual(len(errors),5)

    def test_numeric_strings_and_optional_missing_latency(self):
        rows,errors=analyzer.normalize_records([{'status':'429','latency':'2.5'},{'status':200,'latency':'NaN'}])
        self.assertEqual(errors,[])
        result=analyzer.calculate_metrics(rows)
        self.assertEqual(result['error_rate'],0.5)
        self.assertEqual(result['latency_samples'],1)
        self.assertEqual(result['p95_latency'],2.5)

    def test_empty_and_bad_percentile(self):
        self.assertIsNone(analyzer.calculate_metrics([])['error_rate'])
        with self.assertRaises(ValueError): analyzer.nearest_rank_percentile([1],101)

    def test_invalid_latencies(self):
        for value in [True,-1,'NaN','Infinity','banana']:
            self.assertIsNone(analyzer.safe_float(value))

if __name__=='__main__': unittest.main()
