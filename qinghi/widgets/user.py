#! -*- coding: utf-8 -*-

from typing import AnyStr, Dict, Any, Callable
from . import Widget
from qinghi.helpers import platform, url_for, write_config
import requests


class User(Widget):
    _actions: Dict[AnyStr, Callable]

    def __init__(self):
        self._actions = {
        }

    def action(self, action: AnyStr, params: Dict[AnyStr, Any]):
        if action == 'login':
            self.login(phone=params.get('name'),
                       password=params.get('password'))

    def login(self, phone: AnyStr, password: AnyStr):
        path: str = 'android/mobileLogin_744'
        params: dict = {
            'mobilephone': phone,
            'password': password,
            'deviceType': '2',
            'detail': '机型：{platform} / 系统版本：{version}'.format(platform=platform(), version='13.1.2')
        }
        target = url_for(path=path)
        resp = requests.post(target, params)
        result = resp.json()