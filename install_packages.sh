#!/bin/bash

if [ "$(id -u)" != "0" ]; then
    echo ""
    echo ""
    echo "This script should be run as root."
    echo ""
    echo ""
    exit 1;
fi

apt-get install -y git 
apt-get install -y vim
apt-get install -y screen
apt-get install -y aptitude
apt-get install -y build-essential
apt-get install -y tmux
apt-get install -y tshark
apt-get install -y tcpdump
apt-get install -y curl
apt-get install -y wget
apt-get install -y stunnel
apt-get install -y wireshark
apt-get install -y net-too
apt-get install -y python3
apt-get install -y python-dev
apt-get install -y python-q
apt-get install -y golang
apt-get install -y perl
apt-get install -y octave
apt-get install -y gnuplo
apt-get install -y texlive-ful
apt-get install -y libatlas-dev
apt-get install -y libpng-dev
apt-get install -y libfreetype6
apt-get install -y libfreetype6-dev
apt-get install -y libzmq3-dev
apt-get install -y liblapack-d
apt-get install -y gfortran
apt-get install -y gcc
apt-get install -y g++
apt-get install -y libc++-dev
apt-get install -y libstdc++-6-dev

apt -y autoremove
