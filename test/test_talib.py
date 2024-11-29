# -*- encoding: utf-8 -*-
# @File    :   test_talib.py
# @Time    :   2023/11/18 16:28:34
# @Author  :   frank
# @Email:
# @Description: 测试talib计算指标

import talib
import numpy as np

close_price = [10, 11, 9, 8, 10, 11, 9, 13, 17, 15, 14, 13]
close_price = np.array(close_price, dtype=np.float64)
ma5 = talib.MA(close_price, timeperiod=5)

print(ma5)
# ma5 = [nan, nan, nan, nan, 10.0, 10.6, 9.8, 11.0, 13.0, 13.6, 13.2, 12.8]
