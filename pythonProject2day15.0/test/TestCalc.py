import unittest
from jiafa import Calc
from ddt import ddt
from ddt import data
from ddt import unpack




data4 = [
    [4,2,2],
    [6,3,2]
]
@ddt
class TestCalcAee(unittest.TestCase):
    @data(*data4)
    @unpack
    def testAee(self,z,zz,zzz):
        g = z
        h = zz
        r = zzz
        calc = Calc()

        sum = calc.aee(g,h)
        self.assertEqual(r,sum)
