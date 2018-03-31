#!/usr/bin/env python3
import os, re
from os.path import join

"""
Setup Charlesreid1.com htdocs

This sets up the directory structure
for various charlesreid1 domains
and their static content.

Each domain has a folder under `/www`:

    /www/
        example.blue
        example.red/
        example.com/

Each domain has a source and live subdirectory:

    /www/
        example.com/
            charlesreid1-src/
            htdocs/

This script checks out the source git repo into the src dir,
and creates the htdocs directory.

It is left up to the user what to copy from src to htdocs, 
and what to add to htdocs that's not added to src.
"""

srcrepo = 'https://charlesreid1.com:3000/charlesreid1/charlesreid1.com.git'

domains = ['charlesreid1.blue',
           'charlesreid1.red',
           'charlesreid1.com']

for domain in domains:
    
    base_dir = join('/www',domain)

    live_branch = "master"
    src_branch = "charlesreid1-src"

    htdocs_name = 'htdocs'
    htdocs = join(base_dir,htdocs_name)

    src_name = domain+'-src'
    src = join(base_dir,src_name)

    # make htdocs dir
    if not os.path.isdir(htdocs):
        mkdircmd = ["mkdir","-p",htdocs]
        subprocess.call(mkdircmd, cwd=base_dir)

    # make charlesreid1.blue-src dir
    if not os.path.isdir(src):
        clonecmd = ["git","clone","-b",branch,srcrepo,src]
        subprocess.call(mkdircmd, cwd=base_dir)


