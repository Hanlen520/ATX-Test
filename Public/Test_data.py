#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json
from Public.ReadConfig import ReadConfig

proDir = os.path.split(os.path.realpath(__file__))[0]
#将path分割成路径名和文件名
data_path = os.path.join(proDir, "data.json")


def generate_test_data(devices):
    dict_tmp = {}
    for d in devices:
        print(d['udid'])
        dict_tmp[d['serial']] = {}
        dict_tmp[d['serial']]['user_name'] = ReadConfig().get_testdata('user_name')[devices.index(d)]
        dict_tmp[d['serial']]['password'] = ReadConfig().get_testdata('password')[devices.index(d)]
    with open(data_path, "w") as f:
        json.dump(dict_tmp, f)
        f.close()
    print("测试数据data.js创建完成")


def get_test_data(d):
    with open(data_path, 'r') as f:
        data = json.load(f)
    return data[d.device_info['serial']]