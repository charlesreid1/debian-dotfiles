#!/usr/bin/python3
from datetime import datetime 
import subprocess
import socket

from backup_mysql import backup_mysql

"""
Back Up Charlesreid1.com

Size: Big

This script does the following:
- back up all MySQL databases
- back up Mediawiki files
- back up Apache files
- back up Nginx files
- back up PHP files
"""


def backup_charlesreid1(basedir):
    """
    Backup charlesreid1.com files
    """
    
    # create backup dir
    subprocess.call(["mkdir","-p",basedir])
    
    #####################
    # Start specific task

    # back up mysql
    backup_mysql(basedir)
    
    # aapache, nginx, php backup
    apachetarget = basedir + "/etc_apache2.tar.gz"
    apacheconf = "/etc/apache2"
    apachecmd = ["tar","czf",apachetarget,apacheconf]
    
    nginxtarget = basedir + "/etc_nginx.tar.gz"
    nginxconf = "/etc/nginx"
    nginxcmd = ["tar","czf",nginxtarget,nginxconf]
    
    phptarget = basedir + "/etc_php.tar.gz"
    phpconf = "/etc/php5"
    phpcmd = ["tar","czf",phptarget,phpconf]
    
    # End specific task
    #####################
    
    print("Done backing up charlesreid1.com to %s"%basedir)


if __name__=="__main__":

    host = socket.gethostname()

    dat = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    if(host=="rojo"):
        basedir = "/junkinthetrunk/backups/charlesreid1_"+dat
        backup_charlesreid1(basedir)
    else:
        raise Exception("You aren't rojo - you probably didn't mean to run this script!")

