'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2024-11-28 23:27:14
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2024-11-28 23:53:35
FilePath: /tdx/tdx_tools/parse_tools/parse.py
Description:  解析数据的工具

Copyright (c) 2024 by Frank, All Rights Reserved. 
'''

import pandas as pd
import numpy as np
from tdx_tools.parse_tools.user_cfg import STOCKS_CODE_FILE,TDX_INSTALL_DIR

def parse_sh_zs_stock_list():
    tdx_stocks = pd.read_csv(STOCKS_CODE_FILE,sep='|', header=None, index_col=None, encoding='gbk', dtype={0: str})
    tdx_stocks = tdx_stocks[~(tdx_stocks[0].str.startswith('9')
                              | tdx_stocks[0].str.startswith('8') 
                              | tdx_stocks[0].str.startswith('68') # 科创板
                              | tdx_stocks[0].str.startswith('43') # 新三板
                              | tdx_stocks[0].str.startswith('30') # 创业板
                              )]
    return tdx_stocks

def parse_sh_code():
    tdx_stocks = parse_sh_zs_stock_list()
    codes = tdx_stocks[0][tdx_stocks[0].apply(lambda x: x[0:1] == "6")]
    return codes

def parse_sz_code():
    tdx_stocks = parse_sh_zs_stock_list()
    codes = tdx_stocks[0][tdx_stocks[0].apply(lambda x: x[0:1] != "6")]
    return codes

def parse_sh_name():
    tdx_stocks = parse_sh_zs_stock_list()
    codes = tdx_stocks[1][tdx_stocks[0].apply(lambda x: x[0:1] == "6")]
    return codes

def parse_sz_name():
    tdx_stocks = parse_sh_zs_stock_list()
    codes = tdx_stocks[1][tdx_stocks[0].apply(lambda x: x[0:1] != "6")]
    return codes


def parse_day(data_path):
    dt = np.dtype([
        ('Date', 'u4'),
        ('Open', 'u4'),
        ('High', 'u4'),
        ('Low', 'u4'),
        ('Close', 'u4'),
        ('Amount', 'f'),
        ('Volume', 'u4'),
        ('Reserve','u4')])
    data = np.fromfile(data_path, dtype=dt)
    #df = pd.DataFrame(data)
    # Or if you want to explicitly set the column names
    df = pd.DataFrame(data, columns=data.dtype.names)
    df.eval('''
        year=floor(Date/10000)
        month=floor((Date%10000)/100)
        day=floor(Date%10000%100)
        Open=Open/100
        High=High/100
        Low=Low/100
        Close=Close/100
    ''',inplace=True)
    df.index=pd.to_datetime(df.loc[:,['year','month','day']])
    return df.drop(columns=['Date','year','month','day'])


# TODO
def 读取分钟数据(文件路径):
    '''
    year=floor(m_date/2048)+2004; %提取年信息
    mon=floor(mod(m_date,2048)/100); %提取月信息
    day=mod(mod(m_date,2048),100); %提取日信息*/
    m_time/60 输出小时
    m_time%60 输出分钟
    '''
    dt = np.dtype([
        ('m_date', 'u2'),
        ('m_time', 'u2'),
        ('Open', 'f4'),
        ('High', 'f4'),
        ('Low', 'f4'),
        ('Close', 'f4'),
        ('Amount', 'f4'),
        ('Volume', 'u4'),
        ('Reserve','u4')])
    data = np.fromfile(文件路径, dtype=dt)
    #df = pd.DataFrame(data)
    # Or if you want to explicitly set the column names
    df = pd.DataFrame(data, columns=data.dtype.names)
    df.eval('''
        year=floor(m_date/2048)+2004
        month=floor((m_date%2048)/100)
        day=floor(m_date%2048%100)
        hour = floor(m_time/60)
        minute = m_time%60
    ''',inplace=True)
    df.index=pd.to_datetime(df.loc[:,['year','month','day','hour','minute']])
    return df.drop(columns= ['m_date','m_time','year','month','day','hour','minute'])


def main():
    sh_codes = parse_sh_code()
    # print(sh_codes)
    print(sh_codes.iloc[0])
    # sh_names = parse_sh_name()
    # print(sh_names)
    pass

    code = sh_codes.iloc[0]
    code_data_path = TDX_INSTALL_DIR/ f"vipdoc/sh/lday/sh{code}.day"
    data = parse_day(code_data_path)
    print(data)
 
 
if __name__ == '__main__':
    main()
    pass
