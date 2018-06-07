#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
# sys.path.append(os.path.split(os.path.split(os.path.abspath(''))[0])[0])
sys.path.append('..')

import time
import re

import uiautomator2 as u2
import uiautomator2.ext.htmlreport as htmlreport

from Public.BasePage import BasePage
from Public.ReadConfig import ReadConfig
from Public.Test_data import get_test_data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


# u2.DEBUG = True


def is_toast_exist(driver, text, timeout=30, poll_frequency=0.5):
    """is toast exist, return True or False
    :Agrs:
     - toastmessage   - 页面上看到的toast消息文本内容
     - timeout - 最大超时时间，默认30s
     - poll_frequency  - 间隔查询时间，默认0.5s查询一次
    :Usage:
     is_toast_exist(driver, "toast消息的内容")

    """
    try:
        toast_loc = ("xpath", ".//*[contains(@text,'%s')]" % text)
        WebDriverWait(driver, timeout, poll_frequency).until(
            expected_conditions.presence_of_element_located(toast_loc))
        return True
    except Exception as e:
        print('Cannot find toast \n %s' % e)
        return False

def getActivity(d):
    # packageName=subprocess.check_output('adb shell dumpsys activity top | grep ACTIVITY', shell=True).decode()

    packageName=d.shell('adb shell dumpsys activity top | grep ACTIVITY')[0]
    packageName_list = packageName.split('ACTIVITY')
    packageName = packageName_list[-1]
    packageName = packageName.strip()
    packageName=' '.join(packageName.split(' ')[:1])
    return packageName

if __name__ == '__main__':
    base_page = BasePage()
    # base_page.set_driver('10.0.31.63') # nexus5
    base_page.set_driver('10.0.30.162') # s8
    #
    d = base_page.get_driver()
    # print(d.current_app())
    # print(d.info)
    d.set_fastinput_ime(True)
    # d(resourceId="com.yupaopao.yuer:id/l5").set_text("123456")
    d(description=u'搜索').click()
    ele = d(resourceId="com.sec.android.inputmethod:id/keyboardView")

    # ele =d(resourceId="com.sec.android.inputmethod:id/keyboardView").info['bounds']
    # print(keyboard)
    # def get_key_secrch(ele):
    #     x=ele['left']+3*(ele['right']-ele['left'])/8
    #     y=ele['top']+7*(ele['bottom']-ele['top'])/8
    #     print(x,y)
    #
    #
    # get_key_secrch(ele)
    #
    # x = ele['left'] + 3 * (ele['right'] - ele['left']) / 8
    # y = ele['top'] + 7 * (ele['bottom'] - ele['top']) /
    # d.click(x,y)


    # packageName = d.shell('dumpsys activity top | grep ACTIVITY')[0]
    # packageName1 = d.shell('dumpsys window windows | grep Focused')[0]
    # print(packageName1)
    # # packageName_list = packageName.split('ACTIVITY')
    # print(packageName_list)
    # packageName = packageName_list[-1]
    # print(packageName)
    # packageName = packageName.strip()
    # print(packageName)
    # packageName = ' '.join(packageName.split(' ')[:1])
    # print(packageName)
















