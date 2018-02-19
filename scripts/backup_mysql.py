#!/usr/bin/python3
from datetime import datetime 
import subprocess


"""
Back Up Charlesreid1.com

Size: Small

This script does the following:
- back up all MySQL databases
"""


dat = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
basedir = "/junkinthetrunk/backups/mysql_"+dat

# create backup dir
subprocess.call(["mkdir","-p",basedir])

#####################
# Start specific task

# load mysql username/password
with open('rojo.mysql.password','r') as f:
    credentials = f.readlines()
u = credentials[0].strip()
p = credentials[1].strip()

# back up mysql db
userarg = "--user=%s"%(u)
pwarg = "--password=%s"%(p)
dumpcmdbase = ["mysqldump",userarg,pwarg]

allargs = "--all-databases"
alldump = basedir+"/sql_dump.sql"
dumpcmd = dumpcmdbase + [allargs]

wikiargs = "wikidb"
wikidump = basedir+"/wikidb_dump.sql"
wikicmd = dumpcmdbase + [wikiargs]

with open( alldump,'wb') as f:
    subprocess.call(dumpcmd, cwd=basedir, stdout=f)

with open(wikidump,'wb') as f:
    subprocess.call(wikicmd, cwd=basedir, stdout=f)

# End specific task
#####################

print("Done backing up mysql to %s"%basedir)


