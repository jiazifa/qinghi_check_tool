#! -*- coding: utf-8 -*-

from typing import AnyStr, Dict, Any, Callable, Optional
from . import Widget
from qinghi.helpers import platform, url_for, session, user_config
from qinghi.config import Config

class User(Widget):
    _actions: Dict[AnyStr, Any]

    def __init__(self):
        self._actions = {
            'login': self.login,
            'checkin': self.check_in_work,
        }

    def action(self, action: AnyStr, config: Optional[Config]):
        act = self._actions.get(action)
        act(config)

    def login(self, config: Config):
        path: str = 'android/mobileLogin_744'
        params: dict = {
            'mobilephone': config.mobilephone,
            'password': config.password,
            'deviceType': '2',
            'detail': '机型：{platform} / 系统版本：{version}'.format(platform=platform(), version='13.1.2')
        }
        print(params)
        target = url_for(path=path)
        resp = session.post(target, params)
        result = resp.json()
        user_config.token = result.get('token')
        user_config.signature = result['user']['signature']
        user_config.email = result['user']['email']
        user_config.mobilephone = result['user']['mobilephone']
        user_config.userId = result['user']['userId']
        user_config.username = result['user']['username']
        print(user_config.username)

    def checkCurrentSign(self):
        path: str = 'mobileAttendance/nearestAttendanceSetting'
        target: str = url_for(path)
        resp = session.get(target)
        result = resp.json()
        print(result)        
    
    def check_in_work(self):
        pass