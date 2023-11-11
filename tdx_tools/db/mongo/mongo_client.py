# -*- encoding: utf-8 -*-
# @File    :   mongo_client.py
# @Time    :   2023/11/11 17:02:52
# @Author  :   frank
# @Email:
# @Description: mongodb 读写 接口

from ast import Tuple
from ctypes import Union
from gc import collect
from http import client
from time import strftime
from typing import Optional, Type
from urllib import request

from tdx_tools.db.mongo.mongo_info import MongoDbInfo
from tdx_tools.protos.stock_pb2 import Stock

import pymongo
from pymongo import ReplaceOne
from pymongo.collection import Collection
# from pymongo.cursor import Cursor
from pymongo.results import BulkWriteResult

from typing import Dict, List

from google.protobuf.message import Message
from google.protobuf.json_format import ParseDict, MessageToDict


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


if __name__ == '__main__':
    client = MongoClient()
    client.delete_stocks()
