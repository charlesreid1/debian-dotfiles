#!/bin/bash

if [[ "$HOSTNAME" == "krash" ]]; then
    DOCKER="$HOME/codes/docker"
    mkdir -p $DOCKER
    cd $DOCKER
    
    git clone --recursive https://git.charlesreid1.com/docker/pod-charlesreid1-wiki.git
fi

