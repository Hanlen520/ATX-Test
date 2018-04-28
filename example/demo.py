#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
# sys.path.append(os.path.split(os.path.split(os.path.abspath(''))[0])[0])
sys.path.append('..')

import time
from Public.Devices import Devices
import uiautomator2 as u2
from Public.Base import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Public.gt import GT
import zipfile
import os
import io
from Public.atx_server import ATX_Server
from Public.gt import zip_report
import re

u2.DEBUG = True


def is_toast_exist(driver, toastmessage, timeout=30, poll_frequency=0.5):
    """is toast exist, return True or False
    :Agrs:
     - toastmessage   - 页面上看到的toast消息文本内容
     - timeout - 最大超时时间，默认30s
     - poll_frequency  - 间隔查询时间，默认0.5s查询一次
    :Usage:
     is_toast_exist(driver, "toast消息的内容")

    """
    try:
        toast_loc = ("xpath", ".//*[contains(@text,'%s')]" % toastmessage)
        print(toast_loc)
        WebDriverWait(driver, timeout, poll_frequency).until(
            expected_conditions.presence_of_element_located(toast_loc))
        return True
    except:
        return False



if __name__ == '__main__':
    d = u2.connect()

    pkgs = re.findall('package:([^\s]+)', d.adb_shell('pm', 'list', 'packages', '-3'))
    process_names = re.findall('([^\s]+)$', d.adb_shell('ps'), re.M)
    print(pkgs)
    print(process_names)

    if 'com.macaca.android.testing.test1' in pkgs:
        print("tttttt")
    else:
        print('eeeeee')







