"""Original HHFinAi domain arithmetic tests; all numbers are synthetic."""
import copy, math, random, unittest
from sf_agent.analytics import *
from sf_agent.validation import DataError

class Mandate(unittest.TestCase):
    def test_unknown_not_pass(self):self.assertEqual(mandate_bounds(.55,.2,.25,.7)['result'],'UNKNOWN')
    def test_lower_guarantees_arithmetic_threshold(self):self.assertEqual(mandate_bounds(.8,.1,.1,.7)['result'],'MET_ARITHMETICALLY')
    def test_upper_fails(self):self.assertEqual(mandate_bounds(.3,.5,.2,.7)['result'],'NOT_MET')
    def test_no_legal_certification(self):self.assertIs(mandate_bounds(1,0,0,.7)['legal_certification'],False)
    def test_bad_sum(self):
        with self.assertRaises(DataError):mandate_bounds(.55,.2,.4,.7)
    def test_negative_weight(self):
        with self.assertRaises(DataError):mandate_bounds(-.1,.5,.6,.7)
    def rule(self,id,r):return {'id':id,'result':r,'basis':'Synthetic test rationale','source_ref':'test://rule'}
    def test_fail_dominates_unknown(self):self.assertEqual(combine_mandatory_rules([self.rule('a','UNKNOWN'),self.rule('b','FAIL')])['result'],'FAIL')
    def test_all_pass_declarations(self):self.assertEqual(combine_mandatory_rules([self.rule('a','PASS')])['result'],'PASS_DECLARED_TESTS')
    def test_unknown_gate(self):self.assertEqual(combine_mandatory_rules([self.rule('a','UNKNOWN')])['result'],'UNKNOWN')
    def test_inapplicability_needs_reason(self):
        with self.assertRaises(DataError):combine_mandatory_rules([self.rule('a','NOT_APPLICABLE')])
    def test_post_trade(self):self.assertAlmostEqual(post_trade_fraction(100,50,10,20,0)['fraction'],.6)
    def test_post_trade_overallocation(self):
        with self.assertRaises(DataError):post_trade_fraction(100,50,10,70,0)
    def test_post_flow_denominator(self):self.assertAlmostEqual(post_trade_fraction(100,50,0,10,20)['fraction'],.5)

if __name__=='__main__':unittest.main()
