import unittest

import time

from HTMLTestRunner_PY3 import HTMLTestRunner
from app import BASE_DIR
from script.emp_params import TestEmployeeParams
from script.login_params import TestLoginParams

suite = unittest.TestSuite()
# 将测试用例添加到测试套件
suite.addTest(unittest.makeSuite(TestLoginParams))
suite.addTest(unittest.makeSuite(TestEmployeeParams))
# filename = BASE_DIR + "/report/report{}.html".format(time.strftime("%Y%m%d %H%M%S"))

filename = BASE_DIR + "/report/ihrm.html"

with open(filename,mode='wb') as f :
    runner = HTMLTestRunner(f, verbosity=2, title="IHRM测试报告",description="IHRM测试报告生成")
    runner.run(suite)

