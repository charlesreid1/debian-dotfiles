#!/usr/bin/env python3
import getpass
import subprocess
import os, re
from os.path import join

"""
Setup Charlesreid1.com Permissions

TODO: check hostname

This sets the permissions of `/wwww/charlesreid1.X/htdocs`
to `www-data:www-data` so we don't get a 403 error.

Note that this complicates the procedure of running 
sudo tasks, then running user tasks, because this task
must be run after the user task taht creates the 
htdocs structure.

We could fix it, but we're going to move to a git webhook 
anyway, so just wait for that.
"""

user = getpass.getuser()
if(user!="root"):
    raise Exception("You are not root - this script requires root (chown commands).")


domains = [ 'charlesreid1.blue',
            'charlesreid1.red' ,
            'charlesreid1.com']

for domain in domains:

    print("")
    print("set permissions on %s htdocs"%(domain))
    print("-----------------------------")
    print("")


    # Create /www/domain.com
    base_dir = join('/www',domain)
    mkdircmd = ["mkdir","-p",base_dir]
    print(" - making dir %s"%(base_dir))
    subprocess.call(mkdircmd)

    # charles owns /www/domain.com
    permissions = "charles:charles"
    chowncmd = ["chown", permissions, base_dir]
    print(" - setting permissions on %s to %s"%(base_dir,permissions))
    subprocess.call(chowncmd)


    # Create /www/domain.com/domain.com-src
    src_name = domain+"-src"
    src_dir = join('/www',domain,src_name)
    mkdircmd = ["mkdir","-p",src_dir]
    print(" - making dir %s"%(src_dir))
    subprocess.call(mkdircmd)

    # charles owns /www/domain.com/domain.com-src
    permissions = "charles:charles"
    chowncmd = ["chown", permissions, src_dir]
    print(" - setting permissions on %s to %s"%(src_dir,permissions))
    subprocess.call(chowncmd)


    # Create /www/domain.com/htdocs
    live_dir = join('/www',domain,'htdocs')
    mkdircmd = ["mkdir","-p",live_dir]
    print(" - making dir %s"%(live_dir))
    subprocess.call(mkdircmd)

    # www-data owns /www/domain.com/htdocs
    permissions = "www-data:www-data"
    chowncmd = ["chown", permissions, live_dir]
    print(" - setting permissions on %s to %s"%(live_dir,permissions))
    subprocess.call(chowncmd)


    print(" - done.")

