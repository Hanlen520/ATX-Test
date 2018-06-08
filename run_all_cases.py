import sys

sys.path.append('.')
from Public.CaseStrategy import CaseStrategy
from Public.Drivers import Drivers


if __name__ == '__main__':
    cs = CaseStrategy()
    cases = cs.collect_cases(suite=True)
    Drivers().run(cases)
