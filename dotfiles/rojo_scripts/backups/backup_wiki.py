#!/usr/bin/python3
from datetime import datetime 
import subprocess
import socket


"""
Back Up Charlesreid1.com Wiki

Size: Medium

This script does the following:
- back up wiki dump
- zip wiki files (images, config files, skins, etc.)
"""


def backup_wiki(basedir):

    # create backup dir
    subprocess.call(["mkdir","-p",basedir])
    
    #####################
    # Start specific task
    
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

    # compress wiki files
    wikitar = basedir+"/wiki_files.tar.gz"
    wikidir = "/www/w"
    subprocess.call(["tar","czf",wikitar,wikidir])
    
    # End specific task
    #####################
    
    print("Done backing up wiki to %s"%basedir)


if __name__=="__main__":

    host = socket.gethostname()

    dat = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    if(host=="rojo"):
        basedir = "/junkinthetrunk/backups/wiki_"+dat
        backup_wiki(basedir)
    else:
        raise Exception("You aren't rojo - you probably didn't mean to run this script!")

