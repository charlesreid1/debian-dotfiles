#!/usr/bin/python3
from datetime import datetime 
import subprocess


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


dat = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
basedir = "/junkinthetrunk/backups/charlesreid1_"+dat

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

