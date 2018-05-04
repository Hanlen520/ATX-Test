#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# extention for http://gt.qq.com/
# reference doc http://gt.qq.com/docs/a/UseGtWithBroadcast.txt
# GT3.1 supported


import functools
from logzero import logger
import time
import zipfile
import os
import re


class GT(object):
    def __init__(self, d):
        self.d = d
        self._broadcast = functools.partial(self.d.adb_shell, 'am', 'broadcast', '-a', )
        # self._package_name = None

    def start_test(self, package_name, cpu=True, net=True, pss=True, jif=False, pri=False, fps=False):
        '''
        :param package_name: 被测app包名
        :param cpu: 开启CPU采集
        :param net: 开启NET网络采集
        :param pss: 开启PSS内存采集
        :param jif: 开启CPU时间片采集
        :param pri: 开启PrivateDirty采集
        :param fps: 开启FPS采集
        :return:
        '''
        pkgs = re.findall('package:([^\s]+)', self.d.adb_shell('pm', 'list', 'packages', '-3'))
        if package_name in pkgs:
            if 'com.tencent.wstt.gt' in pkgs:
                # self._package_name = package_name
                broadcast = self._broadcast
                # 1. start app
                self.clean_data()  # clean old data

                logger.info('Stopping all running app')
                self.d.app_stop_all()
                logger.info('Starting GT Test')
                self.d.app_start('com.tencent.wstt.gt')  # 'com.tencent.wstt.gt.activity.GTMainActivity')
                time.sleep(4)

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
                time.sleep(2)
                self.d.app_start(package_name)
            else:
                raise Exception("GT App not installed, please install first!!!")
        else:
            raise Exception("There is no package named %s" % package_name)

    def stop_test(self, zip=True):
        '''
        停止测试，备份测试数据、关闭GT、执行导出js的自动化脚本、执行Pull 将data.js 复制到电脑
        :param zip: 是否将报告文件夹压缩成zip 默认Ture
        :return:
        '''
        self._broadcast('com.tencent.wstt.gt.baseCommand.endTest')
        self.quit()
        self.backup_data()
        logger.info('Testing finished>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        self.d.app_stop_all()
        self.export_data()
        if zip:
            _zip_report()
        else:
            pass


    def backup_data(self):
        '''备份GTR文件到GTR_Backup'''
        # self._broadcast('com.tencent.wstt.gt.baseCommand.exportData', '--es', 'saveFolderName', '/sdcard/GTR_Backup/')
        self.d.adb_shell('cp -r sdcard/GTR/. sdcard/GTR_Backup/')
        logger.info('Backup /GTR/ to /GTR_Backup/ success')

    def clean_data(self):
        '''清除GTR文件'''
        # self._broadcast('com.tencent.wstt.gt.baseCommand.clearData')
        self.d.adb_shell('rm -r sdcard/GTR')
        self.d.adb_shell('rm -r sdcard/GTRData/data.js')
        logger.info('Clearing GTR file and data.js')


    def quit(self):
        '''结束GT并退出'''
        self._broadcast('com.tencent.wstt.gt.baseCommand.exitGT')
        self.d.app_stop('com.tencent.wstt.gt')
        logger.info('Exiting GT and stop GT App')

    def export_data(self):
        '''导出js文件的UI自动化脚本,并pull到data.js到电脑'''
        logger.info('Starting launch GT to export json data')
        self.d.adb_shell('rm -r sdcard/GTRData/data.js')
        self.d.app_start('com.tencent.wstt.gt')
        self.d(resourceId="com.tencent.wstt.gt:id/button_pulldata").click()
        self.d(resourceId="android:id/button2").click()
        filename = self.d(resourceId="com.tencent.wstt.gt:id/textView").get_text()
        self.d(resourceId="com.tencent.wstt.gt:id/textView").click()
        self.d(resourceId="android:id/button1").click()
        time.sleep(0.2)  # 点击确定后需要sleep一下才会捕捉到progress
        f = self.d(resourceId="com.tencent.wstt.gt:id/textView").wait(timeout=1800.0)  # 等待导出结束，最长30分钟
        if f:
            if 'data' in self.d.adb_shell('ls /sdcard/GTRData/'):
                logger.info('%s exported data success' % filename)
                self.pull_js()
                time.sleep(3)
                self.d.app_stop_all()
            else:
                logger.error('There is no data.js in /sdcard/GTRData!\n Please check data.js manually!')
        else:
            logger.error('%s exported Failed\n Please Export data.js manually! ' % filename)

    def pull_js(self, dst='../GT_Report/data/data.js'):
        '''将手机内的data.js复制到电脑'''
        if 'data' in self.d.adb_shell('ls /sdcard/GTRData/'):
            logger.info('Starting to pull data.js to %s ' % os.path.abspath(dst))
            self.d.pull('/sdcard/GTRData/data.js', dst)
            logger.info('Pull data.js success')
            return True
        else:
            raise Exception('There is no data.js in /sdcard/GTRData/!  Please check out!')

    # def unlock_devices(self):
    #     '''../apk/unlock.apk install and launch'''
    #     pkgs = re.findall('package:([^\s]+)', self.d.adb_shell('pm', 'list', 'packages', '-3'))
    #     if 'io.appium.unlock' in pkgs:
    #         self.d.app_start('io.appium.unlock')
    #         self.d.adb_shell('input keyevent 3')
    #     else:
    #         #  appium unlock.apk 下载安装
    #         self.d.app_install('https://raw.githubusercontent.com/pengchenglin/ATX-Test/master/apk/unlock.apk')
    #         self.d.app_start('io.appium.unlock')
    #         self.d.adb_shell('input keyevent 3')


def _zip_report():
    name = 'GTReport ' + time.strftime("%Y-%m-%d %H.%M.%S", time.localtime())
    startdir = "../GT_Report"  # 要压缩的文件夹路径
    file_news = '../' + name + '.zip'  # 压缩后文件夹的名字
    z = zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED)  # 参数一：文件夹名
    for dirpath, dirnames, filenames in os.walk(startdir):
        fpath = dirpath.replace(startdir, '')  # 这一句很重要，不replace的话，就从根目录开始复制
        fpath = fpath and fpath + os.sep or ''  # 这句话理解我也点郁闷，实现当前文件夹以及包含的所有文件的压缩
        for filename in filenames:
            z.write(os.path.join(dirpath, filename), fpath + filename)
            # z.write(os.path.join(dirpath, filename))
    z.close()
    logger.info('Generate zip_report file successful.\n %s' % os.path.abspath(file_news))


