#!/usr/bin/python3
import getpass
import subprocess
import glob
import time
import os
import re
import socket
from datetime import datetime
from pprint import pprint


"""
Pull Charlesreid1.com - Rojo

This script pulls the latest version of charlesreid1.com source.
"""


def extract_output(cmd, cwd):
    result = subprocess.Popen(cmd, cwd=cwd, stdout=subprocess.PIPE).stdout.read().decode('utf-8')
    return result


def pull():

    htdocs_dir = "/www/charlesreid1.com/htdocs"
    log_dir   = "/home/charles/.logs/pull_charlesreid1"
    theme_dir = "/home/charles/codes/charlesreid1/charlesreid1.com-theme"
    src_dir = "/www/charlesreid1.com/charlesreid1-src"
    pelican_dir = src_dir+"/pelican"
    output_dir = pelican_dir + "/output"

    try:
        output = ""

        # ensure log dir exists
        mkdircmd = ["mkdir","-p",log_dir]
        output += extract_output(mkdircmd, "/")

        # update theme
        themepullcmd = ["git","pull","origin","master"]
        output += extract_output(themepullcmd, theme_dir)

        pelicanthemescmd = ["pelican-themes","-U",theme_dir]
        output += extract_output(pelicanthemescmd, "/")

        # make site
        gitpullcmd = ["git","pull","origin","charlesreid1-src"]
        output += extract_output(gitpullcmd, src_dir)

        pelicancmd = ["pelican","content"]
        output += extract_output(pelicancmd, pelican_dir)

        everything = glob.glob(output_dir+"/*")
        cpcmd = ["/bin/cp","-r",*everything,htdocs_dir+"/."]
        output += extract_output(cpcmd, output_dir)

        now = datetime.now()
        day = now.date().isoformat()
        hr = re.sub(":","-",now.time().isoformat()[0:8])
        timestamp = day + "_" + hr

        logfile = log_dir+"/SUCCESS_"+timestamp+".log"
        touchcmd = ["touch",logfile]
        subprocess.call(touchcmd)

    except subprocess.CalledProcessError:

        print("Encountered error: logging to %s"%logfile)

        now = datetime.now()
        day = now.date().isoformat()
        hr = re.sub(":","-",now.time().isoformat()[0:8])
        timestamp = day + "_" + hr

        print("Dumping out results")
        print(len(output))
        logfile = log_dir+"/FAIL_"+timestamp+".log"
        with open(logfile,'w') as f:
            f.write(output)


if __name__=="__main__":

    host = socket.gethostname()
    user = getpass.getuser()

    if(host!="rojo"):
        print("You aren't on rojo - you probably didn't mean to run this script!")
    elif(user!="charles"):
        print("You aren't charles - you should run this script as charles!")
    else:
        pull()

