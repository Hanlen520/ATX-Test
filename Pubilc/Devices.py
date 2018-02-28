#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from logzero import logger
from Pubilc.ReadConfig import ReadConfig

class Devices:
    def __init__(self):
        self.Devices_LIST = ReadConfig().get_host()+'list'

    def get_devices(self):
        devices = []
        value = requests.get(self.Devices_LIST).json()
        # print(value[1])
        for v in value:
            if v["present"] == True:
                devices.append(v)
            elif v["present"] == False:
                logger.info('Devices %s is offline' % v['udid'])
            else:
                logger.error(Exception)
        for i in devices:
            logger.info('Online devices is : %s' % i["udid"])
        return devices

    def handle_devices(self,udid):
        url = ReadConfig().get_host()+'devices/'+udid+'/shell'
        data = {'command': ReadConfig().get_command()}
        logger.info('handling device >>>>>>  %s' % udid)
        response = requests.post(url, data)
        return response.text

    def device_shell(self,udid,command):
        url = ReadConfig().get_host() + 'devices/' + udid + '/shell'
        data = {'command': command}
        logger.info('device shell : >>>>>>  %s' % command)
        response = requests.post(url,data)
        return response.text



if __name__ == '__main__':
    drivers = Devices().get_devices()
    print(drivers)
    print(Devices().handle_devices(drivers[1]['udid']))