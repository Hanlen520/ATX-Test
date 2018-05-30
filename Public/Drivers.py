import time

from multiprocessing import Pool

# from macaca import WebDriver
#
# from Public.Ports import Ports
# from Public.Devices import Devices
# from Public.MacacaServer import MacacaServer
import uiautomator2 as u2
from Public.atx_server import ATX_Server
from Public.RunCases import RunCases
from Public.ReportPath import ReportPath
from Public.BasePage import BasePage
from Public.Log import Log
from Public.LoginStatus import LoginStatus

# from App.PageObject.WizardPage import skip_wizard_to_home


url = '192.168.31.192:8000'

class Drivers:
    @staticmethod
    def _run_cases(run, cases):
        log = Log()
        log.set_logger(run.get_device()['ip'], run.get_path() + '\\' + 'client.log')

        # log.i('platformName: %s', run.get_device()['platformName'])
        log.i('udid: %s', run.get_device()['udid'])
        # log.i('package: %s\n', run.get_device()['package'])
        # log.i('bundleId: %s\n', run.get_device()['bundleId'])

        # init driver
        # print(run.get_device())
        # driver = u2.connect(run.get_device()['ip'])
        # driver = u2.connect()
        # driver.init()

        # set cls.path, it must be call before operate on any page
        path = ReportPath()
        path.set_path(run.get_path())

        # login_status = LoginStatus()
        # login_status.set_status(False)

        # set cls.driver, it must be call before operate on any page
        base_page = BasePage()
        base_page.set_driver(run.get_device()['ip'])

        try:
            # skip wizard
            # if not into home page will raise AssertionError
            # skip_wizard_to_home()

            # run cases
            run.run(cases)
        except AssertionError as e:
            log.e('AssertionError, %s', e)

        # quit driver
        # driver.quit()

    def run(self, cases):
        # read ATX-Server Online devices
        devices = ATX_Server(url).online_devices()

        if not devices:
            print('There is no device online in ATX-Server')
            return

        runs = []
        for i in range(len(devices)):
            print(i)
            runs.append(RunCases(devices[i]))

        # run on every device
        pool = Pool(processes=len(runs))
        for run in runs:
            pool.apply_async(self._run_cases,
                             args=(run, cases,))

            # fix bug of macaca, android driver can not init in the same time
            time.sleep(4)
        print('Waiting for all runs done........ ')
        pool.close()
        pool.join()
        print('All runs done........ ')

        # macaca_server.kill_macaca_server()
