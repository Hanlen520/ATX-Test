#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
import os
import uiautomator2 as u2
from Public.gt import GT


d = u2.connect()
d.app_start('xdf.android_unlock')
d.unlock()

GT(d).start_test('com.quvideo.xiaoying')

os.system('adb shell monkey --throttle 1000 -s 53 --pct-anyevent 0 --pct-nav 0 --pct-touch 44 -p com.quvideo.xiaoying --pct-motion 30 --pct-trackball 8 --pct-syskeys 8 --pct-majornav 0 --pct-appswitch 10 --pct-flip 0 --monitor-native-crashes -v -v 10000')

GT(d).stop_test('com.quvideo.xiaoying')



