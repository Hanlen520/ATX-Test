import time

from multiprocessing import Pool
import uiautomator2 as u2
from Public.atx_server import ATX_Server
from Public.RunCases import RunCases
from Public.ReportPath import ReportPath
from Public.BasePage import BasePage
from Public.Log import Log


# from App.PageObject.WizardPage import skip_wizard_to_home


url = '10.0.34.75:8000'

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
            # skip wizard
            # if not into home page will raise AssertionError
            # skip_wizard_to_home()

            # run cases
            run.run(cases)
        except AssertionError as e:
            log.e('AssertionError, %s', e)

    def run(self, cases):
        # get ATX-Server Online devices
        devices = ATX_Server(url).online_devices()

        if not devices:
            print('There is no device online in ATX-Server')
            return

        runs = []
        for i in range(len(devices)):
            runs.append(RunCases(devices[i]))

        # run on every device
        pool = Pool(processes=len(runs))
        for run in runs:
            pool.apply_async(self._run_cases,
                             args=(run, cases,))
            # time.sleep(4)
        print('Waiting for all runs done........ ')
        pool.close()
        pool.join()
        print('All runs done........ ')

