#!/bin/bash

git -C /www/charlesreid1.com \
    --git-dir=git.data --work-tree=htdocs/data \
    pull origin master

