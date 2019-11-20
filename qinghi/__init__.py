#! -*- coding: utf-8 -*-
from typing import Dict, AnyStr, List, Any
from qinghi.widgets import User, Widget

__version__ = '0.1.0'

class Qinghi(object):
    _widget: Widget
    _extras: Dict[AnyStr, Any]
    _action: AnyStr

    def __init__(self, widget: Widget, action: AnyStr, extras: dict):
        self._widget = widget()
        self._action = action
        self._extras =extras

    def execute(self):
        self._widget.action(action=self._action, params=self._extras)