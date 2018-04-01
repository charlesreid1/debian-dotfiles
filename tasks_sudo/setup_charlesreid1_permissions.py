#!/usr/bin/env python3
import getpass
import subprocess
import os, re
from os.path import join

"""
Setup Charlesreid1.com Permissions

This sets the permissions of `/wwww/charlesreid1.X/htdocs`
to `www-data:www-data` so we don't get a 403 error.
"""

user = getpass.getuser()
if(user!="root"):
    raise Exception("You are not root - this script requires root (chown commands).")


domains = [
        'charlesreid1.blue',
        'charlesreid1.red' ,
        'charlesreid1.com'
]

for domain in domains:

    print("")
    print("set permissions on %s htdocs"%(domain))
    print("-----------------------------")
    print("")

    base_dir = join('/www',domain)
    live_dir = join('/www',domain,'htdocs')
    permissions = "www-data:www-data"

    print(" - setting permissions on %s to %s"%(live_dir,permissions))
    chowncmd = ["chown","-R",permissions,live_dir]
    subprocess.call(chowncmd)
    print(" - done.")


