#!/bin/bash

DOCKER="$HOME/codes/docker"
mkdir -p $DOCKER
cd $DOCKER

git clone --recursive https://charlesreid1.com:3000/docker/d-mysql.git
cd d-mysql
make
cd ../

git clone https://charlesreid1.com:3000/docker/d-phpmyadmin.git
cd d-phpmyadmin
make
cd ../

git clone --recursive https://charlesreid1.com:3000/docker/d-mediawiki.git
cd d-mediawiki
make
cd ../

git clone https://charlesreid1.com:3000/docker/d-charlesreid1-utils.git

