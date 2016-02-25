#!/usr/bin/env python

import os
import pexpect
import pty
import re
import select
import signal
import subprocess
import string
import sys
import time

def exit_gracefully(signum, frame):
    signal.signal(signal.SIGINT, original_sigint)
    sys.exit(1)

original_sigint = signal.getsignal(signal.SIGINT)
signal.signal(signal.SIGINT, exit_gracefully)


current_milli_time = lambda: int(round(time.time() * 1000))
starttime= current_milli_time()

proc = subprocess.Popen(['adb', 'shell', 'getevent'], stdout=subprocess.PIPE)

for line in iter(proc.stdout.readline, ""):
    if not line.startswith("/dev/input"):
        continue

    lineSplit = line.split()
    if len(lineSplit) < 4:
        continue

    delay = current_milli_time()-starttime
    if delay / 1000.0 > 0.1:
        print "sleep {0:.1f}".format(delay/1000.0)

    starttime = current_milli_time()

    event = string.replace(lineSplit[0], ":", "")
    x1 = int(lineSplit[1], 16)
    x2 = int(lineSplit[2], 16)
    x3 = int(lineSplit[3], 16)

    print "sendevent " + event + " " + str(x1) + " " + str(x2) + " " + str(x3)

