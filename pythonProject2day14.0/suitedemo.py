import unittest
from HTMLTestRunner import HTMLTestRunner
from testcase.testyinhan import TestBank
suite = unittest.TestSuite()

suite.addTest(TestBank("testSaveMoney"))

f = open("a.html","w+",encoding="utf-8")

runner = HTMLTestRunner.HTMLTestRunner(
    stream=f,
    title="银行测试",
    verbosity=1,
    description="这是银行测试"
)

runner.run(suite)