#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
# sys.path.append(os.path.split(os.path.split(os.path.abspath(''))[0])[0])
sys.path.append('..')

from Pubilc.Devices import Devices
import uiautomator2 as u2
from Pubilc.Base import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class testdemo(BasePage):
    def __init__(self):
        devices_list = Devices().get_devices()
        # Devices().handle_devices(devices_list[1]['udid'])
        ip = devices_list[1]['ip']
        self.driver = u2.connect(ip)

    def swiptest(self):
        BasePage(self.driver).swipe_up()
        BasePage(self.driver).swipe_down()
        BasePage(self.driver).swipe_left()
        BasePage(self.driver).swipe_right()


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
    # d.app_start('com.github.android_app_bootstrap')
    # d(resourceId="com.github.android_app_bootstrap:id/login_button").click()
    # d(resourceId="com.github.android_app_bootstrap:id/list_button").click()
    # d(resourceId="android:id/text1").click()
    d(resourceId="com.github.android_app_bootstrap:id/alert_button").click()
    print(is_toast_exist(d, 'Hello'))





