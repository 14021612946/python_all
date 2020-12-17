import unittest
from cal import Calc

class TestCalcl(unittest.TestCase):
    def testSubs(self):
        a = 1
        b = 2
        sum = -1
        c = Calc()
        s = c.subs(a,b)
        self.assertEqual(sum,s)