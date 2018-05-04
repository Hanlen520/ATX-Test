#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

sys.path.append('..')
import re


def unlock_devices(d):
    '''../apk/unlock.apk install and launch'''
    pkgs = re.findall('package:([^\s]+)', d.adb_shell('pm', 'list', 'packages', '-3'))
    if 'io.appium.unlock' in pkgs:
        d.app_start('io.appium.unlock')
        d.adb_shell('input keyevent 3')
    else:
        #  appium unlock.apk 下载安装
        d.app_install('https://raw.githubusercontent.com/pengchenglin/ATX-Test/master/apk/unlock.apk')
        d.app_start('io.appium.unlock')
        d.adb_shell('input keyevent 3')


def get_current_app(d):
    a = d.adb_shell('dumpsys window windows | grep \/ | grep name=')
    current_app = a.split('name=')[1].split(')')[0]
    return current_app


def keep_identify(d):
    #
    unlock_devices(d)
    d.open_identify(theme='black')
    if 'IdentifyActivity' in get_current_app(d):
        print('%s open identify ok' % d.serial)
    else:
        d.app_start('com.github.uiautomator', '.MainActivity', wait=True, stop=True)
        d.open_identify(theme='black')

