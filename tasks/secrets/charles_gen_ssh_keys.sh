#!/bin/bash
# 
# this is where you would add any
# pre-baked public keys.
set -x

yes | ssh-keygen -f $HOME/.ssh/id_rsa -t rsa -N ''
chmod 700 $HOME/.ssh
touch $HOME/.ssh/authorized_keys
chmod 600 $HOME/.ssh/authorized_keys

