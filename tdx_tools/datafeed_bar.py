# -*- encoding: utf-8 -*-
# @File    :   datafeed-bar.py
# @Time    :   2023/11/12 15:02:05
# @Author  :   frank
# @Email:
# @Description: 从第三方数据拉取数据

from ast import List
import time
import datetime
from tqdm import tqdm
import akshare as ak
from tdx_tools.db.mongo.mongo_client import MongoClient
from tdx_tools.protos.bar_pb2 import Bar
from multiprocessing import Pool, Manager
from itertools import product
from functools import partial


def unix_timestamp_to_str(unix_ts: float) -> str:
    datetime_obj = datetime.datetime.fromtimestamp(unix_ts)
    return datetime_obj.strftime("%Y%m%d")


def str_to_unix_timestamp(ts: str) -> float:
    datetime_obj = datetime.datetime.strptime(ts, "%Y%m%d")
    return datetime_obj.timestamp()


def process_bar_daily(args, adjusts: List, latest_data_date: float, trade_date: List):
    period = "daily"
    DATE_STR = '日期'
    OPEN_STR = '开盘'
    CLOSE_STR = '收盘'
    HIGH_STR = '最高'
    LOW_STR = '最低'
    VOL_STR = '成交量'
    AMOUNT_STR = '成交额'

    client = MongoClient()
    code, market = args

    trade_date_end = trade_date[-1]
    for adjust in adjusts:
        #
        update_ts = client.find_bar_update_time(code, adjust)
        if update_ts >= latest_data_date:
            break
        #
        cnt = 0
        while trade_date[cnt] < update_ts:
            cnt += 1
        trade_date_start = unix_timestamp_to_str(trade_date[cnt])
        while True:
            try:
                bar_df = ak.stock_zh_a_hist(
                    symbol=code,
                    period=period,
                    start_date=trade_date_start,
                    end_date=trade_date_end,
                    adjust=adjust
                )

                bars = []
                for index, row in bar_df.iterrows():
                    bar = Bar()
                    bar.market = market
                    bar.code = code
                    bar.adjust = adjust

                    time_obj = datetime.time(15, 0, 0)
                    datetime_obj = datetime.datetime.combine(row[DATE_STR], time_obj)
                    unix_timestamp = int(datetime_obj.timestamp())
                    bar.timestamp = unix_timestamp

                    bar.open = row[OPEN_STR]
                    bar.close = row[CLOSE_STR]
                    bar.high = row[HIGH_STR]
                    bar.low = row[LOW_STR]
                    bar.vol = row[VOL_STR]
                    bar.amount = row[AMOUNT_STR]

                    bars.append(bar)
                client.write_bars(bars)
                break
            except Exception as e:
                print(e)


def get_stock_bar_daily():

    ENABLE_MULTIPLE = True
    ENABLE_MULTIPLE = False

    NUM_PROCESS = 24

    #
    trade_date_hist = ak.tool_trade_date_hist_sina()
    trade_date_str = "trade_date"
    trade_date = trade_date_hist[trade_date_str]
    trade_date = [datetime.datetime.combine(date, datetime.datetime.min.time()).timestamp() for date in trade_date_hist[trade_date_str]]

    #
    client = MongoClient()
    stocks = client.find_stocks()
    code_list = [stock.code for stock in stocks]
    market_list = [stock.market for stock in stocks]
    adjusts = ["qfq", "hfq", ""]

    #
    current_unix_stamp = datetime.datetime.now().timestamp()
    cnt = 0
    while trade_date[cnt] < current_unix_stamp:
        cnt += 1
    ELAPSE_THRESH = 19*3600
    latest_data_date = trade_date[cnt-1] if current_unix_stamp-trade_date[cnt-1] > ELAPSE_THRESH else trade_date[cnt-2]
    latest_data_date += 15*3600

    #
    partial_process_bar_daily = partial(
        process_bar_daily,
        adjusts=adjusts,
        latest_data_date=latest_data_date,
        trade_date=trade_date
    )
    #
    iterable_args = zip(code_list, market_list)
    #
    if ENABLE_MULTIPLE:
        with Pool(processes=NUM_PROCESS) as pool:
            #
            progress_bar = tqdm(total=len(code_list))
            #
            for _ in pool.imap(partial_process_bar_daily, iterable_args):
                progress_bar.update(1)
            #
            progress_bar.close()
    else:
        for iter in tqdm(iterable_args, total=len(code_list)):
            partial_process_bar_daily(iter)
            break


if __name__ == '__main__':
    get_stock_bar_daily()
    print("finish")
