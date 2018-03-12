#!/bin/bash
#
# initialize all the dotfiles stuff
# for user charles

DOTFILES="$HOME/codes/dotfiles"
mkdir -p $DOTFILES

DEBIAN="$DOTFILES/debian"
git clone https://charlesreid1.com:3000/dotfiles/debian.git $DEBIAN

cd $DEBIAN/tasks_charles

./pre_bootstrap.sh
./bootstrap.sh -f
./install_pyenv.sh
./python_install.sh
./python_setup.sh
./gen_ssh_keys.sh
./docker_init.sh

