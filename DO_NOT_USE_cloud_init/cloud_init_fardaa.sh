#!/bin/bash
set -x

# this is hard-coded into the system tasks:
# sudo_make_user_charles.sh
USER="charles"

# first things first
apt-get update
apt-get install -y git

# check out root user dotfiles at /root/dotfiles
DOTFILES="$HOME/dotfiles"
git clone https://git.charlesreid1.com/dotfiles/debian $DOTFILES

# run root init script
THE_HOSTNAME="fardaa"
$DOTFILES/tasks/sudo_all.sh $THE_HOSTNAME

# above script creates user charles with pw zeno135
# change it

# copy the user init script
cp $DOTFILES/tasks/charles_init.sh /home/$USER/.
chown $USER:$USER /home/$USER/charles_init.sh

# run user init script as user
sudo -H -i -u $USER /home/$USER/charles_init.sh

