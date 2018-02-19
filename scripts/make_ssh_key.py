#!/usr/bin/python3
import socket
import subprocess

"""
Make SSH Key

This makes a new public/private key pair.
"""


def make_ssh_key(keydir):

    print("-"*40)
    print("Making 4096-bit RSA key")
    print("keyholder: charlesreid1@gmail.com")
    print("private key: %s/id_rsa"%(keydir))
    print("public key: %s/id_rsa.pub"%(keydir))
    print("-"*40)

    keygencmd = ["ssh-keygen",
                "-f",keydir+"/id_rsa",
                "-t","rsa",
                "-C","\"charlesreid1@gmail.com\"",
                "-N",""]
    subprocess.call(keygencmd)

    agentcmd = ["eval","\"$(ssh-agent -s)\""]
    subprocess.Popen(agentcmd, shell=True)

    addcmd = ["ssh-add",keydir+"/id_rsa"]
    subprocess.call(addcmd)


if __name__=="__main__":

    host = socket.gethostname()

    if(host=="rojo"):
        keydir = "/home/charles/.ssh"
        make_ssh_key(keydir)
    elif(host=="jupiter"):
        keydir = "/home/charles/.ssh"
        make_ssh_key(keydir)
    else:
        raise Exception("You aren't rojo or jupiter - you probably didn't mean to run this script!")

