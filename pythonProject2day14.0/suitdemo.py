import unittest
from oridemo import TestCal
from subsdemo import TestCalcl
from HTMLTestRunner import  HTMLTestRunner
suite=unittest.TestSuite()

suite.addTest(TestCal("testAdd"))
suite.addTest(TestCal("testAdd1"))
suite.addTest(TestCalcl("testSubs"))

# runner=unittest.TextTestRunner()
f = open("计算器.html","w+",encoding="utf-8")
htmlrunner = HTMLTestRunner.HTMLTestRunner(
    stream=f,
    title="计算器的测试报告",
    description="这是一个计算器",
    verbosity=1,
)

htmlrunner.run(suite)