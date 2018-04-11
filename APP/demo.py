#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
# sys.path.append(os.path.split(os.path.split(os.path.abspath(''))[0])[0])
sys.path.append('..')
from logzero import logger
from Pubilc.Devices import Devices
import uiautomator2 as u2
from Pubilc.Base import BasePage

class testdemo(BasePage):
    def __init__(self):
        devices_list = Devices().get_devices()
        # Devices().handle_devices(devices_list[1]['udid'])
        ip = devices_list[1]['ip']
        self.driver = u2.connect(ip)

    def swiptest(self):
        BasePage(self.driver).swipe_up()
        BasePage(self.driver).swipe_down()
        BasePage(self.driver).swipe_left()
        BasePage(self.driver).swipe_right()









if __name__ == '__main__':
    testdemo().swiptest()



#     devices_list = Devices().get_devices()
#
#     Devices().handle_devices(devices_list[0]['udid'])
#
#     ip = devices_list[0]['ip']
    u = u2.connect(ip)

#     print(u.info)
#     u.drag(sx, sy, ex, ey)
    # u.app_start('com.netease.cloudmusic')
    # u(text='私人FM').click()
    # u(description='转到上一层级').click()
    # u(text='每日推荐').click()
    # u(description='转到上一层级').click()
    # u(text='歌单').click()
    # u(description='转到上一层级').click()
    # u(text='排行榜').click()
    # u(description='转到上一层级').click()
    # logger.debug("hello %s", "world")
    # logger.info("info")
    # logger.warning("warn")
    # logger.error("error")


