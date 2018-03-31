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

print("")
print("setup charlesreid1.com htdocs")
print("-----------------------------")
print("")

for domain in domains:
    
    base_dir = join('/www',domain)
    mkdircmd = ["mkdir","-p",base_dir]
    subprocess.call(mkdircmd)

    live_branch = "pages"
    src_branch = "master"

    htdocs_name = 'htdocs'
    htdocs = join(base_dir,htdocs_name)

    src_name = domain+'-src'
    src = join(base_dir,src_name)

    # make charlesreid1.blue-src dir
    if not os.path.isdir(src):
        clonecmd = ["git","clone","-b", src_branch, srcrepo, src_name]
        subprocess.call(clonecmd, cwd=base_dir)

    # make charlesreid1.blue-src dir
    if not os.path.isdir(src):
        clonecmd = ["git","clone","-b", live_branch, srcrepo, htdocs_name]
        subprocess.call(clonecmd, cwd=base_dir)


