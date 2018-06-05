#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
# sys.path.append(os.path.split(os.path.split(os.path.abspath(''))[0])[0])
sys.path.append('..')

import time
import re

import uiautomator2 as u2
import uiautomator2.ext.htmlreport as htmlreport
from  Public.gt import GT
from Public import devices
from Public.BasePage import BasePage
from Public.ReadConfig import ReadConfig
from Public.Test_data import get_test_data


# u2.DEBUG = True


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
    base_page =BasePage()
    base_page.set_driver('10.0.31.63')
    d = base_page.get_driver()

    print(d.device_info)
    print(d.device_info['serial'])















