import unittest
from jiafa import Calc
from ddt import ddt
from ddt import data
from ddt import unpack


data2 = [
    [3,1,2],
    [3,3,0]
]
@ddt
class TestCalcAcc(unittest.TestCase):
    @data(*data2)
    @unpack
    def testAcc(self,q,w,l):
        c = q
        d = w
        o = l
        calc = Calc()

        sum = calc.acc(c,d)
        self.assertEqual(o,sum)
