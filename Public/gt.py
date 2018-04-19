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
        self.quit()  # reset gt

        logger.info('Clear GTR file')
        self.clean_data()  # clean old data

        logger.info('Stopping all running app')
        self.d.app_stop_all()

        logger.info('starting GT Test')
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
        '''
        停止测试，备份测试数据、关闭GT和被测app、执行导出js的自动化脚本、执行Pull 将data.js 复制到电脑
        :param package_name: test app package_name
        :return:
        '''
        self._broadcast('com.tencent.wstt.gt.baseCommand.endTest', '--es', 'pkgName', package_name)
        self.backup_data()
        self.quit()
        self.d.app_stop(package_name)
        logger.info('Testing finished>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        self.export_data()


    def backup_data(self):
        '''备份GTR文件到GTR_Backup'''
        # self._broadcast('com.tencent.wstt.gt.baseCommand.exportData', '--es', 'saveFolderName', '/sdcard/GTR_Backup/')
        self.d.adb_shell('cp -r sdcard/GTR/. sdcard/GTR_Backup/')
        logger.info('Backup Test data success')

    def clean_data(self):
        '''清除GTR文件'''
        # self._broadcast('com.tencent.wstt.gt.baseCommand.clearData')
        self.d.adb_shell('rm -r sdcard/GTR')

    def quit(self):
        '''结束GT并退出'''
        self._broadcast('com.tencent.wstt.gt.baseCommand.exitGT')
        self.d.app_stop('com.tencent.wstt.gt')
        logger.info('exitGT and stop GT App')

    def export_data(self):
        '''导出js文件的UI自动化脚本,并pull到data.js到电脑'''
        logger.info('Starting to export json data')
        self.d.app_start('com.tencent.wstt.gt')
        self.d(resourceId="com.tencent.wstt.gt:id/button_pulldata").click()
        self.d(resourceId="android:id/button2").click()
        filename = self.d(resourceId="com.tencent.wstt.gt:id/textView").get_text()
        self.d(resourceId="com.tencent.wstt.gt:id/textView").click()
        self.d(resourceId="android:id/button1").click()
        time.sleep(0.2)  # 点击确定后需要sleep一下才会捕捉到progress
        f = self.d(resourceId="com.tencent.wstt.gt:id/textView").wait(timeout=1800.0)
        if f:
            logger.info('%s exported success' % filename)
            self.pull_js()
            time.sleep(3)
            self.quit()
        else:
            logger.error('%s exported Failed\n Please Export data.js manually ' % filename)


    def pull_js(self, dst='../GT_Report/data/data.js'):
        '''pull /sdcard/GTRData/data.js ../GT_Report/data/data.js '''
        self.d.pull('/sdcard/GTRData/data.js', dst)
        logger.info('Pull data.js to %s Success' % dst)


