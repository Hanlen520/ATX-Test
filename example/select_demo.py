#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Public.ATX_Server import ATX_Server
from Public.ATX_Server import get_device_ip
from tinydb import where
import uiautomator2 as u2
from Public import devices
from multiprocessing import Pool
import time

url = 'http://10.0.34.75:8000/'
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
ip_list = get_device_ip(s.online_devices())
print(ip_list)


def idntiofy_devices(ip):
    d = u2.connect(ip)
    devices.keep_identify(d)

    # print(ip_list)
    # devices_list =[]
    # for ip in ip_list:
    #     devices_list.append(u2.connect(ip))
    # print(devices_list)
    # for d in devices_list:
    #     devices.keep_identify(d)


if __name__ == '__main__':
    ip_list = get_device_ip(s.online_devices())
    print(ip_list)

    # p = Pool(len(ip_list))
    p = Pool(8)
    for i in range(len(ip_list)):
        print(i)
        p.apply_async(idntiofy_devices, args=(ip_list[i],))
        # time.sleep(4)
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
