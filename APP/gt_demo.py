#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
import uiautomator2 as u2
from Public.gt import GT
import time
from Public.Maxim_monkey import Maxim


d = u2.connect()
d.open_identify(theme='red')
# 开始GT
GT(d).start_test('com.quvideo.xiaoying')
# os.system('adb shell monkey --throttle 1000 -s 53 --pct-anyevent 0 --pct-nav 0 --pct-touch 44 -p com.quvideo.xiaoying --pct-motion 30 --pct-trackball 8 --pct-syskeys 8 --pct-majornav 0 --pct-appswitch 10 --pct-flip 0 --monitor-native-crashes -v -v 10000')
# monkey_shell ='CLASSPATH=/sdcard/monkey.jar:/sdcard/framework.jar exec app_process /system/bin tv.panda.test.monkey.Monkey -p com.quvideo.xiaoying --running-minutes 20 --uiautomatormix --throttle 100 -v -v >/sdcard/monkeyout.txt 2>/sdcard/monkeyerr.txt &'
# 运行monkey
command = Maxim().command(package='com.quvideo.xiaoying', runtime=60, mode='uiautomatormix', whitelist=True, throttle=500)
Maxim().run_monkey(d, command)

# 结束GT
GT(d).stop_test()



