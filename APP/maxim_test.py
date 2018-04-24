#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Public.Maxim_monkey import Maxim
import uiautomator2 as u2

d = u2.connect()
d.app_stop_all()
cmd = Maxim().command(package='com.tencent.mm', runtime=78, whitelist=True)
print(cmd)
runtime = int(cmd.split('running-minutes ')[1].split(' ')[0])*60
print(runtime)


# Maxim().run_monkey(d, cmd,actions=True,widget_black=True)
# Maxim().clear_env(d)

