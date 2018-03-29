#!/bin/bash
#
# initialize all the dotfiles stuff for user 
set -x

DOTFILES="$HOME/codes/dotfiles"
mkdir -p $DOTFILES

DEBIAN="$DOTFILES/debian"
git clone https://charlesreid1.com:3000/dotfiles/debian.git $DEBIAN

cd $DEBIAN/tasks_charles

./pre_bootstrap.sh
(
cd ../
./bootstrap.sh -f
./gen_ssh_keys.sh
)
./install_pyenv.sh
./python_install.sh
./python_setup.sh
./docker_init.sh
./deploy_codes_docker.sh
