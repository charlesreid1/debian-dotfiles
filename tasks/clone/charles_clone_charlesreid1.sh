#!/bin/bash

if [[ "$HOSTNAME" == "krash" ]]; then
    CHAZ="$HOME/codes/charlesreid1"
    mkdir -p $CHAZ
    cd $CHAZ

    git clone --recursive https://git.charlesreid1.com/charlesreid1/charlesreid1-master.git charlesreid1-master
fi
