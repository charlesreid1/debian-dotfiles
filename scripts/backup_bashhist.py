#!/usr/bin/python3
from datetime import datetime 
import subprocess


"""
Back Up Bash History

Size: Tiny

This script does the following:
- back up bash history

That's it. No tricky dance moves.
"""


dat = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
basedir = "/junkinthetrunk/backups/bashhist_"+dat

# create backup dir 
subprocess.call(["mkdir","-p",basedir])

#####################
# Start specific task

subprocess.call(["/bin/cp","/home/charles/.bash_history",base])

# End specific task
#####################

print("Done backing up charlesreid1.com to %s"%basedir)

