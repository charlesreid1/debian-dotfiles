#!/bin/bash
#
# This installs packages for both
# Python2 and Python3 using pip.
#
# Run python_setup.sh first.
#
# ./python_setup.sh
# ./python_install.sh
#

if [ "$(id -u)" == "0" ]; then
    echo "DO NOT RUN THIS AS ROOT" 1>&2
    exit 1;
fi

# Note:
# Once we source ~/.bash_profile,
# the version of python we installed
# will be shimmed, and should also be
# in our path.
source ~/.bash_profile

# Be explicit about pip location, just in case.
PIP="$HOME/.pyenv/shims/pip"

$PIP install -U pelican
$PIP install -U numpy scipy pandas 
$PIP install -U jupyter ipython
$PIP install -U matplotlib seaborn 
$PIP install -U tornado pyzmq pygments pygments pillow 

