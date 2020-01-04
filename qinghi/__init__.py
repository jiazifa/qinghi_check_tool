#! -*- coding: utf-8 -*-
from typing import Dict, List, Any, Optional
from qinghi.widgets import User, Widget
from qinghi.config import Config

__version__ = '0.1.0'


class Qinghi(object):
    _widget: Widget
    _action: str
    _config: Optional[Config]

    def __init__(
        self,
        widget: Widget,
        action: str,
        config: Optional[Config]
    ):
        self._widget = widget()
        self._action = action
        self._config = config

    def execute(self):
        self._widget.action(action=self._action, config=self._config)
