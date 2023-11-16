# -*- encoding: utf-8 -*-
'''
@File    :   datafeed_fhpg.py
@Time    :   2023/11/15 22:41:29
@Author  :   frank 
@Version :   1.0
@Contact :   
@License :   
@Desc    :   分红配股信息查询
refrence: https://data.eastmoney.com/yjfp/
0930 0630 0331 1231
'''

import requests
import json
import re


def get_fhpg():
    url = "https://datacenter-web.eastmoney.com/api/data/v1/get?callback=jQuery1123026590177773483425_1700058214545&sortColumns=EX_DIVIDEND_DATE%2CSECURITY_CODE&sortTypes=-1%2C-1&pageSize=50&pageNumber=2&reportName=RPT_SHAREBONUS_DET&columns=ALL&quoteColumns=&js=%7B%22data%22%3A(x)%2C%22pages%22%3A(tp)%7D&source=WEB&client=WEB&filter=(REPORT_DATE%3D%272023-06-30%27)(EX_DIVIDEND_DAYS%3E%3D0)"
    r = requests.get(url)
    print(r.status_code)
    # print(r.content)
    response_str = r.content.decode('utf-8')  # 将字节字符串解码为字符串
    match = re.search(r'\((.*?)\)\;', response_str)
    response_str = match.group(1)
    # print(response_str)
    response_dict = json.loads(response_str)  # 将字符串解析为字典
    print(response_dict)


if __name__ == '__main__':
    get_fhpg()
