import os
from datetime import date


class GeneralUsage(object):
    @staticmethod
    def date_format():
        today = date.today()
        return '{DAY}.{MONTH}.{YEAR}'.format(DAY=today.day, MONTH=today.month, YEAR=today.year)


class EC2Utils:
    def __init__(self):
        try:
            self.is_ec = os.environ["USER"] in ('ubuntu', 'jenkins')
        except KeyError:
            self.is_ec = False


class CMD:
    def __init__(self, app_name, argv, *args):
        self.arguments = {}
        for value in args:
            self.arguments[value] = False

        print '{LEN}\n{APP}\n{LEN}'.format(LEN='*' * len(app_name), APP=app_name)
        for x in range(1, (len(argv)), 2):
            if argv[x] in self.arguments:
                self.arguments[argv[x]] = argv[x + 1]
