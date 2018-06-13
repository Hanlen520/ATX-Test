#!/usr/bin/env python
# -*- coding: utf-8 -*-


import uiautomator2 as u2
import time
from Public.BasePage import BasePage
from Public.Decorator import *
import unittest


class gt_test(unittest.TestCase, BasePage):
    '''gt ceshi '''
    @classmethod
    @setupclass
    def setUpClass(cls):
        cls.d.app_start("com.tencent.wstt.gt")  # restart app


    @classmethod
    @teardownclass
    def tearDownClass(cls):
        cls.d.app_stop("com.tencent.wstt.gt")  # restart app
        cls.restitute_device()
        cls.d.open_identify()



    @testcase
    def test_export(self):
        # self.d.adb_shell('rm -r sdcard/GTRData/data.js')
        # self.d.app_start('com.tencent.wstt.gt')

        self.d(resourceId="com.tencent.wstt.gt:id/button_pulldata").click()
        self.d(resourceId="android:id/button2").click()
        filename = self.d(resourceId="com.tencent.wstt.gt:id/textView").get_text()
        self.d(resourceId="com.tencent.wstt.gt:id/textView").click()
        self.d(resourceId="android:id/button1").click()
        time.sleep(0.2)  # 点击确定后需要sleep一下才会捕捉到progress
        f = self.d(resourceId="com.tencent.wstt.gt:id/textView").wait(timeout=1800.0)  # 等待导出结束，最长30分钟
        if f:
            if 'data' in self.d.adb_shell('ls /sdcard/GTRData/'):
                print('%s exported data success' % filename)
                # self.pull_js()
                time.sleep(3)
                # self.d.app_stop_all()
            else:
                print('There is no data.js in /sdcard/GTRData!\n Please check data.js manually!')
        else:
            print('%s exported Failed\n Please Export data.js manually! ' % filename)