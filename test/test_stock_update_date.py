# -*- encoding: utf-8 -*-
# @File    :   datafeed_stock_update_date.py
# @Time    :   2023/11/15 16:44:48
# @Author  :   frank
# @Email:
# @Description: (临时使用，更新数据的最新更新日期)
# 最终是使用的是建立索引和聚合查询的方式，并没有添加新的字段来进行快速查询

from http import client
from tdx_tools.db.mongo.mongo_client import MongoClient
from tdx_tools.globals import mesure_time


@mesure_time
def get_update_time_patch():
    client = MongoClient()
    results = client.find_bar_update_time_patch()
    # res = list(results)
    # for doc in results:
    #     print(doc["code"], ":", doc["adjust"], doc["maxStamp"])


if __name__ == '__main__':
    get_update_time_patch()
    print("finish")
