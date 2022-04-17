# -*- coding: utf-8 -*- 
# @Time : 2022/4/15 0:59 
# @Author : wangbo
import json

import jsonpath

import requests


url = 'http://ihrm-test.itheima.net/api/employees/undefined/positive'
headers = {"Content-Type":"application/json","Authorization":"Bearer 0e5b03c8-ae58-45c9-a67b-b6be4d9d87f8"}
data = '''{"userId":"1071632760222810112","dateOfCorrection":null,"correctionEvaluation":null,"enclosure":null,"estatus":1,"createTime":"2022-04-16T02:15:54.000+0000"}'''
res = requests.put(url=url,headers=headers,data=data).text
print(res)