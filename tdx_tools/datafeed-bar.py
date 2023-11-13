# -*- encoding: utf-8 -*-
# @File    :   datafeed-bar.py
# @Time    :   2023/11/12 15:02:05
# @Author  :   frank
# @Email:
# @Description: 从第三方数据拉取数据

import time
import datetime
from tqdm import tqdm
import akshare as ak
from tdx_tools.db.mongo.mongo_client import MongoClient
from tdx_tools.protos.bar_pb2 import Bar


def unix_timestamp_to_str(unix_ts: float) -> str:
    datetime_obj = datetime.datetime.fromtimestamp(unix_ts)
    return datetime_obj.strftime("%Y%m%d")


def str_to_unix_timestamp(ts: str) -> float:
    datetime_obj = datetime.datetime.strptime(ts, "%Y%m%d")
    return datetime_obj.timestamp()


def get_stock_bar_daily():
    #
    trade_date_hist = ak.tool_trade_date_hist_sina()
    trade_date_str = "trade_date"
    trade_date = trade_date_hist[trade_date_str]
    trade_date = [datetime.datetime.combine(date, datetime.datetime.min.time()).timestamp() for date in trade_date_hist[trade_date_str]]
    # trade_date = [date.strftime("%Y%m%d") for date in trade_date_hist[trade_date_str]]
    trade_date_start = trade_date[0]
    trade_date_end = trade_date[-1]
    print(trade_date_start)
    print(trade_date_end)

    #
    client = MongoClient()
    stocks = client.find_stocks()
    code_list = [stock.code for stock in stocks]
    market_list = [stock.market for stock in stocks]

    #
    current_unix_stamp = datetime.datetime.now().timestamp()
    cnt = 0
    while trade_date[cnt] < current_unix_stamp:
        cnt += 1
    latest_data_date = trade_date[cnt-1]

    #
    adjusts = ["qfq", "hfq", ""]
    period = "daily"
    DATE_STR = '日期'
    OPEN_STR = '开盘'
    CLOSE_STR = '收盘'
    HIGH_STR = '最高'
    LOW_STR = '最低'
    VOL_STR = '成交量'
    AMOUNT_STR = '成交额'

    for idx in tqdm(range(len(code_list))):
        for adjust in adjusts:
            while True:
                try:
                    #
                    update_ts = client.find_bar_update_time(code_list[idx], adjust)
                    print(update_ts)
                    #
                    tmp_bars = client.find_bars(code_list[idx], adjust)
                    tmp_ts = [bar.timestamp for bar in tmp_bars]
                    tmp_ts.append(str_to_unix_timestamp(trade_date_start))
                    tmp_max_ts = max(tmp_ts)
                    if current_unix_stamp - tmp_max_ts < (24+4)*3600:
                        continue
                    tmp_trade_date_start = unix_timestamp_to_str(tmp_max_ts)
                    tmp_index = trade_date.index(tmp_trade_date_start)
                    if tmp_index > 0 and tmp_index < len(trade_date)-1:
                        tmp_trade_date_start = trade_date[tmp_index+1]
                    elif tmp_index == len(trade_date)-1:
                        continue

                    bar_df = ak.stock_zh_a_hist(
                        symbol=code_list[idx],
                        period=period,
                        start_date=tmp_trade_date_start,
                        end_date=trade_date_end,
                        adjust=adjust
                    )

                    bars = []
                    for index, row in bar_df.iterrows():
                        bar = Bar()
                        bar.market = market_list[idx]
                        bar.code = code_list[idx]
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


if __name__ == '__main__':
    get_stock_bar_daily()
    print("finish")
