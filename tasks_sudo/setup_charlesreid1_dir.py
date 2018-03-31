#!/usr/bin/env python3
import os, re
from os.path import join

"""
Setup Charlesreid1.com Dir

Creates the /www/ directory,
which contains all the htdocs
and static content for the 
various charlesreid1 domains.
"""

subprocess.call(["mkdir","-p","/www"])
subprocess.call(["chown","-R","charles:charles","/www"])

