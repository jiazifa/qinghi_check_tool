#! -*- coding: utf-8 -*-
from configparser import ConfigParser
from typing import Optional, Text, Sequence, AnyStr, Dict, Any

class Config(object):
    _source_file: AnyStr
    _cf: ConfigParser
    
    # User
    mobilephone: Optional[AnyStr]
    password: Optional[AnyStr]

    def __init__(self, path: AnyStr):
        self._source_file = path
        self._cf = ConfigParser()
        self._cf.read(path)
        self.prepare()
    
    def prepare(self):
        sections = self._cf.sections()
        self.mobilephone = self._cf.get('User', 'mobilephone')
        self.password = self._cf.get('User', 'password')