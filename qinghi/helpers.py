#! -*- coding: utf-8 -*-

import random
import os
import json
import sys
import time
import datetime
from typing import Optional, List, Generator, Union, Pattern, Match, Dict, Any
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


class _User(object):
    __payload: Dict[str, Any] = {}

    def __getattr__(self, attr: str) -> Optional[Any]:
        return self.__payload.get(attr)

    def __setattr__(self, key: str, value: Optional[Any]):
        self.__payload.setdefault(key, value)


user_config = _User()

session = requests.Session()

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


def url_for(path: str, base: Optional[str] = None) -> str:
    url: str = base or BASE_URL
    url += path
    return url


def header_for() -> Dict[str, str]:
    headers: Dict[str, str] = {}
    cookie: str = 'JSESSIONID={jsessionid};signature={signature};userId={userId}'.format(
        jsessionid=user_config.jsessionid, signature=user_config.signature, userId=user_config.userId)
    headers.update({'Cookie': cookie})
    headers.update({'Accept-Language': 'zh-Hans-CN;q=1, en-CN;q=0.9'})
    headers.update(
        {'User-Agent': 'QingHI/8.0.6 (iPhone; iOS 10.1.1; Scale/2.00)'})
    return headers


def get_unix_time_tuple(
    date=datetime.datetime.now(),
    millisecond: bool = False
) -> str:
    """ get time tuple

    get unix time tuple, default `date` is current time

    Args:
        date: datetime, default is datetime.datetime.now()
        millisecond: if True, Use random three digits instead of milliseconds, default id False 

    Return:
        a str type value, return unix time of incoming time
    """
    time_tuple = time.mktime(date.timetuple())
    time_tuple = round(time_tuple * 1000) if millisecond else time_tuple
    second = str(int(time_tuple))
    return second


def get_date_from_time_tuple(unix_time: str = get_unix_time_tuple(), formatter: str = '%Y-%m-%d %H:%M:%S') -> str:
    """ translate unix time tuple to time

    get time from unix time

    Args:
        unix_time: unix time tuple
        formatter: str time formatter

    Return:
        a time type value, return time of incoming unix_time
    """
    if len(unix_time) == 13:
        unix_time = str(float(unix_time) / 1000)
    t = int(unix_time)
    time_locol = time.localtime(t)
    return time.strftime(formatter, time_locol)
