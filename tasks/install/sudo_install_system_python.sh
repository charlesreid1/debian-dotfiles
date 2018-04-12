#!/bin/bash
# 
# this is probably not even necessary,
# principal version of python is pyenv version,
# but this provides a fallback if pyenv goes haywire.

if [ "$(id -u)" != "0" ]; then
    echo ""
    echo ""
    echo "This script should be run as root."
    echo ""
    echo ""
    exit 1;
fi

apt-get install -y python3 

wget https://bootstrap.pypa.io/get-pip.py
/usr/bin/env python3 get-pip.py

