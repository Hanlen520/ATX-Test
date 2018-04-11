#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# extention for http://gt.qq.com/
# reference doc http://gt.qq.com/docs/a/UseGtWithBroadcast.txt
# GT3.1 supported


import functools


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
        self.clean_data()  # clean old data
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
        self.d.app_start(package_name)

    def stop_test(self, package_name):
        self._broadcast('com.tencent.wstt.gt.baseCommand.endTest', '--es', 'pkgName', package_name)
        self.d.app_stop(package_name)
        self.quit()
        self.export_data()
        print(u'请手动打开GT App导出测试数据后，执行')
        print('$ adb pull /sdcard/GTRData/data.js\n将data.js文件传到电脑上')

    def export_data(self):
        self._broadcast('com.tencent.wstt.gt.baseCommand.exportData', '--es', 'saveFolderName', '/sdcard/GTR_Backup/')

    def clean_data(self):
        self.d.adb_shell('rm -r sdcard/GTR')

    def quit(self):
        self._broadcast('com.tencent.wstt.gt.baseCommand.exitGT')

