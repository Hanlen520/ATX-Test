#!/usr/bin/env python
# -*- coding: utf-8 -*-
import configparser
import os


proDir = os.path.split(os.path.realpath(__file__))[0]
#将path分割成路径名和文件名
configPath = os.path.join(proDir, "config.ini")
#将多个路径组合后返回

class ReadConfig:
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath, encoding='UTF-8')

    def get_command(self):
        value = self.cf.get("ATXSERVER", "handle")
        return value

    def get_host(self):
        value = self.cf.get("ATXSERVER", "host")
        return value

    def get_devices(self):
        value = self.cf.get("ATXSERVER", "devices")
        return value.split('/')

    def get_apk_url(self):
        value = self.cf.get("APP", "apk_url")
        return value

    def get_pkg_name(self):
        value = self.cf.get("APP", "pkg_name")
        return value

if __name__ == '__main__':
    print(ReadConfig().get_pkg_name())
    print(ReadConfig().get_apk_url())
