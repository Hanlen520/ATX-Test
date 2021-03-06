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
        cls.set_fastinput_ime()
        cls.d.app_stop(pkg_name)
        cls.unlock_device()


    @classmethod
    @teardownclass
    def tearDownClass(cls):
        cls.d.app_stop("com.github.android_app_bootstrap")



    @testcase
    def test_install_apk(self):
        # self.d.app_install(apk_url)
        self.d.app_start(pkg_name)

        time.sleep(3)
        LoginPage.LoginPage().wait_page()
        raise Exception('手动报错')