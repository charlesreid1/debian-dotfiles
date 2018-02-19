#!/usr/bin/python3
from datetime import datetime 
import subprocess
import socket


"""
Back Up Bash History

Size: Tiny

This script does the following:
- back up bash history

That's it. No tricky dance moves.
"""


def backup_bashhist(basedir,histfile):
    """
    Backup bash history
    """
    
    # create backup dir 
    subprocess.call(["mkdir","-p",basedir])
    
    #####################
    # Start specific task
    
    subprocess.call(["/bin/cp",histfile,base])
    
    # End specific task
    #####################
    
    print("Done backing up %s to %s"%(histfile,basedir))


if __name__=="__main__":

    host = socket.gethostname()

    dat = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    if(host=="rojo"):
        histfile = "/home/charles/.bash_history"
        basedir = "/junkinthetrunk/backups/bashhist_"+dat
        backup_mysql(basedir,histfile)
    elif(host=="jupiter"):
        histfile = "/home/charles/.bash_history"
        basedir = "/opt/backups/bashhist_"+dat
        backup_mysql(basedir,histfile)
    else:
        raise Exception("You aren't rojo or jupiter - you probably didn't mean to run this script!")

