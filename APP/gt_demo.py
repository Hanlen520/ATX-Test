#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import uiautomator2 as u2
from Pubilc.gt import GT
import os

import time

d = u2.connect()
# d.unlock()
GT(d).start_test('com.quvideo.xiaoying')

# d.adb_shell('monkey --throttle 1000 -s 53 --pct-anyevent 0 --pct-nav 0 --pct-touch 44 -p com.quvideo.xiaoying --pct-motion 30 --pct-trackball 8 --pct-syskeys 8 --pct-majornav 0 --pct-appswitch 10 --pct-flip 0 --monitor-native-crashes -v -v 1000')
# time.sleep(10)
os.system('adb shell monkey --throttle 1000 -s 53 --pct-anyevent 0 --pct-nav 0 --pct-touch 44 -p com.quvideo.xiaoying --pct-motion 30 --pct-trackball 8 --pct-syskeys 8 --pct-majornav 0 --pct-appswitch 10 --pct-flip 0 --monitor-native-crashes -v -v 5000')

GT(d).stop_test('com.quvideo.xiaoying')
# GT(d).pull_js()


