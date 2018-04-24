#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
import requests
from logzero import logger
from Public.ReadConfig import ReadConfig
from Public.atx_server import ATX_Server
from tinydb import where

# s = ATX_Server(url=ReadConfig().get_host())


class Devices:
    # def get_devices(self):
    #     '''
    #     获取atxserver在线的设备
    #     :return: devices 在线的设备以列表返回
    #     '''
    #     devices = []
    #     value = requests.get(self.list_url).json()
    #     # print(value[1])
    #     for v in value:
    #         if v["present"] == True:
    #             devices.append(v)
    #         elif v["present"] == False:
    #             logger.warning('Devices %s is offline' % v['udid'])
    #         else:
    #             logger.error(Exception)
    #
    #     logger.info('Online devices Number is : %s' % len(devices))
    #     for i in devices:
    #         logger.info('Online devices  : %s' % i["udid"])
    #     return devices

    def ready_devices(self):
        s.load()
        ready_devices = s.find(where('ready') == True).devices()
        return ready_devices

    def online_devices(self):
        s.load()
        online_devices = s.find(where('present') == True).devices()
        return online_devices

    def handle_device(self, device):
        '''
        点亮设备
        :param device:
        :return:response.text
        '''
        url = ReadConfig().get_host() + 'devices/' + device['udid'] + '/shell'
        data = {
            'command': 'input keyevent HOME && am start -W --user 0 -a com.github.uiautomator.ACTION_IDENTIFY -e theme red'}
        logger.info('handling device >>>>>>  %s' % device['udid'])
        response = requests.request("POST", url, data=data)
        return response.text

    def device_shell(self, device, command):
        '''
        :param device:
        :param command: shell command
        :return: response.text
        '''
        url = ReadConfig().get_host() + 'devices/' + device['udid'] + '/shell'
        data = {'command': command}
        logger.info('device[%s] shell : >>>>>>  %s' % (device['udid'], command))
        response = requests.post(url, data)
        return response.text

    def device_info(self, device):
        '''

        :param device:
        :return: 单个设备的信息
        '''
        url = ReadConfig().get_host() + 'devices/' + device['udid'] + '/info'
        device_info = requests.get(url)
        return device_info.text


# if __name__ == '__main__':
#     drivers = Devices().get_devices()
#     # print(drivers)
#     print(Devices().handle_device(drivers[1]))
#     info = Devices().device_info(drivers[1])
#     print(info)
