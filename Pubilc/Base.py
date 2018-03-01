#!/usr/bin/env python
# -*- coding: utf-8 -*-
import uiautomator2 as u2
from Pubilc.Devices import Devices

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
            fromX = 0.5*x
            fromY = 0.5*y
            toX = 0.5*x
            toY = 0.25*y
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
            fromX = 0.5*x
            fromY = 0.5*y
            toX = 0.5*x
            toY = 0.75*y
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
            fromX = 0.5*x
            fromY = 0.5*y
            toX = 0.25*x
            toY = 0.5*y
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
            fromX = 0.5*x
            fromY = 0.5*y
            toX = 0.75*x
            toY = 0.5*y
        self._swipe(fromX, fromY, toX, toY, steps)

