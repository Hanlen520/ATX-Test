#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Public.atx_server import ATX_Server
from Public.atx_server import get_device_ip
from tinydb import where

url ='10.0.34.223:8000'
s = ATX_Server(url)

# print('devices list ------------')
# print(s.devices())
# print('ready devices>>>>>>>>>>>>>>>>>>>>>>')
# print(s.ready_devices())
# print('version 4.4.4 devices >>>>>>>>>>>>>>>>>>')
# print(s.version_devices('4.4.4'))
# print('serial ce051715b2ef600802 device >>>>>>>')
# print(s.serial_devices('ce051715b2ef600802'))
#
# if s.brand_devices('samsung'):
#     print(s.brand_devices('samsung')[0]['ip'])
# else:
#     print('ssssss')
#
# print(s.model_devices('SM-G530H'))
#
# print(s.sdk_devices('19'))

a=s.sdk_devices('18')
print(get_device_ip(a))