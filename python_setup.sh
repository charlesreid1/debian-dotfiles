#!/bin/bash
#
# Set up Python 2 and Python 3
# by installing pip.

echo "This script should be run as root."

wget https://bootstrap.pypa.io/get-pip.py
/usr/bin/python2 get-pip.py
/usr/bin/python3 get-pip.py
/bin/rm -f get-pip.py
