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
        value = self.cf.get("ATXSERVER", "command")
        return value

    def get_host(self):
        value = self.cf.get("ATXSERVER", "host")
        return value

    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value

# if __name__ == '__main__':
#     print(ReadConfig().get_command())
#     print(ReadConfig().get_host())