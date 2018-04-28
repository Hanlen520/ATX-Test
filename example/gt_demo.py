#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
import uiautomator2 as u2
from Public.gt import GT
import time


d = u2.connect('10.0.30.162')
GT(d).unlock_devices()
# 开始GT

GT(d).start_test('com.gtr.sdkdemo')
# # os.system('adb shell monkey --throttle 1000 -s 53 --pct-anyevent 0 --pct-nav 0 --pct-touch 44 -p com.quvideo.xiaoying --pct-motion 30 --pct-trackball 8 --pct-syskeys 8 --pct-majornav 0 --pct-appswitch 10 --pct-flip 0 --monitor-native-crashes -v -v 10000')
# # monkey_shell ='CLASSPATH=/sdcard/monkey.jar:/sdcard/framework.jar exec app_process /system/bin tv.panda.test.monkey.Monkey -p com.quvideo.xiaoying --running-minutes 20 --uiautomatormix --throttle 100 -v -v >/sdcard/monkeyout.txt 2>/sdcard/monkeyerr.txt &'
#
time.sleep(10)
#
#
# 结束GT
GT(d).stop_test()



