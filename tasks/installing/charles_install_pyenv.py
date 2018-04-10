#!/usr/bin/env python3
import getpass
import os, sys
import subprocess

"""
Install pyenv

This script runs the script that installs pyenv.
It prints some information about what further steps
the user should take to add pyenv to their path
and ensure they are using the pyenv python version 
all the time.

Once you do this, you can install a python version, e.g.,

    pyenv install -s miniconda3-4.3.30

"""

FNULL = open(os.devnull, 'w')

def install_pyenv():
    user = getpass.getuser()
    if(user=="root"):
        raise Exception("You are root - you should run this script as a normal user.")
    else:

        print("installing pyenv...")

        # Install pyenv 
        curlcmd = ["curl","-L","https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer"]
        curlproc = subprocess.Popen(curlcmd, stdout=subprocess.PIPE, stderr=FNULL)
        subprocess.call(["/bin/bash"], stdin=curlproc.stdout, stdout=FNULL, stderr=FNULL)

        print("Done.\n")

        # We don't need to add ~/.pyenv/bin to $PATH,
        # it is already done.
        binpath = os.path.join(os.environ['HOME'],'.pyenv','bin')
        pypath = os.path.join(os.environ['HOME'],'.pyenv','shims')
        syspath = sys.path

        if binpath in syspath:
            print("     ~~*~~ ~~*~~ ~~*~~ SUCCESS! ~~*~~ ~~*~~ ~~*~~\n")
            print("")
            print("     The location of the pyenv binary is: %s"%(binpath))
            print("     This directory is already on your $PATH.")
            print("     You can modify your .bash_profile to change your $PATH.\n")
            print("")
            print("     To start using pyenv immediately, use the pyenv command:")
            print("         $ pyenv install --list")
            print("         $ pyenv install X")
            print("         $ pyenv global X")
            print("         $ eval \"$(pyenv init - )\"")
            print("")
            print("     The location of the python installed by pyenv is: %s"%(pypath))
            print("     The python binary in this directory can be used")
            print("     as a 'pointer' to the current pyenv python version.")

        else:
            print("     *************** NOTICE: FURTHER ACTION NEEDED: ************\n")
            print("")
            print("     The location of the pyenv binary is: %s"%(binpath))
            print("     This directory is not on your $PATH.")
            print("     You should execute the following before calling pyenv:\n")
            print("         export PATH=\"%s:${PATH}\" \n"%(binpath))
            print("     to make this change permanent, add this to your .bash_profile")
            print("     or just run the following command:\n")
            print("         $ echo 'export PATH=\"%s:${PATH}\"' >> ~/.bash_profile"%(binpath))
            print("         $ echo 'eval \"$(pyenv init -)\"' >> ~/.bash_profile")
            print("         $ source ~/.bash_profile\n")
            print("     (This should be set in charlesreid1 dotfiles\n")
            print("")
            print("     Once you have pyenv on your path, you can use the pyenv command:")
            print("         $ pyenv install --list")
            print("         $ pyenv install X")
            print("         $ pyenv global X")
            print("         $ eval \"$(pyenv init - )\"")
            print("")
            print("     The location of the python installed by pyenv is: %s"%(pypath))
            print("     The python binary in this directory can be used")
            print("     as a 'pointer' to the current pyenv python version.")


if __name__=="__main__":
    install_pyenv()

