#! -*- coding: utf-8 -*-
from typing import Dict, AnyStr, List, Any
from qinghi.widgets import User, Widget

__version__ = '0.1.0'

class Qinghi(object):
    _widget: Widget
    _extras: Dict[AnyStr, Any]
    def __init__(self, widget: Widget, extras: dict):
        self._widget = widget
        self._extras =extras
