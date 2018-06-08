import os
import time

import uiautomator2 as u2
from uiautomator2 import UiObjectNotFoundError
import re
import warnings

from Public.chromedriver import ChromeDriver
from Public.Ports import Ports


# u2.DEBUG = True

class BasePage(object):
    @classmethod
    def set_driver(cls, dri):
        cls.d = u2.connect(dri)

    def get_driver(self):
        return self.d

    # def current_app(self):
    #     """
    #     Return: dict(package, activity, pid?)
    #     """
    #     # try: adb shell dumpsys activity top
    #     _activityRE = re.compile(
    #         r'(?P<package>[^/]+)/(?P<activity>[^/\s]+) \w+ pid=(?P<pid>\d+)'
    #     )
    #     # m1=self.shell('dumpsys activity top | grep ACTIVITY')[0].split('ACTIVITY')[-1].strip()
    #     m = _activityRE.search(self.d.shell('dumpsys activity top | grep ACTIVITY')[0].split('ACTIVITY')[-1].strip())
    #     if m:
    #         return dict(
    #             package=m.group('package'),
    #             activity=m.group('activity'),
    #             pid=int(m.group('pid')))
    #
    #     # try: adb shell dumpsys window windows
    #     _focusedRE = re.compile(
    #         'mFocusedApp=.*ActivityRecord{\w+ \w+ (?P<package>.*)/(?P<activity>.*) .*'
    #     )
    #     m = _focusedRE.search(self.d.shell('dumpsys window windows | grep Focused')[0])
    #     if m:
    #         return dict(
    #             package=m.group('package'), activity=m.group('activity'))
    #     # empty result
    #     warnings.warn("Couldn't get focused app", stacklevel=2)
    #     return dict(package=None, activity=None)
    @classmethod
    def unlock_device(cls):
        '''unlock.apk install and launch'''
        pkgs = re.findall('package:([^\s]+)', cls.d.shell(['pm', 'list', 'packages', '-3'])[0])
        if 'io.appium.unlock' in pkgs:
            cls.d.app_start('io.appium.unlock')
            cls.d.shell('input keyevent 3')
        else:
            #  appium unlock.apk 下载安装
            print('installing io.appium.unlock')
            cls.d.app_install('https://raw.githubusercontent.com/pengchenglin/ATX-Test/master/apk/unlock.apk')
            cls.d.app_start('io.appium.unlock')
            cls.d.shell('input keyevent 3')

    def back(self):
        '''点击返回'''
        self.d.press('back')

    def set_chromedriver(self, device_ip=None, package=None, activity=None, process=None):
        driver = ChromeDriver(self.d, Ports().get_ports(1)[0]).\
            driver(device_ip=device_ip, package=package, attach=True, activity=activity, process=process)
        return driver

    def _get_window_size(self):
        window = self.d.window_size()
        x = window[0]
        y = window[1]
        return x, y

    @staticmethod
    def _get_element_size(element):
        # rect = element.info['visibleBounds']
        rect = element.info['bounds']
        print(rect)
        x_center = (rect['left'] + rect['right']) / 2
        y_center = (rect['bottom'] + rect['top']) / 2
        x_left = rect['left']
        y_up = rect['top']
        x_right = rect['right']
        y_down = rect['bottom']

        return x_left, y_up, x_center, y_center, x_right, y_down

    def _swipe(self, fromX, fromY, toX, toY, steps):
        self.d.swipe(fromX, fromY, toX, toY, steps)

    def swipe_up(self, element=None, steps=0.2):
        """
        swipe up
        :param element: UI element, if None while swipe window of phone
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
            toY = 0.2 * y

        self._swipe(fromX, fromY, toX, toY, steps)

    def swipe_down(self, element=None, steps=0.2):
        """
        swipe down
        :param element: UI element, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :return: None
        """
        if element:
            x_left, y_up, x_center, y_center, x_right, y_down = self._get_element_size(element)

            fromX = x_center
            fromY = y_center
            toX = x_center
            toY = y_down
        else:
            x, y = self._get_window_size()
            fromX = 0.5 * x
            fromY = 0.5 * y
            toX = 0.5 * x
            toY = 0.8 * y

        self._swipe(fromX, fromY, toX, toY, steps)

    def swipe_left(self, element=None, steps=0.2):
        """
        swipe left
        :param element: UI element, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :return: None
        """
        if element:
            x_left, y_up, x_center, y_center, x_right, y_down = self._get_element_size(element)
            fromX = x_center
            fromY = y_center
            toX = x_left
            toY = y_center
        else:
            x, y = self._get_window_size()
            fromX = 0.5 * x
            fromY = 0.5 * y
            toX = 0.2 * x
            toY = 0.5 * y
        self._swipe(fromX, fromY, toX, toY, steps)

    def swipe_right(self, element=None, steps=0.2):
        """
        swipe right
        :param element: UI element, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :return: None
        """
        if element:
            x_left, y_up, x_center, y_center, x_right, y_down = self._get_element_size(element)
            fromX = x_center
            fromY = y_center
            toX = x_right
            toY = y_center
        else:
            x, y = self._get_window_size()
            fromX = 0.5 * x
            fromY = 0.5 * y
            toX = 0.8 * x
            toY = 0.5 * y
        self._swipe(fromX, fromY, toX, toY, steps)

    def _find_element_by_swipe(self, direction, value, element=None, steps=0.5, max_swipe=6):
        """
        :param direction: swip direction exp: right left up down
        :param value: The value of the UI element location strategy. exp: d(text='Logina')
        :param element: UI element, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :param max_swipe: the max times of swipe
        :return: UI element
        """
        times = max_swipe
        for i in range(times):
            try:
                if value.exists:
                    return value
                else:
                    raise UiObjectNotFoundError
            except UiObjectNotFoundError:
                if direction == 'up':
                    self.swipe_up(element=element, steps=steps)
                elif direction == 'down':
                    self.swipe_down(element=element, steps=steps)
                elif direction == 'left':
                    self.swipe_left(element=element, steps=steps)
                elif direction == 'right':
                    self.swipe_right(element=element, steps=steps)
                if i == times - 1:
                    raise UiObjectNotFoundError

    def find_element_by_swipe_up(self, value, element=None, steps=0.2, max_swipe=6):
        return self._find_element_by_swipe('up', value,
                                           element=element, steps=steps, max_swipe=max_swipe)

    def find_element_by_swipe_down(self, value, element=None, steps=0.2, max_swipe=6):
        return self._find_element_by_swipe('down', value,
                                           element=element, steps=steps, max_swipe=max_swipe)

    def find_element_by_swipe_left(self, value, element=None, steps=0.2, max_swipe=6):
        return self._find_element_by_swipe('left', value,
                                           element=element, steps=steps, max_swipe=max_swipe)

    def find_element_by_swipe_right(self, value, element=None, steps=0.2, max_swipe=6):
        return self._find_element_by_swipe('right', value,
                                           element=element, steps=steps, max_swipe=max_swipe)

