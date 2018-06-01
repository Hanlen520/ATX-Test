#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding: utf-8
import unittest
import uiautomator2 as u2
import time
from Public.BasePage import BasePage
from Public.Decorator import *
# from Public.Decorator import teardownclass
# from Public.Decorator import setup
# from Public.Decorator import teardown
# from Public.Decorator import testcase


class TestBootStrap(unittest.TestCase, BasePage):
    '''BootStrap demo测试'''
    @classmethod
    @setupclass
    def setUpClass(cls):
        # cls.u = u2.connect()
        # cls.driver.healthcheck()  # 解锁屏幕并启动uiautomator服务
        # hrp = htmlreport.HTMLReport(cls.u, 'report')
        # hrp.patch_click()

        # cls.d = BasePage()
        cls.unlock_device()
        cls.d.app_install('https://npmcdn.com/android-app-bootstrap@latest/android_app_bootstrap/build/outputs/apk/android_app_bootstrap-debug.apk')
        cls.d.make_toast("开始测试", 3)
        cls.d.app_stop("com.github.android_app_bootstrap")
        cls.d.set_fastinput_ime(True)
        # cls.driver.app_stop_all()
        cls.d.app_start("com.github.android_app_bootstrap")  # restart app
        # pass

    @classmethod
    @teardownclass
    def tearDownClass(cls):
        # pass
        cls.d.make_toast("测试结束", 3)
        cls.d.set_fastinput_ime(False)
        # cls.driver.service("uiautomator").stop()  # 停止uiautomator守护程序，允许其他测试框架如 appium 运行
        cls.d.app_stop("com.github.android_app_bootstrap")  # restart app

    @setup
    def setUp(self):

        #
        time.sleep(3)  # 等待首页广告结束
        # pass

    @teardown
    def tearDown(self):

        pass

    @testcase
    def test_01_login(self):
        '''点击登录'''
        self.d(resourceId="com.github.android_app_bootstrap:id/mobileNoEditText").set_text("中文+Test+12345678")
        self.d(resourceId="com.github.android_app_bootstrap:id/codeEditText").set_text("111112")
        self.d(text='Login').click()
        time.sleep(2)


    @testcase
    def test_02_scroll_tableview(self):
        '''弹窗'''
        self.d(resourceId="com.github.android_app_bootstrap:id/imageview").click()
        self.d(resourceId="com.github.android_app_bootstrap:id/list_button").click()
        self.d(text='Alert').click()
        self.d(text='yes').click()
        self.back()

        time.sleep(2)

    @testcase
    def test_03_ZZZZZ(self):
        '''主页、个人 再点login'''
        self.back()
        self.d(text='HOME').click()
        self.d(text='PERSONAL').click()
        self.d(text='Logout').click()
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()
