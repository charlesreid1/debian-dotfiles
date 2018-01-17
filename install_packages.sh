#!/bin/bash

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
    wireshark

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
    libstdc++-6-dev

apt autoremove
