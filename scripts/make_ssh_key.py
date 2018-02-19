#!/usr/bin/python3


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
                "-t","rsa",
                "-b","4096",
                "-C","\"charlesreid1@gmail.com\"",
                "-P","\"\"",
                "-f",keydir+"/.id_rsa"]

    subprocess.call(keygencmd)

    agentcmd = ["eval","\"$(ssh-agent -s)\""]
    subprocess.call(agentcmd)

    addcmd = ["ssh-add",keydir+"/.id_rsa"]
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

