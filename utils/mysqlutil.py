# -*- coding: utf-8 -*- 
# @Time : 2022/4/17 16:58 
# @Author : wangbo

import pymysql
from tqdm import tqdm
from faker import Faker
import time


DB_CONFIG = {"host": "127.0.0.1",
             "user": "root",
             "password": "root",
             "database": "test",
             "port": 3306,
             "charset": "utf8"}


faker = Faker('zh_CN')
ad_name = faker.name()
db = pymysql.connect(**DB_CONFIG)
cursor = db.cursor()

data_list = []

sql  = '''SELECT pid,ad_name FROM `tpshop3.0`.`test`'''

cursor.execute(sql)
data = cursor.fetchall()
# print(list(data))
# print(data_list.append(data))
#
# data_list = []
# for i in range(1,100000):
#
#     idList = i
#     ad_name = faker.name()
#     data_list.append((idList,ad_name))
#

# sql = '''INSERT INTO `tpshop3.0`.`test`( `pid`, `media_type`, `ad_name`, `ad_link`, `ad_code`, `start_time`, `end_time`, `link_man`, `link_email`, `link_phone`, `click_count`, `enabled`, `orderby`, `target`, `bgcolor`)
#          VALUES ( %s, 0, %s, 'http://www.tp-shop.cn', '/public/upload/ad/2017/05-20/5b3261f64a247198d8c23a2d4bf3f8b7.jpg', 1451577600, 1864656000, '', '', '', 0, 1, 50, 1, NULL);'''

sql = '''INSERT INTO `tpshop3.0`.`test1`(`pid`,`ad_name`) values (%s,%s)'''

statr_time = time.time()
try:
    # db对象和指针对象同时存在
    if db and cursor:

        # 执行sql
        cursor.executemany(sql, data)

        # 提交执行sql到数据库，完成insert或者update相关命令操作，非查询时使用
        db.commit()

except Exception as e:
    # 出现异常时，数据库回滚
    db.rollback()

end_time = time.time()
print(end_time-statr_time)

cursor.close()
db.close()