# -*- coding: utf-8 -*- 
# @Time : 2022/4/15 0:19 
# @Author : wangbo

import os
import openpyxl
import json
import time
import unittest
from common.api import RunMethod
from parameterized import parameterized
from utils.logutil import logger
from utils.util import parse_xls, insert_result, pasre_relation, DirPath, read_config, parse_yaml

run_method = RunMethod()
dir_path = DirPath()
config_path = dir_path.get_config_path()
report_path = dir_path.get_report_path()

yaml_path = os.path.join(dir_path.get_data_path(), 'test_data.yaml')

test_data = parse_yaml(yaml_path, 'test01')

current_time = time.strftime('%Y_%m_%d')


class TestAllCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logger.info(f"***** 开始执行测试用例，开始时间为：{time.strftime('%Y-%m-%d %H:%M:%S')} *****")
        cls.url = read_config(config_path, 'Host', 'URL')

    @classmethod
    def tearDown(self):
        # wb.save(os.path.join(report_path, f'result_{current_time}.xlsx'))
        # wb.close()
        logger.info(f"***** 开始执行测试用例，开始时间为：{time.strftime('%Y-%m-%d %H:%M:%S')} *****")

    @parameterized.expand(test_data)
    def test_all_case(self, desc, method, path, headers, data, text, expected):
        url = self.url + path

        # 打印日志
        logger.info("正在执行{}用例".format(desc))
        # 执行测试用例，发送http请求
        res = run_method.run_main(method, url, headers, data)
        print(res.text)
        # print(type(data))

        # 打印日志
        logger.info("用例执行成功，请求的结果为{}".format(res.text))

        actual = run_method.get_text(res.text, text)

        is_pass = False
        # 异常处理，捕获assert抛出的异常，不直接抛出
        try:
            # 根据结果进行断言验证
            assert expected == actual
            # 打印信息
            logger.info(f"用例断言成功,预期值：{expected},实际值：{actual}")

            # 设置变量为True
            is_pass = True
        # 捕获异常
        except:
            # 设置变量为False
            is_pass = False
            # 打印日志
            logger.info(f"用例断言失败,预期值：{expected},实际值：{actual}")


        # 无论是否出现异常，都执行下面内容代码
        finally:

            # 根据变量结果是True/False，进行断言验证，成功则通过，失败则未通过
            assert is_pass
        # 返回该变量结果
        return is_pass
