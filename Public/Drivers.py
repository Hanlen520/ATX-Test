import time

from multiprocessing import Pool
import uiautomator2 as u2
from Public.ATX_Server import ATX_Server
from Public.RunCases import RunCases
from Public.ReportPath import ReportPath
from Public.BasePage import BasePage
from Public.Log import Log
from Public.ReadConfig import ReadConfig
from Public.chromedriver import ChromeDriver
from Public.Test_data import generate_test_data


class Drivers:
    @staticmethod
    def _run_cases(run, cases):
        log = Log()
        log.set_logger(run.get_device()['model'], run.get_path() + '/' + 'client.log')
        log.i('udid: %s', run.get_device()['udid'])

        # set cls.path, it must be call before operate on any page
        path = ReportPath()
        path.set_path(run.get_path())

        # set cls.driver, it must be call before operate on any page
        base_page = BasePage()
        base_page.set_driver(run.get_device()['ip'])

        try:
            # run cases
            run.run(cases)
        except AssertionError as e:
            log.e('AssertionError, %s', e)

    def run(self, cases):
        method = ReadConfig().get_atx_server('method').strip()
        if method == 'host':
            # get ATX-Server Online devices
            devices = ATX_Server(ReadConfig().get_url()).online_devices()
            print('\nThere has %s online devices in ATX-Server' % len(devices))
        elif method == 'devices':
            # get  devices from config devices list
            devices = get_devices()
            print('\nThere has %s  devices alive in config list' % len(devices))
        else:
            raise Exception('Config.ini method illegal:method =%s' % method)

        # generate test data for every devices
        generate_test_data(devices)

        if not devices:
            print('There is no device found')
            return

        print('Starting Run test >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        runs = []
        for i in range(len(devices)):
            runs.append(RunCases(devices[i]))

        # run on every device
        pool = Pool(processes=len(runs))
        for run in runs:
            pool.apply_async(self._run_cases,
                             args=(run, cases,))
        print('Waiting for all runs done........ ')
        pool.close()
        pool.join()
        print('All runs done........ ')
        ChromeDriver.kill()


def get_devices():
    devices_ip = ReadConfig().get_devices()
    print('Getting devices from config devices list %s' % devices_ip)
    devices_list = []
    for i in devices_ip:
        device = u2.connect(i)
        try:
            if device.alive:
                dict_tmp = device.device_info
                dict_tmp['ip'] = i
                devices_list.append(dict_tmp)
            else:
                print('The IP %s device is not alive,please checkout!' % i)
        except Exception as e:
            print('Raise ERR %s\nThe IP %s device is not alive,please checkout!' % (e, i))
    return devices_list


# if __name__ == '__main__':
#
#     print(ATX_Server(ReadConfig().get_url()).online_devices())
#
#     print(get_devices())
#     print(ReadConfig().get_atx_server('method'))

