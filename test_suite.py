# -*- coding: utf-8 -*- 
# @Time : 2022/4/15 1:57 
# @Author : wangbo

import unittest
from HTMLTestRunner import HTMLTestRunner

suite = unittest.TestLoader().discover('./test_case','test_*.py')

# 执行测试
with open(r'./report/report.html','wb') as f:
    runner = HTMLTestRunner(f)
    runner.run(suite)