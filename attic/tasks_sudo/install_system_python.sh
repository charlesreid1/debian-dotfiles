#!/bin/bash
# 
# install a baseline system version of python.
#
# this script is old.
# current approach is to use the pyenv version of python,
# and set up the .bash_profile to do that automatically.

if [ "$(id -u)" != "0" ]; then
    echo ""
    echo ""
    echo "This script should be run as root."
    echo ""
    echo ""
    exit 1;
fi

apt-get install -y python3 
apt-get install -y python3-dev
apt-get install -y libpython3.5-dev

wget https://bootstrap.pypa.io/get-pip.py
/usr/bin/env python3 get-pip.py

sudo chown charles:charles /home/charles/.cache

