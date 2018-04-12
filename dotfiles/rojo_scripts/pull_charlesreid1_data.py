#!/usr/bin/python3
import glob
import getpass
import subprocess
import time
import os
import re
import socket

"""
Pull Charlesreid1.com Data
(Rojo)

This script pulls the latest version of 
git, wiki, map, and census data
into charlesreid1.com/data

VERIFIED
"""


def extract_output(cmd, cwd):
    result = subprocess.Popen(cmd, cwd=cwd, stdout=subprocess.PIPE).stdout.read().decode('utf-8')
    return result


def pull_charlesreid1_data():

    log_dir  = "/home/charles/.logs/pull_charlesreid1"
    data_dir = "/www/charlesreid1.com/htdocs/data"

    try:
        output = ""

        # ensure log dir exists
        mkdircmd = ["mkdir","-p",log_dir]
        output += extract_output(mkdircmd, "/")

        # pull to latest 
        gitpullcmd = ["git","pull","origin","master"]
        output += extract_output(gitpullcmd, data_dir)

        # update each submodule
        for direc in glob.glob(data_dir+"/*"):
            if os.path.isdir(direc):

                # pull this submodule
                output += extract_output(gitpullcmd, direc)

                # add it to the list of submodules to update (add commit push)
                addcmd = ["git","add",direc]
                subprocess.call(addcmd, cwd=data_dir)


        # continue updating submodules to latest (add commit push)
        commitcmd = ["git","commit","-a","-m","[SCRIPT] updating submodules to latest"]
        subprocess.call(commitcmd, cwd=data_dir)

        pushcmd = ["git","push","origin","master"]
        subprocess.call(pushcmd, cwd=data_dir)



    except subprocess.CalledProcessError:

        now = datetime.now()
        day = now.date().isoformat()
        hr = re.sub(":","-",now.time().isoformat()[0:8])
        timestamp = day + "_" + hr
        logfile = log_dir+"/logfile_"+timestamp+".log"
        with open(logfile,'w') as f:
            logfile.write(output)

        print("Encountered error: logging to %s"%logfile)


if __name__=="__main__":

    host = socket.gethostname()
    user = getpass.getuser()

    if(host!="rojo"):
        print("You aren't on rojo - you probably didn't mean to run this script!")
    elif(user!="charles"):
        print("You aren't charles - you should run this script as charles!")
    else:
        pull_charlesreid1_data()
