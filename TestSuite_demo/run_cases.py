import os
import sys

# sys.path.append(os.path.split(os.path.split(os.path.abspath(''))[0])[0])
sys.path.append('..')
from Public.CaseStrategy import CaseStrategy

from Public.Drivers import Drivers


if __name__ == '__main__':
    cs = CaseStrategy()
    cases = cs.collect_cases(suite=False)
    Drivers().run(cases)
