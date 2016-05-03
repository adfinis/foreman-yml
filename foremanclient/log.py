class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

LOG_DEBUG = 1
LOG_INFO  = 2
LOG_WARN  = 3
LOG_ERROR = 4


LOGLEVEL = LOG_DEBUG

def log(level, message):
    if (level==1): pf="[{0}{1}{2}]".format("", "DEBUG", "")
    if (level==2): pf="[{0}{1}{2}]".format(bcolors.OKGREEN, "INFO", bcolors.ENDC)
    if (level==3): pf="[{0}{1}{2}]".format(bcolors.WARNING, "WARNING", bcolors.ENDC)
    if (level==4): pf="[{0}{1}{2}]".format(bcolors.FAIL, "ERROR", bcolors.ENDC)
    if level >= LOGLEVEL:
        print("{0} {1}".format(pf, message))
