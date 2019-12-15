#!/bin/python3

import subprocess
import sys

place=input("What place?\n")
place="wttr.in/"+place
subprocess.call(["curl",str(place)]) 

