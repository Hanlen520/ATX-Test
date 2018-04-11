#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import uiautomator2 as u2
from Pubilc.gt import GT

import time

d = u2.connect()
d.unlock()
# d.app_stop_all()
GT(d).start_test('com.gtr.sdkdemo', jif=True, pri=True)

time.sleep(10)
#
GT(d).stop_test('com.gtr.sdkdemo')

