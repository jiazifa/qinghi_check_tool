#! -*- coding: utf-8 -*-

from typing import Dict, Any, Optional
from qinghi.config import Config


class Widget(object):

    def __call__(self, *args, **kwargs):
        action: AnyStr
        params: Dict[AnyStr, Any]
        action = kwargs.get('action')
        params = kwargs.get('params')
        self.action(action, params)

    def action(self, action: str, config: Optional[Config]):
        raise NotImplementedError
