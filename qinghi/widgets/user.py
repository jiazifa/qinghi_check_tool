#! -*- coding: utf-8 -*-
import sys
from collections import namedtuple
from typing import Dict, Any, Callable, Optional
from . import Widget
from qinghi.helpers import platform, url_for, session, user_config, header_for
from qinghi.config import Config

AttendInfo = namedtuple('AttendInfo', ['offwork', 'onwork'])

class User(Widget):
    _actions: Dict[str, Any]

    def __init__(self):
        self._actions = {
            'login': self.login,
            'checkin': self.check_in_work,
            'checkout': self.check_out_work,
            'nest': self.checkCurrentSign,
        }

    def action(self, action: str, config: Optional[Config]):
        act: Any = self._actions.get(action)
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

    def checkCurrentSign(self, config: Config) -> AttendInfo:
        self.login(config)
        path: str = 'mobileAttendance/nearestAttendanceSetting'
        target: str = url_for(path)
        resp = session.get(target, headers=header_for())
        result = resp.json()
        info: Dict[str, Any] = result.get('attendanceDouble') or {}
        onwork: bool = True if info['onwork'] else False
        offwork: bool = True if info['offwork'] else False
        attend = AttendInfo(offwork, onwork)
        return attend

    def check_in_work(self, config: Config):
        attend: AttendInfo = self.checkCurrentSign(config)
        if attend.onwork:
            print('已经打卡过了吧？')
            sys.exit(0)
            return
        path: str = 'workCenter/createAttendance_744'
        target: str = url_for(path)
        longitude: str = config.longitude or ""
        latitude: str = config.latitude or ""

        params: Dict[str, Any] = {
            'attendance': {
                'longitude': float(longitude),
                'latitude': float(latitude),
                'attendanceAddress': config.address,
                'type': 'startwork',
            },
            'distance': float(300.8334)
        }
        headers = header_for()
        print(target, headers, params)
        resp = session.post(target, json=params, headers=headers)
        result: Dict[str, Any] = resp.json()
        print(result)
        attendanceId: Optional[int] = result.get('attendanceId')
        attendanceIsLate: bool = result.get('attendanceIsLate') or False
        checked: bool = result.get('result') or False
        if not checked:
            print('已经打卡过了吧？')
        else:
            print('上班打卡成功')
        sys.exit(0)

    def check_out_work(self, config: Config) -> Dict[str, str]:
        self.login(config)
        path: str = 'workCenter/createAttendance_744'
        target: str = url_for(path)
        longitude: str = config.longitude or ""
        latitude: str = config.latitude or ""
        params: Dict[str, Any] = {
            'attendance': {
                'longitude': float(longitude),
                'latitude': float(latitude),
                'attendanceAddress': config.address,
                'type': 'offwork',
            },
            'distance': float(300.8334)
        }
        headers = header_for()
        print(target, headers, params)
        resp = session.post(target, json=params, headers=headers)
        result: Dict[str, Any] = resp.json()
        print(result)
        attendanceId: Optional[int] = result.get('attendanceId')
        checked: bool = result.get('result') or False
        if not checked:
            print('已经打卡过了吧？')
        else:
            print('下班打卡成功')
        sys.exit(0)