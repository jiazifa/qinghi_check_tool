#! -*- coding: utf-8 -*-
from configparser import ConfigParser
from typing import Optional, Text, Sequence, Dict, Any, List, Tuple
import random

LOCATIONS: List[Tuple[float, float, str]] = [
    (30.185444, 120.162222, "浙江省杭州市滨江区浦沿街道南环路27号"),
    (30.179597854614258, 120.15566253662109, "浙江省杭州市滨江区联庄路靠近金南创业大厦"),
    (30.17957954, 120.155963236, "浙江省杭州市滨江区连庄路靠近金南创业大厦"),
    (30.1785978, 120.161262, "浙江省杭州市滨江区南环路靠近钱塘江站")
]

class Config(object):
    _source_file: str
    _cf: ConfigParser

    # User
    mobilephone: Optional[str]
    password: Optional[str]
    latitude: Optional[str]
    longitude: Optional[str]
    address: Optional[str]

    def __init__(self, path: Optional[str]):
        if path:
            self._source_file = path
            self._cf = ConfigParser()
            self._cf.read(path)
            self.prepare()
        else:
            location: Tuple[float, float, str] = random.choice(LOCATIONS)
            latitude, longitude, address = location
            self.latitude = latitude
            self.longitude = longitude
            self.address = address

    def prepare(self):
        sections = self._cf.sections()
        self.mobilephone = self._cf.get('User', 'mobilephone')
        self.password = self._cf.get('User', 'password')

        location: Tuple[float, float, str] = random.choice(LOCATIONS)
        latitude, longitude, address = location
        self.latitude = latitude
        self.longitude = longitude
        self.address = address
