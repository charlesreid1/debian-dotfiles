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

if [[ "$HOSTNAME" == "jupiter" ]]; then
    EXTRA_EXCLUDE=''
else
    EXTRA_EXCLUDE='--exclude "jupiter_scripts"'
fi

function doIt() {
    rsync \
        --exclude ".git/" \
        --exclude "bootstrap.sh" \
        ${EXTRA_EXCLUDE} \
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
