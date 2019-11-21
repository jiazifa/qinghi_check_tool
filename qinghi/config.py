#! -*- coding: utf-8 -*-

from typing import Optional, Text, Sequence, AnyStr, Dict, Any

class _Config(object):
    __payload: Dict[AnyStr, Any]
    
    def __getattr__(self, attr: AnyStr) -> Optional[Any]:
        return self.__payload.get(attr)
    
    def __setattr__(self, key: AnyStr, value: Optional[Any]):
        self.__payload[key] = value

config = _Config()