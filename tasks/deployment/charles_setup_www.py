#!/usr/bin/env python3
import subprocess
import os, re, socket
from os.path import join


"""
Setup Charlesreid1.com User Tasks #krash

This sets up the directory structure
for various charlesreid1 domains
and their static content.

Each domain has a folder under `/www`:

    /www/
        example.blue
        example.red/
        example.com/

Each domain has a source directory and a live 
htdocs directory. The source directory is labeled
with -src and the live directory is called htdocs:

    /www/
        example.com/
            example.com-src/
            htdocs/

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
    if(user=="root"):
        raise Exception("You are root - this script should be run as a regular user!")
    
    
    for domain in domains:
    
        print("")
        print("setup %s htdocs"%(domain))
        print("-----------------------------")
        print("")
    
    
        srcrepo = domains[domain]
    
    
        # sudo creates /www/domain.com
    
    
        # sudo creates /www/domain.com/htdocs
    
    
        # user creates /www/domain.com/domain.com-src
    
        # Clone source branch to /www/domain.com/domain.com-src
        branch = "master"
        base_dir = join('/www',domain)
        src_name = domain+"-src"
        src_dir = join(base_dir,src_name)
        if not os.path.isdir(src_dir):
            sudoclonecmd = ["git","clone","-b",branch,srcrepo,src_dir]
            print(" - cloning %s into %s"%(srcrepo,src_dir))
            subprocess.call(sudoclonecmd, cwd=base_dir)
    
    
        print(" - done.")
    
