#!/bin/bash
set -x

USER="charles"

# first things first
apt-get update
apt-get install -y git

# check out root user dotfiles at /root/dotfiles
DOTFILES="$HOME/dotfiles"
git clone https://git.charlesreid1.com/dotfiles/debian $DOTFILES

# run root init script
$DOTFILES/tasks/sudo_all.sh blackbeard

# copy the user init script
cp $DOTFILES/tasks/charles_init.sh /home/$USER/.
chown $USER:$USER /home/$USER/user_init.sh

# run user init script as user
sudo -H -i -u $USER /home/$USER/user_init.sh

