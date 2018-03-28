#!/bin/bash
#
# create ssh in the default key location ~/.ssh/id_rsa
# 
# this can be run by the root user
# or by any regular user

ssh-keygen -f $HOME/.ssh/id_rsa -t rsa -N ''
chmod 700 $HOME/.ssh
touch $HOME/.ssh/authorized_keys
chmod 600 $HOME/.ssh/authorized_keys

