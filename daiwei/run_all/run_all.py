import os
import time
import unittest
import sys
from HTMLTestRunner_cn import HTMLTestRunner

path='E:\\python_project\\'
sys.path.append(path)

suite = unittest.TestSuite()  # 定义测试集合
all_case = unittest.defaultTestLoader.discover(
    r'E:\python_project\daiwei', 'test_*.py'
)  # 找到daiwei目录下所以的.py文件

for case in all_case:
    # 循环添加case到测试集合里面
    suite.addTests(case)

# 定义报告路径
now = time.strftime("%Y-%m-%d %H-%M-%S")
report_name = 'e:/python_project/daiwei/warehouse/reports/%s_report.html' % now
fw = open(report_name, 'wb')

runner = HTMLTestRunner(
    stream=fw, title='代维系统测试报告', verbosity=2, retry=1, save_last_try=True
)
runner.run(suite)
