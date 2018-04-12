#!/bin/bash
# 
# very first script run as the user charles
# (user charles equivalent of cloud_init.sh script)
# 
# root copies this script into home dir, runs it bare
# check out a copy of this repository in the home dir

# check out root user dotfiles at /home/charles/dotfiles
DOTFILES="$HOME/dotfiles"
git clone https://git.charlesreid1.com/dotfiles/debian $DOTFILES

# run user init script
$DOTFILES/tasks/charles_all.sh

