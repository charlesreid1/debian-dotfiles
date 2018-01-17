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
else
    pip2 install --user numpy scipy pandas
    pip3 install --user numpy scipy pandas

    pip2 install --user matplotlib seaborn
    pip3 install --user matplotlib seaborn

    pip2 install --user jupyter ipython
    pip3 install --user jupyter ipython

    pip2 install --user tornado pyzmq pygments
    pip3 install --user tornado pyzmq pygments

    pip2 install --user pygments pillow pelican
    pip3 install --user pygments pillow pelican
fi
