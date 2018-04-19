#!/usr/bin/env python
# -*- coding: utf-8 -*-
import uiautomator2 as u2
from Public.Devices import Devices
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage(object):
    # @classmethod
    # def set_driver(cls, dri):
    #     cls.driver = dri
    #
    # def get_driver(self):
    #     return self.driver
    def __init__(self, driver):
        self.driver = driver

    def _get_window_size(self):
        window = self.driver.info
        y = window['displayHeight']
        x = window['displayWidth']
        return x, y

    def _swipe(self, fromX, fromY, toX, toY, steps):
        self.driver.swipe(fromX, fromY, toX, toY, steps)

    def swipe_up(self, element=None, steps=0.05):
        """
        swipe up
        :param element: WebElement of Macaca, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :return: None
        """
        if element:
            x_left, y_up, x_center, y_center, x_right, y_down = self._get_element_size(element)

            fromX = x_center
            fromY = y_center
            toX = x_center
            toY = y_up
        else:
            x, y = self._get_window_size()
            fromX = 0.5 * x
            fromY = 0.5 * y
            toX = 0.5 * x
            toY = 0.25 * y
        self._swipe(fromX, fromY, toX, toY, steps)

    def swipe_down(self, element=None, steps=0.05):
        """
        swipe up
        :param element: WebElement of Macaca, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :return: None
        """
        if element:
            x_left, y_up, x_center, y_center, x_right, y_down = self._get_element_size(element)

            fromX = x_center
            fromY = y_center
            toX = x_center
            toY = y_up
        else:
            x, y = self._get_window_size()
            fromX = 0.5 * x
            fromY = 0.5 * y
            toX = 0.5 * x
            toY = 0.75 * y
        self._swipe(fromX, fromY, toX, toY, steps)

    def swipe_left(self, element=None, steps=0.05):
        """
        swipe up
        :param element: WebElement of Macaca, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :return: None
        """
        if element:
            x_left, y_up, x_center, y_center, x_right, y_down = self._get_element_size(element)

            fromX = x_center
            fromY = y_center
            toX = x_center
            toY = y_up
        else:
            x, y = self._get_window_size()
            fromX = 0.5 * x
            fromY = 0.5 * y
            toX = 0.25 * x
            toY = 0.5 * y
        self._swipe(fromX, fromY, toX, toY, steps)

    def swipe_right(self, element=None, steps=0.05):
        """
        swipe up
        :param element: WebElement of Macaca, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :return: None
        """
        if element:
            x_left, y_up, x_center, y_center, x_right, y_down = self._get_element_size(element)

            fromX = x_center
            fromY = y_center
            toX = x_center
            toY = y_up
        else:
            x, y = self._get_window_size()
            fromX = 0.5 * x
            fromY = 0.5 * y
            toX = 0.75 * x
            toY = 0.5 * y
        self._swipe(fromX, fromY, toX, toY, steps)

    def is_toast_exist(self, toastmessage, timeout=30, poll_frequency=0.5):
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
            WebDriverWait(self.driver, timeout, poll_frequency).until(
                expected_conditions.presence_of_element_located(toast_loc))
            return True
        except:
            return False
