#!/bin/bash

set -x

if [ "$(id -u)" != "0" ]; then
    echo ""
    echo ""
    echo "This script should be run as root."
    echo ""
    echo ""
    exit 1;
fi

for SUB in pages bots hooks; do
    REPOURL="https://git.charlesreid1.com/charlesreid1/${SUB}.charlesreid1.com.git"

    mkdir -p /www/${SUB}.charlesreid1.com
    sudo chown -R charles:charles /www/${SUB}.charlesreid1.com

    sudo -H -u charles git -C /www/${SUB}.charlesreid1com \
            --git-dir=git --work-tree=htdocs \
            pull origin gh-pages

done

set +x


