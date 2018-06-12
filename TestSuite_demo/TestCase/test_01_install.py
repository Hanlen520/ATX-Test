#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uiautomator2 as u2
import time
from Public.BasePage import BasePage
from Public.Decorator import *
from PageObject import LoginPage
import unittest

from Public.ReadConfig import ReadConfig
apk_url = ReadConfig().get_apk_url()
pkg_name = ReadConfig().get_pkg_name()


class apk_install(unittest.TestCase, BasePage):
    @classmethod
    @setupclass
    def setUpClass(cls):

        cls.unlock_device()
        cls.d.make_toast('安装apk', 3)


    @classmethod
    @teardownclass
    def tearDownClass(cls):
        cls.d.make_toast("安装成功", 3)
        cls.d.app_stop("com.github.android_app_bootstrap")  # restart app

    @setup
    def setUp(self):
        pass

    @teardown
    def tearDown(self):
        pass

    @testcase
    def test_install_apk(self):
        '''打开app'''
        # self.d.app_install(apk_url)
        self.d.app_start(pkg_name)
        time.sleep(3)
        LoginPage.LoginPage().wait_page()
        raise Exception('手动报错')

    @testcase
    def test_okok(self):
        '''okok
        jsjkdj'''
        a=1
        b=2
        self.assertEqual(a,b)

    @testcase
    def test_opppp(self):
        '''ooooooooo
        好的按时付款杰拉德看风景
        爱是看得见'''
        self.assertEqual(oooo)