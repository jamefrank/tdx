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
# from pytdx.config.hosts import hq_hosts
# from pytdx.hq import TdxHq_API
# from datetime import datetime
# from global_var import MarkeType, BarType

# print(len(hq_hosts))
# # print(hq_hosts[:10])

# api = TdxHq_API()

# ihost = 0
# while ihost < len(hq_hosts):
#     try:
#         bsuc = api.connect(str(hq_hosts[ihost][1]), hq_hosts[ihost][2])
#         if bsuc:
#             break
#         else:
#             ihost += 1
#             print(ihost)
#     except Exception as e:
#         ihost += 1
#         print(ihost)

# print(hq_hosts[ihost])
# print("connect server success!")

# api.connect('119.147.212.81', 7709)
# # data = api.to_df(api.get_security_bars(7, 0, '000001', 0, 10))
# # print(data)
# # print(data.columns)
# # print(data['datetime'][0])
# # print(type(data['datetime'][0]))
# # for itime in data['datetime']:
# #     time_obj = datetime.strptime(itime, '%Y-%m-%d %H:%M')
# #     seconds = (time_obj - datetime.utcfromtimestamp(0)).total_seconds()
# #     print(seconds)

# # print("shanghai count:", api.get_security_count(MarkeType.shanghai.value))
# # print("shenzhen count:", api.get_security_count(MarkeType.shenzhen.value))

# # sh_stock_list = api.get_security_list(MarkeType.shanghai.value, 0)
# sh_stock_list = api.get_security_list(MarkeType.shenzhen.value, 0)
# print(len(sh_stock_list))


import akshare as ak

# stock_list = ak.stock_info_a_code_name()
# stock_list = ak.stock_info_sh_delist()
# stock_list = ak.stock_info_sh_name_code()
# print(stock_list)

# stock_szse_summary_df = ak.stock_szse_summary(date="20231109")
# print(stock_szse_summary_df)

stock_sse_summary_df = ak.stock_sse_summary()
print(stock_sse_summary_df)

stock_szse_summary_df = ak.stock_szse_summary()
print(stock_szse_summary_df)
