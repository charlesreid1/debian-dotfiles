#!/usr/bin/python3
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
"""


def extract_output(cmd, cwd):
    result = subprocess.Popen(cmd, cwd=cwd, stdout=subprocess.PIPE).stdout.read().decode('utf-8')
    return result


def pull_charlesreid1_data():

    log_dir  = "/home/charles/.logs/pull_charlesreid1"
    data_dir = "/www/charlesreid1.com/charlesreid1-src/data"

    try:
        output = ""

        # ensure log dir exists
        mkdircmd = ["mkdir","-p",log_dir]
        output += extract_output(mkdircmd, "/")

        # update data
        gitpullcmd = ["git","pull","origin","master"]
        output += extract_output(gitpullcmd, data_dir)


if __name__=="__main__":

    host = socket.gethostname()
    user = getpass.getuser()

    if(host!="rojo"):
        print("You aren't on rojo - you probably didn't mean to run this script!")
    elif(user!="charles"):
        print("You aren't charles - you should run this script as charles!")
    else:
        one_day = 24*3600
        while True:
            pull()
            time.sleep(one_day)

