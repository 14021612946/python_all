import unittest
from  testdemo.calc import Calc
from ddt import ddt
from ddt import data
from ddt import unpack
data1 = [
    [1,2,3],
    [9,-1,8],
    [-9,8,-1],
    [0,4,4],
    [1000,1000,2000]
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






