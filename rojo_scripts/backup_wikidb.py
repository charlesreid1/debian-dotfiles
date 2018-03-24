#!/usr/bin/python3
from datetime import datetime 
import subprocess
import socket

"""
Back Up Charlesreid1.com Wiki Database 
"""

def backup_wikidb(basedir):
# create backup dir
    subprocess.call(["mkdir","-p",basedir])

    # load mysql username/password
    with open('rojo.mysql.password','r') as f:
        credentials = f.readlines()
    u = credentials[0].strip()
    p = credentials[1].strip()

    # back up wiki db
    userarg = "--user=%s"%(u)
    pwarg = "--password=%s"%(p)
    dbarg = "--databases"
    adarg = "--add-drop-database"
    dumpcmdbase = ["mysqldump",userarg,pwarg,dbarg,adarg]
    
    wikiargs = "wikidb"
    wikicmd = dumpcmdbase + [wikiargs]

    wikidump = basedir+"/wikidb_dump.sql"
    with open(wikidump,'wb') as f:
        subprocess.call(wikicmd, cwd=basedir, stdout=f)


if __name__=="__main__":

    host = socket.gethostname()

    dat = datetime.now().strftime("%Y-%m-%d_%H-%M")

    if(host=="rojo"):
        basedir = "/junkinthetrunk/backups/wiki_"+dat
        backup_wikidb(basedir)
    else:
        raise Exception("You aren't rojo - you probably didn't mean to run this script!")
