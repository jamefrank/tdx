# -*- encoding: utf-8 -*-
# @File    :   mongo_client.py
# @Time    :   2023/11/11 17:02:52
# @Author  :   frank
# @Email:
# @Description: mongodb 读写 接口


from ctypes import Union
from gc import collect
from http import client
from time import strftime
from typing import Optional, Type, Tuple
from urllib import request

from tdx_tools.db.mongo.mongo_info import MongoDbInfo
from tdx_tools.protos.stock_pb2 import Stock
from tdx_tools.protos.bar_pb2 import Bar
from tdx_tools.protos.xrxd_pb2 import XRXD

import pymongo
from pymongo import ReplaceOne
from pymongo.collection import Collection
# from pymongo.cursor import Cursor
from pymongo.results import BulkWriteResult

from typing import Dict, List

from google.protobuf.message import Message
from google.protobuf.json_format import ParseDict, MessageToDict

import datetime


class MongoClient:
    def __init__(self, db_info: MongoDbInfo = MongoDbInfo()):
        self.db_info = db_info
        self.client = pymongo.MongoClient(db_info.uri)
        # print(db_info.uri)

    def find_stocks(self) -> List[Stock]:
        """查找A股所有股票

        Returns:
            List[Stock]: A股所有股票
        """
        database = "stock"
        collection = "list"
        col = self.__get_collection(database, collection)
        cursor = col.find()
        cursor = cursor.sort("code", pymongo.ASCENDING)
        stocks = []
        for doc in cursor:
            stocks.append(self.__doc_to_stock(doc))
        return stocks

    def write_stocks(self, stocks: List[Stock]) -> BulkWriteResult:
        """存储股票信息到mongodb

        Args:
            stocks (List[Stock]): list[proto]

        Returns:
            BulkWriteResult: 写入的结果
        """
        requests = []
        for stock in stocks:
            doc = self.__stock_to_doc(stock)
            request = ReplaceOne(
                filter={'_id': doc['_id']},
                replacement=doc,
                upsert=True
            )
            requests.append(request)

        database = "stock"
        collection = "list"
        col = self.__get_collection(database, collection)
        result = col.bulk_write(requests)
        print(f"Written {len(requests)} stocks, matched {result.matched_count}, "f"modified {result.modified_count}.")
        return result

    def delete_stocks(self):
        database = "stock"
        collection = "list"
        col = self.__get_collection(database, collection)
        col.drop()

    def write_bars(self, bars: List[Bar]) -> BulkWriteResult:
        """存储某只股票的历史数据到数据库

        Args:
            bars (List[Bar]): 股票的历史数据

        Returns:
            BulkWriteResult: 写入是否成功
        """
        if not bars:
            return None
        requests = []
        for bar in bars:
            doc = self.__bar_to_doc(bar)
            request = ReplaceOne(
                filter={'_id': doc['_id']},
                replacement=doc,
                upsert=True
            )
            requests.append(request)

        database = "stock"
        collection = "bar"
        col = self.__get_collection(database, collection)
        result = col.bulk_write(requests)
        print(f"Written {len(requests)} bars, matched {result.matched_count}, "f"modified {result.modified_count}.")
        return result

    def find_bars(
            self,
            code: str,
            adjust: Optional[str] = "qfq",
            start_date: Optional[datetime.datetime] = datetime.datetime(
                year=1990,
                month=12,
                day=19,
                hour=0,
                minute=0,
                second=0)) -> List[Bar]:
        database = "stock"
        collection = "bar"
        col = self.__get_collection(database, collection)
        unix_timestamp = int(start_date.timestamp())
        query = {
            "$and":
            [
                {"code": code},
                {"adjust": adjust},
                {"timestamp": {"$gte": unix_timestamp}}
            ]
        }
        cursor = col.find(query)
        bars = []
        for doc in cursor:
            bars.append(self.__doc_to_bar(doc))
        return bars

    def delete_bars(self):
        database = "stock"
        collection = "bar"
        col = self.__get_collection(database, collection)
        col.drop()

    def find_bar_update_time(
            self,
            code: str,
            adjust: Optional[str] = "qfq") -> float:
        database = "stock"
        collection = "bar"
        col = self.__get_collection(database, collection)
        query = {
            "$and":
            [
                {"code": code},
                {"adjust": adjust},
            ]
        }

        count = col.count_documents(query)
        if count == 0:
            update_time = 661536000.0
        else:
            update_time = col.find(query).sort({"timestamp": pymongo.DESCENDING}).limit(1)[0]["timestamp"]
        return update_time

    def find_bar_update_time_patch(self):
        """使用聚合查询，批量查询更新时间
        """
        database = "stock"
        collection = "bar"
        col = self.__get_collection(database, collection)
        # 创建聚合管道
        pipeline = [
            {
                "$group": {
                    "_id": {"code": "$code", "adjust": "$adjust", "market": "$market"},
                    "maxStamp": {"$max": "$timestamp"}
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "code": "$_id.code",
                    "adjust": "$_id.adjust",
                    "market": "$_id.market",
                    "maxStamp": 1
                }
            }
        ]

        # 创建索引
        # col.drop_index([("code", 1), ("adjust", 1)])
        col.create_index([("code", 1), ("adjust", 1), ("market", 1)])

        # 执行聚合查询
        result = col.aggregate(pipeline)
        return result

    def write_xrxds(self, xrxds: List[XRXD]) -> BulkWriteResult:
        """存储分红配股信息到 数据库
        """
        if not xrxds:
            return None
        requests = []
        for xrxd in xrxds:
            doc = self.__xrxd_to_doc(xrxd)
            request = ReplaceOne(
                filter={'_id': doc['_id']},
                replacement=doc,
                upsert=True
            )
            requests.append(request)

        database = "stock"
        collection = "xrxd"
        col = self.__get_collection(database, collection)
        result = col.bulk_write(requests)
        print(f"Written {len(requests)} xrxds, matched {result.matched_count}, "f"modified {result.modified_count}.")
        return result

    def __get_collection(
        self,
        database: str,
        collection: str
    ) -> Collection:
        return self.client.get_database(database).get_collection(collection)

    def __doc_to_message(self, doc: Dict, message_cls: Type[Message]) -> Message:
        return ParseDict(doc, message_cls(), ignore_unknown_fields=True)

    def __message_to_doc(self, message: Message) -> Dict:
        return MessageToDict(
            message,
            including_default_value_fields=True,
            preserving_proto_field_name=True)

    def __doc_to_stock(self, doc: Dict) -> Stock:
        _id = doc.pop('_id')
        try:
            return self.__doc_to_message(doc, Stock)
        except Exception as e:
            raise ValueError(f"Failed to parse doc {_id}: {e}")

    def __stock_to_doc(self, stock: Stock) -> Dict:
        doc = self.__message_to_doc(stock)
        doc['_id'] = stock.market + stock.code
        return doc

    def __bar_to_doc(self, bar: Bar) -> Dict:
        doc = self.__message_to_doc(bar)
        doc['_id'] = bar.market+bar.code+":"+str(bar.timestamp)+":"+bar.adjust
        return doc

    def __doc_to_bar(self, doc: Dict) -> Bar:
        _id = doc.pop('_id')
        try:
            return self.__doc_to_message(doc, Bar)
        except Exception as e:
            raise ValueError(f"Failed to parse doc {_id}: {e}")

    def __xrxd_to_doc(self, xrxd: XRXD) -> Dict:
        doc = self.__message_to_doc(xrxd)
        doc['_id'] = xrxd.code+":"+str(xrxd.date_ts)
        return doc


if __name__ == '__main__':
    client = MongoClient()
    # client.delete_stocks()
    client.delete_bars()
