# -*- encoding: utf-8 -*-
# @File    :   test_globals.py
# @Time    :   2023/11/16 09:12:25
# @Author  :   frank
# @Email:
# @Description: 测试global在多进程中的使用

from multiprocessing import Process
from tdx_tools.globals import singleton_instance


def worker():
    print(singleton_instance)


if __name__ == '__main__':
    p1 = Process(target=worker)
    p2 = Process(target=worker)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
