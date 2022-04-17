# -*- coding: utf-8 -*- 
# @Time : 2022/4/15 0:19 
# @Author : wangbo

import os
from random import random

import openpyxl
import json
import time
import unittest
from common.api import RunMethod
from parameterized import parameterized
from utils.logutil import logger
from utils.util import parse_xls, insert_result, pasre_relation, DirPath, read_config
import random

run_method = RunMethod()
dir_path = DirPath()
config_path = dir_path.get_config_path()
report_path = dir_path.get_report_path()

xls_name = os.path.join(dir_path.get_data_path(), 'test_data.xlsx')
sheet_name = 'test'
wb = openpyxl.load_workbook(xls_name)
ws = wb[sheet_name]
test_data = parse_xls(xls_name, sheet_name)

current_time = time.strftime('%Y_%m_%d')


class TestAllCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logger.info(f"***** 开始执行测试用例，开始时间为：{time.strftime('%Y-%m-%d %H:%M:%S')} *****")
        cls.url = read_config(config_path, 'Host', 'URL')
        cls.uid =None

    @classmethod
    def tearDown(self):
        wb.save(os.path.join(report_path, f'result_{current_time}.xlsx'))
        wb.close()
        logger.info(f"***** 结束执行测试用例，开始时间为：{time.strftime('%Y-%m-%d %H:%M:%S')} *****")

    @parameterized.expand(test_data)
    def test_01(self, id, desc, method, path, headers, data, text, expected):
        url = self.url + path

        if '${id}' in data:
            replace_data = {"id":self.uid}
            data = pasre_relation(data,replace_data)

        # 打印日志
        logger.info("正在执行{}用例".format(desc))
        # 执行测试用例，发送http请求
        res = run_method.run_main(method, url, headers, data)
        print(res.text)
        # 打印日志
        logger.info("用例执行成功，请求的结果为{}".format(res.text))

        actual = run_method.get_text(res.text, text)
        #
        run_method.assert_response(ws, id, data, res, expected, actual)

        uid = run_method.get_text(res.text,'id')

        if uid:
            TestAllCase.uid = uid
