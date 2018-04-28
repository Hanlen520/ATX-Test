#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Public.atx_server import ATX_Server
from tinydb import where

url ='http://10.0.34.223:8000/list'
s = ATX_Server(url)

print(s.devices())
# print((where('version') == '8.0.0'))
print(s.find(where('ready') == True).devices())
# device_list = s.devices()
# print(device_list)