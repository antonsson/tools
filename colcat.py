#!/usr/bin/python
import sys
import signal
import os

# Reset
ColorOff='\033[0m'       # Text Reset

# Regular Colors
Black='\033[30m'        # Black
Red='\033[31m'          # Red
Green='\033[32m'        # Green
Yellow='\033[33m'       # Yellow
Blue='\033[34m'         # Blue
Purple='\033[35m'       # Purple
Cyan='\033[36m'         # Cyan
White='\033[37m'        # White

# Bold
BBlack='\033[1;30m'       # Black
BRed='\033[1;31m'         # Red
BGreen='\033[1;32m'       # Green
BYellow='\033[1;33m'      # Yellow
BBlue='\033[1;34m'        # Blue
BPurple='\033[1;35m'      # Purple
BCyan='\033[1;36m'        # Cyan
BWhite='\033[1;37m'       # White

# High Intensity
IBlack='\033[90m'       # Black
IRed='\033[91m'         # Red
IGreen='\033[92m'       # Green
IYellow='\033[93m'      # Yellow
IBlue='\033[94m'        # Blue
IPurple='\033[95m'      # Purple
ICyan='\033[96m'        # Cyan
IWhite='\033[97m'       # White

# Bold High Intensity
BIBlack='\033[1;90m'      # Black
BIRed='\033[1;91m'        # Red
BIGreen='\033[1;92m'      # Green
BIYellow='\033[1;93m'     # Yellow
BIBlue='\033[1;94m'       # Blue
BIPurple='\033[1;95m'     # Purple
BICyan='\033[1;96m'       # Cyan
BIWhite='\033[1;97m'      # White

currentColor = ColorOff
ColorArray=[
        Green, IGreen, BGreen,
        #Yellow, IYellow,
        #Red, IRed,
        Blue, IBlue, BBlue,
        Purple, IPurple, BPurple,
        Cyan, ICyan, BCyan,
        White, IWhite, BWhite ]

original_sigint = signal.getsignal(signal.SIGINT)


def exit_gracefully(signum, frame):
    # restore the original signal handler as otherwise evil things will happen
    # in raw_input when CTRL+C is pressed, and our signal handler is not re-entrant
    signal.signal(signal.SIGINT, original_sigint)
    sys.exit(1)

# Main start
signal.signal(signal.SIGINT, exit_gracefully)

while True:
    line = sys.stdin.readline()
    splitArray = " ".join(line.split()).split(' ')
    if len(splitArray) > 5:
        try:
            index = int(splitArray[2]) % len(ColorArray)
            currentColor = ColorArray[index]
        except ValueError:
            currentColor = currentColor

    lineSplit = line.split(': ', 1)
    if len(lineSplit) == 2:
        lineColor = ColorOff
        if " E " in lineSplit[0]:
            lineColor = Red
        elif " W " in lineSplit[0]:
            lineColor = Yellow

        sys.stdout.write(currentColor+lineSplit[0]+ColorOff+": "+lineColor+lineSplit[1]+ColorOff)
    else:
        sys.stdout.write(ColorOff+line)
    #sys.stdout.flush()

