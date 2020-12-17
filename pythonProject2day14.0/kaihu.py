import unittest
from HTMLTestRunner import HTMLTestRunner
from testcase.testkauh import TestBank
suite = unittest.TestSuite()
# suite.addTest(TestBank("testSaveUser"))
loader =unittest.defaultTestLoader
cases  = loader.discover("E:\\pythonProject1\\pythonProject2day14.0\\testcase",pattern="test*.py")
suite.addTest(cases)
f = open("hh.html","w+",encoding="utf-8")
runer = HTMLTestRunner.HTMLTestRunner(
    stream=f,
    title="银行测试",
    verbosity=1,
    description="这是银行测试"
)
runer.run(suite)