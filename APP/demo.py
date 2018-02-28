#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
# sys.path.append(os.path.split(os.path.split(os.path.abspath(''))[0])[0])
sys.path.append('..')
from logzero import logger
from Pubilc.Devices import Devices
import uiautomator2 as u2

if __name__ == '__main__':
    devices_list = Devices().get_devices()

    Devices().handle_devices(devices_list[0]['udid'])

    ip = devices_list[0]['ip']
    u = u2.connect(ip)
    u.app_start('com.netease.cloudmusic')
    u(text='私人FM').click()
    u(description='转到上一层级').click()
    u(text='每日推荐').click()
    u(description='转到上一层级').click()
    u(text='歌单').click()
    u(description='转到上一层级').click()
    u(text='排行榜').click()
    u(description='转到上一层级').click()
    logger.debug("hello %s", "world")
    logger.info("info")
    logger.warning("warn")
    logger.error("error")


