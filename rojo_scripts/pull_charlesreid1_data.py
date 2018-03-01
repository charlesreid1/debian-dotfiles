#!/usr/bin/python3
import getpass
import subprocess
import time
import os
import re
import socket

"""
Pull Charlesreid1.com Data
(Rojo)

This script pulls the latest version of 
git, wiki, map, and census data
into charlesreid1.com/data
"""

def pull_charlesreid1_data():

    log_dir  = "/home/charles/.logs/pull_charlesreid1"
    data_dir = "/www/charlesreid1.com/charlesreid1-src/data"

    try:
        output = ""

        # Ensure log dir exists
        output += subprocess.Popen(["mkdir","-p",log_dir], cwd="/").decode('utf-8')

