#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Public.Maxim_monkey import Maxim
import uiautomator2 as u2

d = u2.connect()
# d.app_stop_all()
cmd = Maxim().command(package='com.quvideo.xiaoying', runtime=1, throttle=500)

Maxim().run_monkey(d, cmd, actions=True)


