#!/bin/bash

if [ "$(id -u)" != "0" ]; then
    echo ""
    echo ""
    echo "This script should be run as root."
    echo ""
    echo ""
    exit 1;
fi

apt-get -y update

apt-get install -y git 
apt-get install -y tinc
apt-get install -y vim
apt-get install -y screen
apt-get install -y aptitude
apt-get install -y build-essential
apt-get install -y tmux
apt-get install -y tcpdump
apt-get install -y curl
apt-get install -y wget
apt-get install -y stunnel
apt-get install -y perl
apt-get install -y imagemagick
#apt-get install -y octave

apt -y autoremove
