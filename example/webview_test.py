#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import uiautomator2 as u2
from Public.chromedriver import ChromeDriver   #将chromedriver.py和该脚本放在同一目录下
from Public.BasePage import BasePage

base_page = BasePage()
base_page.set_driver('10.0.31.63')
d = base_page.get_driver()
# d.app_stop('com.github.android_app_bootstrap')
# d.app_start('com.github.android_app_bootstrap')
# d(text='Login').click()
# d(text='Baidu').click()
# time.sleep(3)
driver = ChromeDriver(d).driver()
driver.find_element_by_id('index-kw').click()
driver.find_element_by_id('index-kw').send_keys('Python')
time.sleep(3)
driver.find_element_by_id('index-bn').click()
driver.quit()

ChromeDriver(d).windows_kill()