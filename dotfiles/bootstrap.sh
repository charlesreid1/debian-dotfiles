#!/usr/bin/env bash
#
# Installs all dotfiles in this directory
# into the home directory using rsync.
#
# ./bootstrap.sh
# 
# to force:
#
# ./bootstrap.sh -f

git pull origin master;

EXTRA_EXCLUDE=''

function doIt() {
    rsync \
        --exclude ".git/" \
        --exclude "bootstrap.sh" \
        --exclude "scripts" \
        --exclude "rojo_scripts" \
        --exclude "jupiter_scripts" \
        --exclude "blackbeard_scripts" \
        --exclude "krash_scripts" \
        -avh --no-perms . ~;
    source ~/.bash_profile;
}

if [ "$1" == "--force" -o "$1" == "-f" ]; then
    doIt;
else
    read -p "This may overwrite existing files in your home directory. Are you sure? (y/n) " -n 1;
    echo "";
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        doIt;
    fi;
fi;
unset doIt;

if [ -d "${PWD}/${HOSTNAME}_scripts" ]; then
    echo "Creating scripts link:"
    set -x
    ln -fs ${PWD}/${HOSTNAME}_scripts ${HOME}/scripts
    set +x
fi

