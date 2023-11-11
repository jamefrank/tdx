# -*- encoding: utf-8 -*-
# @File    :   mongo_info.py
# @Time    :   2023/11/11 16:21:07
# @Author  :   frank
# @Email:
# @Description: mongodb 基本信息


import os
from dataclasses import dataclass
from typing import Optional
from urllib.parse import quote_plus


def get_default_host(server: str = 'MONGODB_SERVER') -> Optional[str]:
    host = os.environ[server] if server in os.environ else None
    return host


def get_default_port(port: str = 'MONGODB_PORT') -> int:
    port = os.environ[port] if port in os.environ else 27017
    return port


def get_default_user(user: str = 'MONGODB_USERNAME') -> Optional[str]:
    user = os.environ[user] if user in os.environ else None
    return user


def get_default_password(password: str = 'MONGODB_PASSWORD') -> Optional[str]:
    password = os.environ[password] if password in os.environ else None
    return password


@dataclass
class MongoDbInfo:
    host: str = get_default_host('STOCK_SERVER')
    port: int = get_default_port('STOCK_PORT')
    user: str = get_default_user('STOCK_USERNAME')
    password: str = get_default_password('STOCK_PASSWORD')

    @property
    def server(self) -> str:
        if self.host is None:
            raise ValueError("Need to Set MONGODB_SERVER Env.")
        return f"{self.host}:{self.port}"

    @property
    def uri(self):
        if self.user is None:
            raise ValueError("Need to Set MONGODB_USERNAME Env.")

        if self.password is None:
            raise ValueError("Need to Set MONGODB_PASSWORD Env.")

        uri = f"mongodb://{quote_plus(self.user)}:{quote_plus(self.password)}@{self.server}"
        return uri
