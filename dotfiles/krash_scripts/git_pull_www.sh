#!/bin/bash

git -C /www/charlesreid1.com \
    --git-dir=git --work-tree=htdocs \
    pull origin gh-pages

