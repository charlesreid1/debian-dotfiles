#!/bin/bash

REPOURL="https://git.charlesreid1.com/data/charlesreid1-data.git"

git -C /www/charlesreid1.com \
    clone \
    --separate-git-dir=git.data \
    -b master \
    $REPOURL htdocs/data

