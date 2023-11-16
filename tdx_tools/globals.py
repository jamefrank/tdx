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

import time


def mesure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = (end_time - start_time)*1000
        print(f"函数 {func.__name__} 的运行时间为：{execution_time:.6f} 毫秒")
        return result
    return wrapper

# 方法一：
# class ReadOnlyDescriptor:
#     def __init__(self, value):
#         self._value = value

#     def __get__(self, instance, owner):
#         return self._value

#     def __set__(self, instance, value):
#         raise AttributeError("Cannot modify read-only attribute")


# class Singleton:
#     _instance = None
#     XRXD_DATE_LIST = ReadOnlyDescriptor(
#         [
#             '03-31',
#             '06-30',
#             '09-30',
#             '12-31'
#         ]
#     )

#     def __new__(cls):
#         """保证唯一性
#         """
#         if not cls._instance:
#             cls._instance = super().__new__(cls)
#         return cls._instance

# 方法二：
class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_initialized'):
            self._xrx_date_list = [
                '03-31',
                '06-30',
                '09-30',
                '12-31'
            ]
            self._initialized = True

    @property
    def XRXD_DATE_LIST(self):
        return self._xrx_date_list


singleton_instance = Singleton()

if __name__ == '__main__':
    pass
