#!/usr/bin/env python3
import subprocess
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

This script checks out the source git repo into the src dir,
and creates the htdocs directory.

It is left up to the user what to copy from src to htdocs, 
and what to add to htdocs that's not added to src.
"""

domains = {
        'charlesreid1.blue' : 'https://charlesreid1.com:3000/charlesreid1/charlesreid1.com.git',
        'charlesreid1.red'  : 'https://charlesreid1.com:3000/charlesreid1/charlesreid1.com.git',
        'charlesreid1.com'  : 'https://charlesreid1.com:3000/charlesreid1/charlesreid1.com.git'
}


for domain in domains:

    srcrepo = domains[domain]

    print("")
    print("setup %s htdocs"%(domain))
    print("-----------------------------")
    print("")


    base_dir = join('/www',domain)
    mkdircmd = ["mkdir","-p",base_dir]
    subprocess.call(mkdircmd)

    src_branch = "master"
    live_branch = "pages"

    src_name = domain+'-src'
    src = join(base_dir,src_name)

    htdocs_name = 'htdocs'
    htdocs = join(base_dir,htdocs_name)

    pelicandir = join(src, 'pelican')
    pelicanoutputdir = join(pelicandir, 'output')


    # make charlesreid1.blue-src dir
    print(" - checking for existing source dir %s"%(src_name))
    if not os.path.isdir(src):
        print("     - no existing source dir found, cloning %s"%(srcrepo))
        clonecmd = ["git","clone","-b", src_branch, srcrepo, src_name]
        subprocess.call(clonecmd, cwd=base_dir)
    else:
        print("     - found existing source dir")

    # make the pelican build target 
    print(" - checking for existing pelican build target")
    if not os.path.isdir(pelicanoutputdir):
        print("     - no existing pelican build target found, cloning %s"%(srcrepo))
        outclonecmd = ["git","clone","--recursive","-b", live_branch, srcrepo, pelicanoutputdir]
        subprocess.call(outclonecmd, cwd=pelicandir)
    else:
        print("     - found existing source dir")

    # make the LIVE htdocs dir
    print(" - checking for live htdocs dir")
    if not os.path.isdir(htdocs):
        print("     - no existing live htdocs dir found, cloning %s"%(srcrepo))
        liveclonecmd = ["git","clone","--recursive","-b", live_branch, srcrepo, htdocs_name]
        subprocess.call(liveclonecmd, cwd=base_dir)
    else:
        print("     - found existing live htdocs dir")

