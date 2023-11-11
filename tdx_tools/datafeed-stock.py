# -*- encoding: utf-8 -*-
# @File    :   datafeed-stock.py
# @Time    :   2023/11/11 10:21:54
# @Author  :   frank
# @Email:
# @Description: 从第三方库获取股票列表的信息，并更新到数据库

import akshare as ak
import datetime

from tdx_tools.protos.stock_pb2 import Stock
from tdx_tools.db.mongo.mongo_client import MongoClient


def get_stock_list():
    """获取股票列表
    """
    stocks = []
    # sh
    stock_list = ak.stock_info_sh_name_code()
    columns = stock_list.columns
    code_str = '证券代码'
    name_str = '证券简称'
    full_name_str = '公司全称'
    birth_date_str = '上市日期'
    if code_str not in columns or name_str not in columns or full_name_str not in columns or birth_date_str not in columns:
        raise ValueError("key not in stock data[sh].")

    for index, row in stock_list.iterrows():
        stock = Stock()
        stock.code = row[code_str]
        stock.name = row[name_str]
        stock.full_name = row[full_name_str]
        stock.birth_date = row[birth_date_str].strftime("%Y-%m-%d") if datetime.date == type(row[birth_date_str]) else row[birth_date_str]
        stock.market = 'sh'
        stocks.append(stock)

    # sz
    code_str = 'A股代码'
    name_str = 'A股简称'
    birth_date_str = 'A股上市日期'

    stock_list = ak.stock_info_sz_name_code()
    columns = stock_list.columns
    if code_str not in columns or name_str not in columns or birth_date_str not in columns:
        raise ValueError("key not in stock data[sz].")
    for index, row in stock_list.iterrows():
        stock = Stock()
        stock.code = row[code_str]
        stock.name = row[name_str]
        stock.birth_date = row[birth_date_str]
        stock.market = 'sz'
        stocks.append(stock)

    client = MongoClient()
    client.write_stocks(stocks)
    print("finish")


if __name__ == '__main__':
    get_stock_list()
