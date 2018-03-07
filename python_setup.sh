#!/bin/bash
#
# Set up Python 2 and Python 3
# by installing pip.

if [ "$(id -u)" != "0" ]; then
    echo "This script should be run as root."
    exit 1;
fi

wget https://bootstrap.pypa.io/get-pip.py
/usr/bin/python2 get-pip.py
/usr/bin/python3 get-pip.py
/bin/rm -f get-pip.py

apt-get install -y libpython2.7-dev libpython3.5-dev

sudo chown charles:charles /home/charles/.cache
