#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
# sys.path.append(os.path.split(os.path.split(os.path.abspath(''))[0])[0])
sys.path.append('..')
print(sys.path)
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

def zip_report(name):
    startdir = "../GT_Report"  # 要压缩的文件夹路径
    file_news = name + '.zip'  # 压缩后文件夹的名字
    z = zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED)  # 参数一：文件夹名
    for dirpath, dirnames, filenames in os.walk(startdir):
        fpath = dirpath.replace(startdir, '')  # 这一句很重要，不replace的话，就从根目录开始复制
        fpath = fpath and fpath + os.sep or ''  # 这句话理解我也点郁闷，实现当前文件夹以及包含的所有文件的压缩
        for filename in filenames:
            z.write(os.path.join(dirpath, filename), fpath + filename)
            print('压缩成功')
    z.close()


if __name__ == '__main__':
    d = u2.connect()
    # d.app_start('com.github.android_app_bootstrap')
    # d(resourceId="com.github.android_app_bootstrap:id/login_button").click()
    # d(resourceId="com.github.android_app_bootstrap:id/list_button").click()
    # d(resourceId="android:id/text1").click()
    # d(resourceId="android:id/body").wait_gone()
    # print(type(d(resourceId='android:id/message').get_text))
    # print(is_toast_exist(d, 'Hello'))
    # GT(d).backup_data()
    # GT(d).pull_js()
    # filename = d(resourceId="com.tencent.wstt.gt:id/textView").get_text()
    # print(filename)
    print(d.info)
    # d.open_identify(theme='red')
    # os.system('adb install -r D:\\apk\\xdf.android_unlock.apk')
    # time.sleep(5)
    # d.app_start('xdf.android_unlock')
    # d.press("home")
    d.open_identify('red')


