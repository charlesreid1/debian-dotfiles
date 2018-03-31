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

PIP="$HOME/.pyenv/shims/pip"

$PIP install -U --user numpy scipy pandas matplotlib seaborn jupyter ipython
$PIP install -U --user tornado pyzmq pygments pygments pillow 
$PIP install -U --user pelican
$PIP install -U --user virtualenv conda

