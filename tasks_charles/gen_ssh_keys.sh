#!/bin/bash
#
# pass in an argument that is the key location,
# or pass in no arguments to use the default
# key location ~/.ssh/ida_rsa

if [[ "$#" -eq 1 ]]
then
    ssh-keygen -f $1 -t rsa -N ''
else
    ssh-keygen -f $HOME/.ssh/id_rsa -t rsa -N ''
fi

