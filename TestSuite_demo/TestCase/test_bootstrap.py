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


class TestCloudMusic(unittest.TestCase, BasePage):
    @classmethod
    @setupclass
    def setUpClass(cls):
        # cls.u = u2.connect()
        # cls.driver.healthcheck()  # 解锁屏幕并启动uiautomator服务
        # hrp = htmlreport.HTMLReport(cls.u, 'report')
        # hrp.patch_click()

        # cls.driver= BasePage().get_driver()
        cls.driver.app_stop_all()
        # cls.driver.app_stop_all()
        cls.driver.app_start("com.github.android_app_bootstrap")  # restart app
        # pass

    @classmethod
    @teardownclass
    def tearDownClass(cls):
        # pass
        #  cls.driver.make_toast("测试结束", 3)
        # cls.driver = BasePage().get_driver()
        # cls.driver.app_stop_all()
        # cls.driver.service(
        #     "uiautomator").stop()  # 停止uiautomator守护程序，允许其他测试框架如 appium 运行
        pass

    @setup
    def setUp(self):

        #
        time.sleep(5)  # 等待首页广告结束
        # pass

    @teardown
    def tearDown(self):
        self.driver.app_stop("com.github.android_app_bootstrap")  # restart app
        pass

    @testcase
    def testPrivateFM(self):  # 私人FM
        self.driver(text='Login').click()


    @testcase
    def testRecommendEveryday(self):  # 每日推荐
        self.driver(text='Login').click()
        self.driver(text='Baidu').click()

    @testcase
    def testZZZZZ(self):  # 每日推荐
        self.driver(text='Login').click()

        self.driver(text='HOME').click()
        self.driver(text='PERSONAL').click()
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()
