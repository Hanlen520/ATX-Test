#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import uiautomator2 as u2
from Pubilc.gt import GT

import time

d = u2.connect('10.0.30.71')
d.unlock()
GT(d).start_test('com.gtr.sdkdemo')

time.sleep(15)

GT(d).stop_test('com.gtr.sdkdemo')
GT(d).pull_js()


