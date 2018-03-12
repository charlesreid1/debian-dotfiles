#!/usr/bin/python3
import getpass
import subprocess


def install_pyenv():
    user = getpass.getuser()
    if(user=="root"):
        raise Exception("You are root - you should run this script as a normal user.")
    else:
        # Install pyenv 
        pyenvcmd = ["curl","-L","https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer","|","/bin/bash"]
        subprocess.call(pyenvcmd, shell=True)

        # We don't need to add ~/.pyenv/bin to $PATH,
        # it is already done.


if __name__=="__main__":
    install_pyenv()

