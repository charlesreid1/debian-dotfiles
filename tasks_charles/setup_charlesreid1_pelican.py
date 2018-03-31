#!/usr/bin/env python3
import os, re
from os.path import join

"""
Setup Charlesreid1.com pelican

This script installs the pelican themes and extensions
needed to generate the charlesreid1 github blog
and the charlesreid1.com static site.

Pelican themes:
    charlesreid1.com-theme
    charlesreid1-githubio-theme

Pelican extensions:
    math?
"""

charlesreid1_base_dir = join(os.env['HOME'],'codes','charlesreid1')

url_to_dir = [ ('https://github.com/getpelican/pelican-plugins.git','pelican-plugins'),
               ('https://charlesreid1.com:3000/charlesreid1/charlesreid1.com-theme.git', 'charlesreid1.com-theme'),
               ('https://charlesreid1.com:3000/charlesreid1/charlesreid1-githubio-theme.git', 'charlesreid1-githubio-theme'),
               ('https://charlesreid1.com:3000/charlesreid1/atom-hammer-theme.git', 'atom-hammer-theme'),
               ('https://charlesreid1.com:3000/charlesreid1/coffin-spore-theme.git', 'coffin-spore-theme')
               ]

print("")
print("setup charlesreid1.com pelican")
print("------------------------------")
print("")

for i,_url,_dir in enumerate(url_to_dir):
    print(" - Cloning %s into %s"%(_url,_dir))
    clonedir = join(charlesreid1_base_dir,_dir)
    clonecmd = ['git','clone',_url,clonedir]
    subprocess.call(clonecmd, cwd=charlesreid1_base_dir)

    if(i>0):
        print(" - Installing pelican theme %s"%(_dir))
        installcmd = ["pelican-themes","-U",_dir]
        subprocess.call(installcmd, cwd=charlesreid1_base_dir)


