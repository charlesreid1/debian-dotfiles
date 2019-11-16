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
        --exclude "bootstrap.sh" \
        --exclude "bluebeard_scripts" \
        --exclude "redbeard_scripts" \
        --exclude "blackbeard_scripts" \
        --exclude "bluebear_scripts" \
        --exclude "jupiter_scripts" \
        --exclude "krash_scripts" \
        --exclude "rojo_scripts" \
        --exclude "scripts" \
        --exclude ".git" \
        --exclude ".gitignore" \
        -avh --no-perms . ~;
    source ~/.bash_profile;
}

if [ "$1" == "--force" -o "$1" == "-f" ]; then
    doIt;
else
    ./diff_dotfiles.sh
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
    rm -fr ${HOME}/scripts
    ln -fs ${PWD}/${HOSTNAME}_scripts/ ${HOME}/scripts
    set +x
fi

