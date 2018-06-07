#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import uiautomator2 as u2
from Public.chromedriver import ChromeDriver   #将chromedriver.py和该脚本放在同一目录下
from Public.BasePage import BasePage

import re
import warnings


base_page = BasePage()
# base_page.set_driver('10.0.31.63')
base_page.set_driver('10.0.30.162')
d = base_page.get_driver()
d.app_stop('com.github.android_app_bootstrap')
d.app_start('com.github.android_app_bootstrap')
d(text='Login').click()
time.sleep(2)
d(text='Baidu').click()
time.sleep(3)

driver = base_page.set_chromedriver()
# driver = base_page.set_chromedriver(activity="com.github.android_app_bootstrap.activity.WelcomeActivity",
#                                     package='com.github.android_app_bootstrap', process='com.github.android_app_bootstrap')
driver.find_element_by_id('index-kw').click()
driver.find_element_by_id('index-kw').send_keys('Python')
time.sleep(3)
driver.find_element_by_id('index-bn').click()
driver.quit()

# ChromeDriver(d).windows_kill()


# def current_app(d):
#     """
#     Return: dict(package, activity, pid?)
#     """
#     # try: adb shell dumpsys activity top
#     _activityRE = re.compile(
#         r'ACTIVITY (?P<package>[^/]+)/(?P<activity>[^/\s]+) \w+ pid=(?P<pid>\d+)'
#     )
#     m = _activityRE.search(d.shell(['dumpsys', 'activity', 'top'])[0])
#     print(d.shell('dumpsys window w | findstr \/ | findstr name='))
#     if m:
#         print('m : %s' % m)
#         return dict(
#             package=m.group('package'),
#             activity=m.group('activity'),
#             pid=int(m.group('pid')))
#
#     # try: adb shell dumpsys window windows
#     _focusedRE = re.compile(
#         'mFocusedApp=.*ActivityRecord{\w+ \w+ (?P<package>.*)/(?P<activity>.*) .*'
#     )
#     m = _focusedRE.search(d.shell(['dumpsys', 'window', 'windows']))
#     print(d.shell(['dumpsys', 'window', 'windows']))
#     if m:
#         print('windows \n %s' % m)
#         return dict(
#             package=m.group('package'), activity=m.group('activity'))
#     # empty result
#     warnings.warn("Couldn't get focused app", stacklevel=2)
#     return dict(package=None, activity=None)
#
#
# if __name__ == '__main__':
#     u = u2.connect()
#     print(u.adb_shell('dumpsys window w | findstr \/ | findstr name='))
#     print(current_app(u))
