#!/bin/bash
# 
# this is where you would add any
# pre-baked public keys.
set -x

yes "y" |  ssh-keygen -f $HOME/.ssh/databot_rsa -t rsa -b 4096 -N ""

