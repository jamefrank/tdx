'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2024-11-28 22:18:08
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2024-11-28 22:30:54
FilePath: /tdx/tdx_tools/logger_config.py
Description:  日志配置器

Copyright (c) 2024 by Frank, All Rights Reserved. 
'''

# logger_config.py

import logging
import os

def setup_logger(name):
    # 创建日志记录器
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # 创建处理器
    stream_handler = logging.StreamHandler()
    log_file_path = os.path.join(os.getcwd(), 'tdx.log')
    file_handler = logging.FileHandler(log_file_path)

    # 设置日志级别
    stream_handler.setLevel(logging.INFO)
    file_handler.setLevel(logging.DEBUG)

    # 创建格式化器
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    stream_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # 添加处理器到日志记录器
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    return logger

# 初始化并导出 logger
logger = setup_logger('my_logger')

def main():
    logger.debug("This is a debug message from module2")
    logger.info("This is an info message from module2")
    logger.warning("This is a warning message from module2")
    logger.error("This is an error message from module2")
    logger.critical("This is a critical message from module2")

if __name__ == "__main__":
    main()