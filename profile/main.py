# -*- encoding: utf-8 -*-
# @File    :   main.py
# @Time    :   2023/11/15 13:14:15
# @Author  :   frank
# @Email:
# @Description: 分析脚本性能

import cProfile
import tdx_tools.datafeed_bar
import pstats

file = '/home/frank/tdx/profile/result.out'
cProfile.run('tdx_tools.datafeed_bar.get_stock_bar_daily()', filename=file)

p = pstats.Stats(file)

# 总耗时
p.sort_stats('cumulative').print_stats(30)
