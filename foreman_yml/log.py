import json

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


LOG_DEBUG = 10
LOG_INFO  = 20
LOG_WARN  = 30
LOG_ERROR = 40

global LOGLEVEL
LOGLEVEL = LOG_INFO


def log(level, message, isjson=False):
    global LOGLEVEL
    if (level == LOG_DEBUG):
        pf = "[{0}{1}{2}]".format("", "DEBUG", "")
    if (level == LOG_INFO):
        pf = "[{0}{1}{2}]".format(bcolors.OKGREEN, "INFO", bcolors.ENDC)
    if (level == LOG_WARN):
        pf = "[{0}{1}{2}]".format(bcolors.WARNING, "WARNING", bcolors.ENDC)
    if (level == LOG_ERROR):
        pf = "[{0}{1}{2}]".format(bcolors.FAIL, "ERROR", bcolors.ENDC)
    if level >= LOGLEVEL:
        if not isjson:
            print("{0} {1}".format(pf, message))
        else:
            print("{0} {1}".format(pf, json.dumps(message,
                                                  sort_keys=True,
                                                  indent=2,
                                                  separators=(',', ': ')
                                                  )))
