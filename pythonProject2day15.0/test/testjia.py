import unittest
from jiafa import Calc
from ddt import ddt
from ddt import data
from ddt import unpack
data1 = [
    [1,2,3],
    [2,3,5]
]
@ddt
class TestCalcAdd(unittest.TestCase):
    @data(*data1)
    @unpack
    def testAdd(self,s,t,y):
        a = s
        b = t
        p = y
        calc = Calc()

        sum = calc.add(a,b)
        self.assertEqual(p,sum)