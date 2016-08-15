#!/usr/bin/env python

import signal
import subprocess
import sys
import time

ColorOff='\033[0m'  # Text Reset
Red='\033[31m'      # Red
BoldRed='\033[1;31m'# Bold Red
Green='\033[32m'    # Green
Yellow='\033[33m'   # Yellow

def get_pid(packageName):
    pid = ""
    try:
        pidLine = subprocess.check_output(["adb", "shell", "ps", "|", "grep", packageName]).split()
    except:
        return pid

    if len(pidLine) > 1:
        pid = pidLine[1]
    return pid

def exit_gracefully(signum, frame):
    # restore the original signal handler as otherwise evil things will happen
    # in raw_input when CTRL+C is pressed, and our signal handler is not re-entrant
    signal.signal(signal.SIGINT, original_sigint)
    sys.exit(1)

if len(sys.argv) < 2:
    print "package name missing you moron"
    sys.exit(0)

package = sys.argv[1]
pid = get_pid(package)
last_pid_check = time.time()
startProcString = "ActivityManager: Start proc"

original_sigint = signal.getsignal(signal.SIGINT)
signal.signal(signal.SIGINT, exit_gracefully)
popen = subprocess.Popen(["adb", "logcat", "-v", "threadtime"], stdout=subprocess.PIPE)

for line in iter(popen.stdout.readline, ""):
    if pid == "" or time.time() - last_pid_check > 5 or startProcString in line and package in line:
        pid = get_pid(package)
        last_pid_check = time.time()

    lineSplit = line.split()
    if len(lineSplit) > 5 and lineSplit[2] == pid:
        #level = lineSplit[4]
        #if level == "F":
            #sys.stdout.write(BoldRed)
        #if level == "E":
            #sys.stdout.write(Red)
        #elif level == "W":
            #sys.stdout.write(Yellow)

        sys.stdout.write(line)

