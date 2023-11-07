# -*- encoding: utf-8 -*-
'''
@File    :   global_var.py
@Time    :   2023/11/08 00:55:17
@Author  :   frank 
@Version :   1.0
@Contact :   
@License :   
@Desc    :   
'''
from enum import Enum


class MarkeType(Enum):
    shenzhen = 0
    shanghai = 1


class BarType(Enum):
    minute_5 = 0
    minute_15 = 1
    minute_30 = 2
    hour_1 = 3
    day_1 = 4
    week_1 = 5
    month_1 = 6
    minute = 7
    minute_1 = 8
    day = 9
    season = 10
    year = 11
