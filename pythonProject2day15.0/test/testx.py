import unittest
from jiafa import Calc
from ddt import ddt
from ddt import data
from ddt import unpack


data3 = [
    [1,2,2],
    [2,3,6]
]
@ddt
class TestCalcAbb(unittest.TestCase):
    @data(*data3)
    @unpack
    def testAbb(self,n,k,j):
        e = n
        f = k
        m = j
        calc = Calc()

        sum = calc.abb(e,f)
        self.assertEqual(m,sum)
