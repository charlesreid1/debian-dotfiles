#!/bin/bash

# Get a copy of the dotfiles for charles
BASE="/home/charles"
CODES="$BASE/codes"
DOTFILES="$BASE/codes/dotfiles"
DEBIAN="$BASE/codes/dotfiles/debian"

mkdir -p $DOTFILES
git clone https://charlesreid1.com:3000/dotfiles/debian.git $DEBIAN
cd $DEBIAN
./pre_bootstrap.sh
./bootstrap.sh -f
./install_pyenv.sh
./python_install.sh
./python_setup.sh
./gen_ssh_keys.sh

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

