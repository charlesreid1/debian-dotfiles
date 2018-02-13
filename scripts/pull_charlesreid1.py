import subprocess
import time
import os
import re
import socket

"""
Pull Charlesreid1.com

This script pulls the latest version of charlesreid1.com
source and the latest wiki edit data.
"""

def pull():

    log_dir  = "/home/charles/.logs/pull_charlesreid1"
    theme_dir = "/home/charles/codes/charlesreid1/charlesreid1.com-theme"
    src_dir = "/www/charlesreid1.com/charlesreid1-src"
    pelican_dir = src_dir+"/pelican"
    output_dir = pelican_dir + "/output"

    try:
        output = ""

        # Ensure log dir exists
        output += subprocess.Popen(["mkdir","-p",log_dir], cwd="/").decode('utf-8')

        # update theme
        output += subprocess.Popen(["git","pull","origin","master"], cwd=theme_dir).decode('utf-8')
        output += subprocess.Popen(["pelican-themes","-U",theme_dir], cwd="/").decode('utf-8')

        # make site
        output += subprocess.Popen(["git","pull","origin","charlesreid1-src"], cwd=src_dir).decode('utf-8')
        output += subprocess.Popen(["pelican","content"], cwd=pelican_dir).decode('utf-8')

        # copy new stie over
        output += subprocess.Popen(["/bin/cp","-r","*","/www/charlesreid1.com/htdocs/."], cwd=output_dir).decode('utf-8')

    except subprocess.CalledProcessError:
        now = datetime.now()
        day = now.date().isoformat()
        hr = re.sub(":","-",now.time().isoformat()[0:8])
        timestamp = day + "_" + hr
        logfile = log_dir+"/"+"logfile_"+timestamp+".log"
        with open(logfile,'w') as f:
            logfile.write(output)


if __name__=="__main__":

    host = socket.gethostname()

    if(host=="rojo"):

        one_day = 24*3600
        while True:
            pull()
            time.sleep(one_day)

    else:

        print("You aren't rojo - you probably didn't mean to run this script!")

