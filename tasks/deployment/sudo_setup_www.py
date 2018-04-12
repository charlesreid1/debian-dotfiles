#!/usr/bin/env python3
import getpass
import subprocess
import os, re, socket
from os.path import join


"""
Setup Charlesreid1.com Sudo Tasks #krash

This sets up the directory structure
for various charlesreid1 domains
and their static content.

Each domain has a folder under `/www`:

    /www/
        example.blue
        example.red/
        example.com/

The source directory contains the static content
and pelican files required to generate the site's
content. These files are in the source directory
under the pelican directory:

    /www/
        example.com/
            example.com-src/
                pelican/
                    pelicanconf.py
                    content/
                    output/
            htdocs/
                index.html
                style.css
                ...

The user charles owns all the source directories,
so the user script handles the source directories.

The user www-data must own the htdocs directories,
so the sudo script handles the htdocs directories.
"""


domains = {
        'charlesreid1.blue' : 'https://git.charlesreid1.com/charlesreid1/charlesreid1.com.git',
        'charlesreid1.red'  : 'https://git.charlesreid1.com/charlesreid1/charlesreid1.com.git',
        'charlesreid1.com'  : 'https://git.charlesreid1.com/charlesreid1/charlesreid1.com.git'
}

if socket.gethostname()=="krash":

    user = getpass.getuser()
    if(user!="root"):
        raise Exception("You are not root - this script requires root (chown commands).")
    
    
    for domain in domains:
    
        print("")
        print("set permissions on %s htdocs"%(domain))
        print("-----------------------------")
        print("")


        srcrepo = domains[domain]


        # sudo creates /www/domain.com
        base_dir = join('/www',domain)
        if not os.path.isdir(base_dir):
            mkdircmd = ["mkdir","-p",base_dir]
            print(" - making dir %s"%(base_dir))
            subprocess.call(mkdircmd)
    
        # chown charles:charles /www/domain.com
        permissions = "charles:charles"
        chowncmd = ["chown", permissions, base_dir]
        print(" - setting permissions on %s to %s"%(base_dir,permissions))
        subprocess.call(chowncmd)
    
    
        # sudo creates /www/domain.com/htdocs
    
        # Clone live branch as www-data to /www/domain.com/htdocs
        branch = "gh-pages"
        live_name = 'htdocs'
        live_dir = join('/www',domain,live_name)
        if not os.path.isdir(live_dir):
            sudoclonecmd = ["sudo","-H","-u","www-data","git","clone","--recursive","-b",branch,srcrepo,live_dir]
            print(" - cloning %s into %s"%(srcrepo,live_dir))
            subprocess.call(sudoclonecmd, cwd=base_dir)
    
    
        # charles creates /www/domain.com/domain.com-src
    
        print(" - done.")

