'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2024-11-28 22:07:33
LastEditors: frank 13121950875@163.com
LastEditTime: 2024-11-30 00:12:17
FilePath: /tdx/tdx_tools/parse_tools/user_cfg.py
Description:  用户配置

Copyright (c) 2024 by Frank, All Rights Reserved. 
'''

import os
import pandas as pd
from pathlib import Path
from tdx_tools.logger_config import setup_logger

logger = setup_logger("user_cfg")


TDX_INSTALL_DIR = Path("/mnt/c/new_tdx")
LOCAL_STOCKS_CODE_FILE = TDX_INSTALL_DIR / "T0002/hq_cache/infoharbor_ex.code"
LOCAL_CW_DIR = TDX_INSTALL_DIR / "vipdoc/cw"
LOCAL_GBBQ_FILE = TDX_INSTALL_DIR / "T0002/hq_cache/gbbq"

#
BASE_OUTPUT_DIR = Path(__file__).parent
TDX_CW_OUTPUT_DIR = BASE_OUTPUT_DIR / "data/cw"  #股本变迁等财务数据的输出目录
os.makedirs(TDX_CW_OUTPUT_DIR, exist_ok=True)
TDX_GBBQ_OUTPUT_DIR = BASE_OUTPUT_DIR / "data"
os.makedirs(TDX_GBBQ_OUTPUT_DIR, exist_ok=True)

def main():
    logger.info(f"TDX_INSTALL_DIR:{TDX_INSTALL_DIR}")
    tdx_stocks = pd.read_csv(LOCAL_STOCKS_CODE_FILE,sep='|', header=None, index_col=None, encoding='gbk', dtype={0: str})
    tdx_stocks = tdx_stocks[~(tdx_stocks[0].str.startswith('9')
                              | tdx_stocks[0].str.startswith('8') 
                              | tdx_stocks[0].str.startswith('68') # 科创板
                              | tdx_stocks[0].str.startswith('43') # 新三板
                              | tdx_stocks[0].str.startswith('30') # 创业板
                              )]
    print(tdx_stocks)
    # file_listsh = tdx_stocks[0][tdx_stocks[0].apply(lambda x: x[0:1] == "6")]
    file_listsh = tdx_stocks[tdx_stocks[0].apply(lambda x: x[0:1] == "6")]
    # file_listsz = tdx_stocks[0][tdx_stocks[0].apply(lambda x: x[0:1] != "6")]
    file_listsz = tdx_stocks[tdx_stocks[0].apply(lambda x: x[0:1] != "6")]
    # test = tdx_stocks[0][tdx_stocks[0].apply(lambda x: x[0:1] == "2")]
    
    print(file_listsh)
    print(file_listsz)
    # print(test)
    pass
 
 
if __name__ == '__main__':
    main()
    pass
