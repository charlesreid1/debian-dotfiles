#!/bin/bash

if [ "$(id -u)" != "0" ]; then
    echo ""
    echo ""
    echo "This script should be run as root."
    echo ""
    echo ""
    exit 1;
fi

apt-get install -y \
    aptitude \
    apache \
    build-essential \
    git \
    vim \
    screen \
    tmux \
    tshark \
    tcpdump \
    stunnel \
    wireshark \
    net-tools

apt-get install -y \
    python3 \
    python-dev \
    python-qt4

apt-get install -y \
    golang \
    perl \
    octave \
    gnuplot 

apt-get install -y \
    texlive-full 

apt-get install -y \
    libatlas-dev \
    libpng-dev \
    libfreetype6 \
    libfreetype6-dev \
    libzmq3-dev \
    liblapack-dev \
    build-essential 

apt-get install -y \
    gfortran \
    gcc \
    g++ \
    libc++-dev \
    libstdc++-6-dev

apt autoremove
