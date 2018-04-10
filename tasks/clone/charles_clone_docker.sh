#!/bin/bash

DOCKER="$HOME/codes/docker"
mkdir -p $DOCKER
cd $DOCKER

git clone --recursive https://git.charlesreid1.com/docker/d-mysql.git
git clone             https://git.charlesreid1.com/docker/d-phpmyadmin.git
git clone --recursive https://git.charlesreid1.com/docker/d-mediawiki.git
git clone             https://git.charlesreid1.com/docker/d-charlesreid1-utils.git
git clone             https://git.charlesreid1.com/docker/pod-charlesreid1-wiki.git

