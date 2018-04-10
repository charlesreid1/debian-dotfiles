#!/bin/bash

if [ "$(id -u)" != "0" ]; then
    echo ""
    echo ""
    echo "This script should be run as root."
    echo ""
    echo ""
    exit 1;
fi

usermod -aG docker charles
usermod -aG www-data charles
usermod -aG sudo charles

# allow user charles to sudo without a password
# don't yall burn down the house, now. 
echo "charles ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# https://askubuntu.com/a/192062 
sudo service sudo restart

