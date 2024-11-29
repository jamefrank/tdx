'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2024-11-28 23:27:14
LastEditors: frank 13121950875@163.com
LastEditTime: 2024-11-30 00:14:41
FilePath: /tdx/tdx_tools/parse_tools/parse.py
Description:  解析数据的工具

Copyright (c) 2024 by Frank, All Rights Reserved. 
'''
import os
import time
import hashlib
import pandas as pd
import numpy as np
import pytdx.reader.gbbq_reader
from tdx_tools.parse_tools.user_cfg import LOCAL_CW_DIR, LOCAL_STOCKS_CODE_FILE, TDX_CW_OUTPUT_DIR, TDX_GBBQ_OUTPUT_DIR,TDX_INSTALL_DIR,LOCAL_GBBQ_FILE

def parse_sh_zs_stock_list():
    tdx_stocks = pd.read_csv(LOCAL_STOCKS_CODE_FILE,sep='|', header=None, index_col=None, encoding='gbk', dtype={0: str})
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


# -----------------------------------------------
from retry import retry
import requests

@retry(tries=3, delay=3)  # 无限重试装饰性函数
def dowload_url(url):
    """
    :param url:要下载的url
    :return: request.get实例化对象
    """
    
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/87.0.4280.141',
    }
    response_obj = requests.get(url, headers=header, timeout=5)  # get方式请求
    response_obj.raise_for_status()  # 检测异常方法。如有异常则抛出，触发retry
    # print(f'{url} 下载完成')
    return response_obj

def list_localTDX_cwfile(ext_name):
    """
    列出本地已有的专业财务文件。返回文件列表
    :param ext_name: str类型。文件扩展名。返回指定扩展名的文件列表
    :return: list类型。财务专业文件列表
    """
    tmplist = os.listdir(LOCAL_CW_DIR)  # 遍历通达信vipdoc/cw目录
    cw_filelist = []
    for file in tmplist:  # 只保留gpcw????????.扩展名 格式文件
        if len(file) == 16 and file[:4] == "gpcw" and file[-4:] == "." + ext_name:
            cw_filelist.append(file)
    # print(f'检测到{len(cw_filelist)}个专业财务文件')
    return cw_filelist

import threading
from queue import Queue

class ManyThreadDownload:
    def __init__(self, num=10):
        self.num = num  # 线程数,默认10
        self.url = ''  # url
        self.name = ''  # 目标地址
        self.total = 0  # 文件大小

    # 获取每个线程下载的区间
    def get_range(self):
        ranges = []
        offset = int(self.total / self.num)
        for i in range(self.num):
            if i == self.num - 1:
                ranges.append((i * offset, ''))
            else:
                ranges.append(((i * offset), (i + 1) * offset - 1))
        return ranges  # [(0,99),(100,199),(200,"")]

    # 通过传入开始和结束位置来下载文件
    def download(self, ts_queue):
        while not ts_queue.empty():
            start_, end_ = ts_queue.get()
            headers = {
                'Range': 'Bytes=%s-%s' % (start_, end_),
                'Accept-Encoding': '*'
            }
            flag = False
            while not flag:
                try:
                    # 设置重连次数
                    requests.adapters.DEFAULT_RETRIES = 10
                    # s = requests.session()            # 每次都会发起一次TCP握手,性能降低，还可能因发起多个连接而被拒绝
                    # # 设置连接活跃状态为False
                    # s.keep_alive = False
                    # 默认stream=false,立即下载放到内存,文件过大会内存不足,大文件时用True需改一下码子
                    res = requests.get(self.url, headers=headers)
                    res.close()  # 关闭请求  释放内存
                except Exception as e:
                    print((start_, end_, "出错了,连接重试:%s", e,))
                    time.sleep(1)
                    continue
                flag = True

            # print("\n", ("%s-%s download success" % (start_, end_)), end="", flush=True)
            # with lock:
            with open(self.name, "rb+") as fd:
                fd.seek(start_)
                fd.write(res.content)
            # self.fd.seek(start_)                                        # 指定写文件的位置,下载的内容放到正确的位置处
            # self.fd.write(res.content)                                  # 将下载文件保存到 fd所打开的文件里

    def run(self, url, name):
        self.url = url
        self.name = name
        self.total = int(requests.head(url).headers['Content-Length'])
        # file_size = int(urlopen(self.url).info().get('Content-Length', -1))
        file_size = self.total
        if os.path.exists(name):
            first_byte = os.path.getsize(name)
        else:
            first_byte = 0
        if first_byte >= file_size:
            return file_size

        self.fd = open(name, "wb")  # 续传时直接rb+ 文件不存在时会报错,先wb再rb+
        self.fd.truncate(self.total)  # 建一个和下载文件一样大的文件,不是必须的,stream=True时会用到
        self.fd.close()
        # self.fd = open(self.name, "rb+")           # 续传时ab方式打开时会强制指针指向文件末尾,seek并不管用,应用rb+模式
        thread_list = []
        ts_queue = Queue()  # 用队列的线程安全特性，以列表的形式把开始和结束加到队列
        for ran in self.get_range():
            start_, end_ = ran
            ts_queue.put((start_, end_))

        for i in range(self.num):
            t = threading.Thread(target=self.download, name='th-' + str(i), kwargs={'ts_queue': ts_queue})
            # t.setDaemon(True)
            t.daemon = True
            thread_list.append(t)
        for t in thread_list:
            t.start()
        for t in thread_list:
            t.join()  # 设置等待，全部线程完事后再继续

        self.fd.close()
        
def historyfinancialreader(filepath):
    """
    读取解析通达信目录的历史财务数据
    :param filepath: 字符串类型。传入文件路径
    :return: DataFrame格式。返回解析出的财务文件内容
    """
    import struct

    cw_file = open(filepath, 'rb')
    header_pack_format = '<1hI1H3L'
    header_size = struct.calcsize(header_pack_format)
    stock_item_size = struct.calcsize("<6s1c1L")
    data_header = cw_file.read(header_size)
    stock_header = struct.unpack(header_pack_format, data_header)
    max_count = stock_header[2]
    report_date = stock_header[1]
    report_size = stock_header[4]
    report_fields_count = int(report_size / 4)
    report_pack_format = '<{}f'.format(report_fields_count)
    results = []
    for stock_idx in range(0, max_count):
        cw_file.seek(header_size + stock_idx * struct.calcsize("<6s1c1L"))
        si = cw_file.read(stock_item_size)
        stock_item = struct.unpack("<6s1c1L", si)
        code = stock_item[0].decode("utf-8")
        foa = stock_item[2]
        cw_file.seek(foa)
        info_data = cw_file.read(struct.calcsize(report_pack_format))
        data_size = len(info_data)
        cw_info = list(struct.unpack(report_pack_format, info_data))
        cw_info.insert(0, code)
        results.append(cw_info)
    cw_file.close()
    df = pd.DataFrame(results)
    return df

import zipfile

def parse_cw():
    starttime = time.time()
    # 下载通达信服务器文件校检信息txt
    tdx_txt_url = 'http://down.tdx.com.cn:8001/tdxfin/gpcw.txt'
    tdx_txt_df = dowload_url(tdx_txt_url)  # 下载gpcw.txt
    tdx_txt_df = tdx_txt_df.text.strip().split('\r\n')  # 分割行
    tdx_txt_df = [l.strip().split(",") for l in tdx_txt_df]  # 用,分割，二维列表
    tdx_txt_df = pd.DataFrame(tdx_txt_df, columns=['filename', 'md5', 'filesize'])  # 转为df格式，好比较
    # print(tdx_txt_df)
    
    # 检查本机通达信dat文件是否有缺失
    local_zipfile_list = list_localTDX_cwfile('zip')  # 获取本机已有文件
    many_thread_download = ManyThreadDownload()
    for df_filename in tdx_txt_df['filename'].tolist():
        starttime_tick = time.time()
        if df_filename not in local_zipfile_list:
            print(f'{df_filename} 本机没有 开始下载')
            tdx_zipfile_url = 'http://down.tdx.com.cn:8001/tdxfin/' + df_filename
            local_zipfile_path = LOCAL_CW_DIR / df_filename
            many_thread_download.run(tdx_zipfile_url, local_zipfile_path)
            with zipfile.ZipFile(local_zipfile_path, 'r') as zipobj:  # 打开zip对象，释放zip文件。会自动覆盖原文件。
                zipobj.extractall(LOCAL_CW_DIR)
            local_datfile_path = local_zipfile_path[:-4] + ".dat"
            df = historyfinancialreader(local_datfile_path)
            csvpath = TDX_CW_OUTPUT_DIR / df_filename[:-4] + ".pkl"
            df.to_pickle(csvpath, compression=None)
            print(f'{df_filename} 完成更新 用时 {(time.time() - starttime_tick):>5.2f} 秒')
    
    # 检查本机通达信zip文件是否需要更新
    local_zipfile_list = list_localTDX_cwfile('zip')  # 获取本机已有文件
    for zipfile_filename in local_zipfile_list:
        starttime_tick = time.time()
        local_zipfile_path = LOCAL_CW_DIR / zipfile_filename
        with open(local_zipfile_path, 'rb') as fobj:  # 读取本机zip文件，计算md5
            file_content = fobj.read()
            file_md5 = hashlib.md5(file_content).hexdigest()
        if file_md5 not in tdx_txt_df['md5'].tolist():  # 本机zip文件的md5与服务器端不一致
            print(f'{zipfile_filename} 需要更新 开始下载')
            os.remove(local_zipfile_path)  # 删除本机zip文件
            tdx_zipfile_url = 'http://down.tdx.com.cn:8001/tdxfin/' + zipfile_filename
            many_thread_download.run(tdx_zipfile_url, local_zipfile_path)
            with zipfile.ZipFile(local_zipfile_path, 'r') as zipobj:  # 打开zip对象，释放zip文件。会自动覆盖原文件。
                try:
                    zipobj.extractall(LOCAL_CW_DIR)
                except zipfile.BadZipFile:
                    os.remove(local_zipfile_path)  # 删除本机zip文件
                    print(f'文件{local_zipfile_path}下载损坏，或服务器端文件错误，跳过此文件')


            local_datfile_path = LOCAL_CW_DIR / (zipfile_filename[:-4] + ".dat")
            df = historyfinancialreader(local_datfile_path)
            csvpath = TDX_CW_OUTPUT_DIR / (zipfile_filename[:-4] + ".pkl")
            df.to_pickle(csvpath, compression=None)
            print(f'{zipfile_filename} 完成更新 用时 {(time.time() - starttime_tick):>5.2f} 秒')

    # 检查本机财报导出文件是否存在
    cwfile_list = os.listdir(TDX_CW_OUTPUT_DIR)  # cw目录 生成文件名列表
    local_datfile_list = list_localTDX_cwfile('dat')  # 获取本机已有文件
    for filename in local_datfile_list:
        starttime_tick = time.time()
        filenamepkl = filename[:-4] + '.pkl'
        pklpath = TDX_CW_OUTPUT_DIR / filenamepkl
        filenamedat = filename[:-4] + '.dat'
        datpath = LOCAL_CW_DIR / filenamedat
        if filenamepkl not in cwfile_list:  # 本机zip文件的md5与服务器端不一致
            print(f'{filename} 本机没有 需要导出')
            df = historyfinancialreader(datpath)
            df.to_pickle(pklpath, compression=None)
            print(f'{filename} 完成更新 用时 {(time.time() - starttime_tick):>5.2f} 秒')

    print(f'专业财务文件检查更新完成 已用 {(time.time() - starttime):>5.2f} 秒')

def parse_gbbq():
    # 解密通达信股本变迁文件
    starttime_tick = time.time()
    category = {
        '1': '除权除息', '2': '送配股上市', '3': '非流通股上市', '4': '未知股本变动', '5': '股本变化',
        '6': '增发新股', '7': '股份回购', '8': '增发新股上市', '9': '转配股上市', '10': '可转债上市',
        '11': '扩缩股', '12': '非流通股缩股', '13': '送认购权证', '14': '送认沽权证'}
    print(f'解密通达信gbbq股本变迁文件')
    filepath = LOCAL_GBBQ_FILE
    df_gbbq = pytdx.reader.gbbq_reader.GbbqReader().get_df(filepath)
    df_gbbq.drop(columns=['market'], inplace=True)
    df_gbbq.columns = ['code', '权息日', '类别',
                    '分红-前流通盘', '配股价-前总股本', '送转股-后流通盘', '配股-后总股本']
    df_gbbq['类别'] = df_gbbq['类别'].astype('object')
    df_gbbq['code'] = df_gbbq['code'].astype('object')
    for i in range(df_gbbq.shape[0]):
        df_gbbq.iat[i, df_gbbq.columns.get_loc("类别")] = category[str(df_gbbq.iat[i, df_gbbq.columns.get_loc("类别")])]
    df_gbbq.to_csv(TDX_GBBQ_OUTPUT_DIR/ 'gbbq.csv', encoding='gbk', index=False)
    # 如果读取，使用下行命令
    # df_gbbq = pd.read_csv(ucfg.tdx['csv_cw'] + '/gbbq.csv', encoding='gbk', dtype={'code': 'object'})
    print(f'股本变迁解密完成 用时 {(time.time() - starttime_tick):>5.2f} 秒')
    pass

def main():
    # sh_codes = parse_sh_code()
    # # print(sh_codes)
    # print(sh_codes.iloc[0])
    # # sh_names = parse_sh_name()
    # # print(sh_names)
    # pass

    # code = sh_codes.iloc[0]
    # code_data_path = TDX_INSTALL_DIR/ f"vipdoc/sh/lday/sh{code}.day"
    # data = parse_day(code_data_path)
    # print(data)
    
    parse_cw()
    parse_gbbq()
    pass
 
 
if __name__ == '__main__':
    main()
    pass
