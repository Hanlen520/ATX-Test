#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""
stf devices stf_selector

some fields we often use
===============================================
field	     e.g.
manufacturer OPPO
version      5.1.1
display	     {height:1920，width:1080}
sdk	         22
serial	     778d4f10
platform	 android
mode         Plusm A
....         ...
===============================================
"""

import logging


from tinydb import TinyDB, where
from tinydb.storages import MemoryStorage, JSONStorage
import requests

logger = logging.getLogger(__name__)

TinyDB.DEFAULT_STORAGE = MemoryStorage


class ATX_Server(object):
    """
    According to users requirements to select devices
    """

    def __init__(self, url=None):
        """
        Construct method
        """
        self._db = TinyDB(storage=MemoryStorage)
        self._url = url+'/list'
        self.load()

    def load(self):
        """
        Use the data which got from stf platform to crate query db

        :return: the len of records in the db's table
        """
        res = requests.get(self._url).json()
        if res is not None:
            eids = self._db.insert_multiple(res)
            return len(eids)
        else:
            return 0

    def find(self, cond=None):
        """
        According condition to filter devices and return
        :param cond: condition to filter devices
        :type cond: where
        :return: stf_selector object and its db contains devices
        """
        if cond is not None:
            res = self._db.search(cond)
            self.purge()
            self._db.insert_multiple(res)
        return self

    def devices(self):
        """
        return all devices that meeting the requirement
        :return: list of devices
        """
        return self._db.all()

    def refresh(self):
        """
        reload the devices info from stf
        :return: the len of records in the db's table
        """
        self.purge()
        return self.load()

    def count(self):
        """
        count the records in the db's table
        :return: the len of records in the db's table
        """
        return len(self._db.all())

    def purge(self):
        """
        remove all the data from the db
        :return:
        """
        self._db.purge()

    def ready_devices(self):
        '''标记为ready的设备'''
        self.refresh()
        devices = self.find(where('ready') == True).devices()
        return devices

    def online_devices(self):
        '''online 的设备'''
        self.refresh()
        devices = self.find(where('present') == True).devices()
        return devices

    def model_devices(self, model):
        '''查找特定型号的设备'''
        self.refresh()
        devices = self.find(where('model') == model).devices()
        return devices

    def brand_devices(self, brand):
        '''查找特定品牌的设备'''
        self.refresh()

        devices = self.find(where('brand') == brand).devices()
        return devices

    def sdk_devices(self, sdk):
        '''查找特定SDK的设备'''
        self.refresh()
        devices = self.find(where('sdk') == sdk).devices()
        return devices

    def serial_devices(self, serial):
        '''查找特定serial的设备'''
        self.refresh()
        devices = self.find(where('serial') == serial).devices()
        return devices

# if __name__ == '__main__':
#     url ='http://10.0.34.223:8000/list'
#     s = Selector(url)
#     s.load()
#     conds = (where('version') == '8.0.0')
#     device1 =s.find(conds).devices()
#     print(device1)