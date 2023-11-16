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
'''

import datetime
from pydoc import describe
import requests
import json
import re
from typing import Dict, List

from tqdm import tqdm
from tdx_tools.globals import singleton_instance
from tdx_tools.protos.xrxd_pb2 import XRXD
from tdx_tools.db.mongo.mongo_client import MongoClient


def get_xrxd_one_page(pageNumber: int, date: str) -> Dict:
    url = f"https://datacenter-web.eastmoney.com/api/data/v1/get?callback=jQuery1123026590177773483425_1700058214545&sortColumns=EX_DIVIDEND_DATE%2CSECURITY_CODE&sortTypes=-1%2C-1&pageSize=50&pageNumber={pageNumber}&reportName=RPT_SHAREBONUS_DET&columns=ALL&quoteColumns=&js=%7B%22data%22%3A(x)%2C%22pages%22%3A(tp)%7D&source=WEB&client=WEB&filter=(REPORT_DATE%3D%27{date}%27)(EX_DIVIDEND_DAYS%3E%3D0)"

    r = requests.get(url)
    response_str = r.content.decode('utf-8')
    match = re.search(r'\((.*?)\)\;', response_str)
    response_str = match.group(1)
    response_dict = json.loads(response_str)
    return response_dict


def data_analysis(data: Dict) -> List[XRXD]:
    xrxds = []
    for item in data:
        xrxd = XRXD()
        xrxd.code = item['SECURITY_CODE']
        xrxd.name = item['SECURITY_NAME_ABBR']
        if 'SH' in item['SECUCODE']:
            xrxd.market = 'sh'
        elif 'SZ' in item['SECUCODE']:  # TODO
            xrxd.market = 'sz'
        datetime_obj = datetime.datetime.strptime(item['EX_DIVIDEND_DATE'], '%Y-%m-%d %H:%M:%S')
        # print(datetime_obj.timestamp())
        xrxd.date_ts = datetime_obj.timestamp()
        xrxds.append(xrxd)
    return xrxds


def get_xrxd():
    current_time = datetime.datetime.now()
    year = current_time.year
    print(year)
    xrxds = []
    for date in tqdm(singleton_instance.XRXD_DATE_LIST, desc="downloading xrxds..."):
        date = str(year)+"-"+date
        pageNumber = 1
        result = get_xrxd_one_page(pageNumber, date)
        if result['success']:
            pages = result['result']['pages']
            # count = result['result']['count']
            for i in range(pages):
                result = get_xrxd_one_page(i+1, date)  # TODO  need opt
                if result['success']:
                    # print(i+1)
                    # print(result['result']['count'])
                    xrxds.extend(data_analysis(result['result']['data']))
    client = MongoClient()
    client.write_xrxds(xrxds)


if __name__ == '__main__':
    get_xrxd()
