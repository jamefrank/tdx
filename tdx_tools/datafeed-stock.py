# -*- encoding: utf-8 -*-
# @File    :   datafeed-stock.py
# @Time    :   2023/11/11 10:21:54
# @Author  :   frank
# @Email:
# @Description: 从第三方库获取股票列表的信息，并更新到数据库

import akshare as ak
import tdx_tools.stock.list_pb2 as stock_list


def get_stock_list():
    """获取股票列表
    """
    stock_list = ak.stock_info_sh_name_code()
    print(stock_list)


if __name__ == '__main__':
    get_stock_list()
