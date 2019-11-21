#! -*- coding: utf-8 -*-

import random
import os
import json
import sys
from typing import Optional, List, Generator, Union, Pattern, Match, AnyStr, Dict, Any
import requests
from qinghi.constant import BASE_URL


def is_type_check():  # type: () -> bool
    """ 判断是否可用类型检查 """
    try:
        from typing import TYPE_CHECKING
    except ImportError:
        return False
    else:
        return TYPE_CHECKING


PLATFORM_IOS = [
    "iPhone 1G",
    "iPhone 3G",
    "iPhone 3GS",
    "iPhone 4",
    "Verizon iPhone 4",
    "iPhone 4S",
    "iPhone 5",
    "iPhone 5",
    "iPhone 5c",
    "iPhone 5c",
    "iPhone 5s",
    "iPhone 5s",
    "iPhone 6 Plus",
    "iPhone 6",
    "iPhone 6s",
    "iPhone 6s Plus",
    "iPhone SE",
    "iPhone 7",
    "iPhone 7 Plus",
    "iPhone 7",
    "iPhone 7 Plus",
]


def platform() -> str:
    return random.choice(PLATFORM_IOS)


def url_for(path: AnyStr, base: Optional[str] = None) -> AnyStr:
    url: str = base or BASE_URL
    url += path
    return url


def header_for() -> Dict[AnyStr, AnyStr]:
    headers: Dict[AnyStr, AnyStr] = {}
    return headers


session = requests.Session()


class _User(object):
    __payload: Dict[AnyStr, Any] = {}

    def __getattr__(self, attr: AnyStr) -> Optional[Any]:
        return self.__payload.get(attr)

    def __setattr__(self, key: AnyStr, value: Optional[Any]):
        self.__payload.setdefault(key, value)


user_config = _User()
