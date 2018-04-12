#!/bin/bash
#
# This script is intended to get you from
# bare metal to a machine ready for 
# charlesreid1 tasks.
#
# blackbeard - bots/hooks
# krash - charlesreid1 pod
# jupiter - utility
#
# Run as a one-shot installer:
# bash <( curl INSERT_SCRIPT_URL_HERE )
# 
set -x

USER="charles"

# first things first
apt-get update
apt-get install -y git

#######################
# First, the root user 
# runs the dotfiles
# installation script

# check out root user dotfiles at /root/dotfiles
DOTFILES="$HOME/dotfiles"
git clone https://git.charlesreid1.com/dotfiles/debian $DOTFILES



# run root init script
$DOTFILES/tasks_sudo/sudo_init.sh dahak-yeti

# copy the user init script
cp $DOTFILES/tasks_user/user_init.sh /home/$USER/.
chown $USER:$USER /home/$USER/user_init.sh

# run user init script as user
sudo -H -i -u $USER /home/$USER/user_init.sh

