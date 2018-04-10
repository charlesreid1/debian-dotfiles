#!/usr/bin/env python3
import subprocess
import os

rc = 0 # returncode

print("")
print("Installing conda...")

pyenv = os.path.join(os.environ['HOME'],'.pyenv','bin','pyenv')

rc = subprocess.call([pyenv,"install","-s","miniconda3-4.3.30"])
if(rc!=0):
    raise Exception()

rc = subprocess.call([pyenv,"global","miniconda3-4.3.30"])
if(rc!=0):
    raise Exception()

print("Done installing conda.")
print("")