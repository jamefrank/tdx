# -*- encoding: utf-8 -*-
'''
@File    :   datafeed.py
@Time    :   2023/11/07 23:40:35
@Author  :   frank 
@Version :   1.0
@Contact :   
@License :   
@Desc    :   通过第三方服务获取历史数据
'''
from pytdx.hq import TdxHq_API
from datetime import datetime


api = TdxHq_API()
with api.connect('119.147.212.81', 7709):
    data = api.to_df(api.get_security_bars(7, 0, '000001', 0, 10))
    print(data)
    print(data.columns)
    print(data['datetime'][0])
    print(type(data['datetime'][0]))
    for itime in data['datetime']:
        time_obj = datetime.strptime(itime, '%Y-%m-%d %H:%M')
        seconds = (time_obj - datetime.utcfromtimestamp(0)).total_seconds()
        print(seconds)
