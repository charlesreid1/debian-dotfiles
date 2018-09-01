#!/bin/bash

REPOURL="https://git.charlesreid1.com/charlesreid1/charlesreid1.com.git"

git -C /www/charlesreid1.com \
    clone \
    --separate-git-dir=git \
    -b gh-pages \
    $REPOURL htdocs

