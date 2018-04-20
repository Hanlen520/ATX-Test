#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
import os
import uiautomator2 as u2
from Public.atx_server import ATX_Server
from Public.gt import GT
import time

# a = ATX_Server('http://10.0.34.223:8000/')
# print(a.model_devices('SM-G950F')[0]['ip'])
# d = u2.connect(a.model_devices('SM-G950F')[0]['ip'])

d = u2.connect()
d.open_identify(theme='red')

GT(d).start_test('com.quvideo.xiaoying')

os.system('adb shell monkey --throttle 1000 -s 53 --pct-anyevent 0 --pct-nav 0 --pct-touch 44 -p com.quvideo.xiaoying --pct-motion 30 --pct-trackball 8 --pct-syskeys 8 --pct-majornav 0 --pct-appswitch 10 --pct-flip 0 --monitor-native-crashes -v -v 10000')
d.app_stop('com.quvideo.xiaoying')

GT(d).stop_test()



