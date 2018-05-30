#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding: utf-8
import unittest
import uiautomator2 as u2
import time
import uiautomator2.ext.htmlreport as htmlreport

class TestCloudMusic(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.u = u2.connect()
        # cls.u.healthcheck()  # 解锁屏幕并启动uiautomator服务
        # hrp = htmlreport.HTMLReport(cls.u, 'report')
        # hrp.patch_click()
        cls.u.app_stop("com.github.android_app_bootstrap")

        # cls.u.disable_popups(True)  # 允许自动处理弹出框
        cls.u.make_toast("测试开始", 3)

    @classmethod
    def tearDownClass(cls):
        cls.u.make_toast("测试结束", 3)
        cls.u.app_stop_all()
        cls.u.service(
            "uiautomator").stop()  # 停止uiautomator守护程序，允许其他测试框架如 appium 运行

    def setUp(self):
        self.d = self.u.session("com.github.android_app_bootstrap")  # restart app
        time.sleep(5)  # 等待首页广告结束

    def tearDown(self):
        pass

    def testPrivateFM(self):  # 私人FM
        self.d(text='Login').click()

    def testRecommendEveryday(self):  # 每日推荐
        self.d(text='Baidu').click()

    def testZZZZZ(self):  # 每日推荐
        self.d(text='Login').click()
        self.d(text='Baidu').click()



if __name__ == '__main__':
    unittest.main()

