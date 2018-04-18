#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# extention for http://gt.qq.com/
# reference doc http://gt.qq.com/docs/a/UseGtWithBroadcast.txt
# GT3.1 supported


import functools
from logzero import logger
import time


class GT(object):
    def __init__(self, d):
        self.d = d
        self._broadcast = functools.partial(self.d.adb_shell, 'am', 'broadcast', '-a',)
        # self._package_name = None

    def start_test(self, package_name, cpu=True, net=True, pss=True, jif=False,pri=False,fps=False):
        # self._package_name = package_name
        broadcast = self._broadcast
        # 1. start app
        logger.info('Unlock the device')
        self.d.unlock()

        self.quit()  # reset gt

        logger.info('Clear GTR file')
        self.clean_data()  # clean old data

        logger.info('Stopping all running app')
        self.d.app_stop_all()

        logger.info('start GT App')
        self.d.app_start('com.tencent.wstt.gt')     # 'com.tencent.wstt.gt.activity.GTMainActivity')

        # 2. set test package name
        broadcast('com.tencent.wstt.gt.baseCommand.startTest', '--es', 'pkgName', package_name)
        # 3. set collect params
        if cpu:
            broadcast('com.tencent.wstt.gt.baseCommand.sampleData', '--ei', 'cpu', '1')
        if net:
            broadcast('com.tencent.wstt.gt.baseCommand.sampleData', '--ei', 'net', '1')
        if pss:
            broadcast('com.tencent.wstt.gt.baseCommand.sampleData', '--ei', 'pss', '1')
        if jif:
            broadcast('com.tencent.wstt.gt.baseCommand.sampleData', '--ei', 'jif', '1')
        if pri:
            broadcast('com.tencent.wstt.gt.baseCommand.sampleData', '--ei', 'pri', '1')
        if fps:
            broadcast('com.tencent.wstt.gt.baseCommand.sampleData', '--ei', 'fps', '1')

        # 4. switch back to app
        logger.info('GT Setup already, starting GT test......')
        time.sleep(3)
        # self.d.app_start(package_name)

    def stop_test(self, package_name):
        self._broadcast('com.tencent.wstt.gt.baseCommand.endTest', '--es', 'pkgName', package_name)
        logger.info('Back_up GTR file')
        self.backup_data()
        self.quit()
        self.d.app_stop(package_name)
        logger.info('Testing finished')
        self.export_data()
        self.pull_js()

    def backup_data(self):
        self._broadcast('com.tencent.wstt.gt.baseCommand.exportData', '--es', 'saveFolderName', '/sdcard/GTR_Backup/')
        logger.info('Backup Test data')

    def clean_data(self):
        '''Clean old data sdcard/GTR'''
        # self._broadcast('com.tencent.wstt.gt.baseCommand.clearData')
        self.d.adb_shell('rm -r sdcard/GTR')


    def quit(self):
        self._broadcast('com.tencent.wstt.gt.baseCommand.exitGT')
        self.d.app_stop('com.tencent.wstt.gt')

    def export_data(self):
        logger.info('Start to export json data')
        self.d.app_start('com.tencent.wstt.gt')
        self.d(resourceId="com.tencent.wstt.gt:id/button_pulldata").click()
        self.d(resourceId="android:id/button2").click()
        self.d(resourceId="com.tencent.wstt.gt:id/imageView").click()
        self.d(resourceId="android:id/button1").click()
        time.sleep(0.2)
        self.d(resourceId="android:id/progress").wait_gone()
        logger.info('json data exported success')
        time.sleep(5)
        self.quit()

    def pull_js(self, dst='../GT_Report/data/data.js'):
        self.d.pull('/sdcard/GTRData/data.js', dst)
        logger.info('Pull data.js to %s Success' % dst)


