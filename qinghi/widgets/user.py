#! -*- coding: utf-8 -*-
import sys
from typing import AnyStr, Dict, Any, Callable, Optional
from . import Widget
from qinghi.helpers import platform, url_for, session, user_config, header_for
from qinghi.config import Config


class User(Widget):
    _actions: Dict[AnyStr, Any]

    def __init__(self):
        self._actions = {
            'login': self.login,
            'checkin': self.check_in_work,
            'checkout': self.check_out_work,
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
        target = url_for(path=path)
        resp = session.post(target, params)
        user_config.jsessionid = resp.cookies["JSESSIONID"]
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
        resp = session.get(target, headers=header_for())
        result = resp.json()
        print(result)

    def check_in_work(self, config: Config):
        self.login(config)
        path: str = 'workCenter/createAutomaticSignForAttendance'
        target: str = url_for(path)
        params: Dict[AnyStr, Any] = {
            'attendance': {
                'longitude': float(config.longitude),
                'latitude': float(config.latitude),
                'attendanceAddress': config.address,
                'type': 'startwork',
            },
            'distance': float(300.8334)
        }
        headers = header_for()
        print(target, headers, params)
        resp = session.post(target, json=params, headers=headers)
        result: Dict[AnyStr, Any] = resp.json()
        attendanceId: Optional[int] = result['attendanceId']
        attendanceIsLate: bool = result['attendanceIsLate'] or False
        result: bool = result['result'] or False
        if not result:
            print('已经打卡过了吧？')
        else:
            print('上班打卡成功')
        sys.exit(0)

    def check_out_work(self, config: Config) -> Dict[AnyStr, AnyStr]:
        self.login(config)
        path: str = 'workCenter/createAttendance_744'
        target: str = url_for(path)
        params: Dict[AnyStr, Any] = {
            'attendance': {
                'longitude': float(config.longitude),
                'latitude': float(config.latitude),
                'attendanceAddress': config.address,
                'type': 'offwork',
            },
            'distance': float(300.8334)
        }
        headers = header_for()
        print(target, headers, params)
        resp = session.post(target, json=params, headers=headers)
        result: Dict[AnyStr, Any] = resp.json()
        print(result)
        attendanceId: Optional[int] = result['attendanceId']
        result: bool = result['result'] or False
        if not result:
            print('已经打卡过了吧？')
        else:
            print('下班打卡成功')
        sys.exit(0)