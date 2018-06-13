#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding: utf-8


import uiautomator2 as u2
import time
from Public.BasePage import BasePage
from Public.Decorator import *
from PageObject.HomePage import HomePage
from PageObject import LoginPage
from Public.Test_data import get_test_data
import unittest


class TestBootStrap(unittest.TestCase, BasePage):
    '''BootStrap demo测试'''
    @classmethod
    @setupclass
    def setUpClass(cls):
        cls.d.app_start("com.github.android_app_bootstrap")  # restart app
        cls.test_data = get_test_data(cls.d)


    @classmethod
    @teardownclass
    def tearDownClass(cls):
        cls.d.app_stop("com.github.android_app_bootstrap")  # restart app
        cls.set_original_ime()


    @setup
    def setUp(self):
        pass

    @teardown
    def tearDown(self):
        pass

    @testcase
    def test_01_login(self):
        '''登录'''
        LoginPage.LoginPage().wait_page()
        LoginPage.login(self.test_data['user_name'], self.test_data['password'])
        print('登录成功')



    @testcase
    def test_02_show_toast(self):
        '''点击弹窗toast'''
        self.d(resourceId="com.github.android_app_bootstrap:id/imageview").click()
        self.d(resourceId="com.github.android_app_bootstrap:id/list_button").click()
        self.d(text='Toast').click()
        self.d(text='Show Dialog').click()
        self.back()
        self.back()

    @testcase
    def test_03_auto_click_alert(self):
        '''弹窗自动点击测试'''
        self.watch_device()
        self.d(resourceId="com.github.android_app_bootstrap:id/imageview").click()
        self.d(resourceId="com.github.android_app_bootstrap:id/list_button").click()
        self.d(text='Alert').click()
        self.d(text='Show Dialog').click()
        self.back()
        self.d(text='Alert').click()
        self.back()
        self.d(text='Alert').click()

        self.d(text='Show Dialog').click()
        # self.d(text='Show Dialog').click()

        self.unwatch_device()

    @testcase
    def test_04_webview(self):
        '''webview测试 '''
        self.back()
        self.back()
        self.d(text='Baidu').click()
        time.sleep(3)
        driver = self.set_chromedriver()
        driver.find_element_by_id('index-kw').click()
        driver.find_element_by_id('index-kw').send_keys('Python')
        time.sleep(3)
        driver.find_element_by_id('index-bn').click()
        time.sleep(3)
        driver.quit()


    @testcase
    def test_05_Bar_click(self):
        '''主页操作并退出'''
        HomePage().home_click()
        HomePage().baidu_click()
        HomePage().webview_click()
        HomePage().personal_click()
        HomePage().personal_logout_click()

        LoginPage.LoginPage().wait_page()
        time.sleep(3)


    @testcase
    def test_05_login_again(self):
        '''再次登录'''
        LoginPage.LoginPage().login_click()

    @testcase
    def test_06_swipe(self):
        '''swipe 滑动测试'''
        self.d(resourceId="com.github.android_app_bootstrap:id/imageview").click()
        self.d(resourceId="com.github.android_app_bootstrap:id/list_button").click()
        self.d(text='Gesture').click()
        self.swipe_up()
        self.swipe_left()
        self.swipe_down()
        self.swipe_right()

        

