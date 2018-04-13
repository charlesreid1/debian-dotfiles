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
RANDSTRING="`python -c "import random, string; print(''.join(random.choices(string.ascii_uppercase, k=2) + random.choices(string.digits, k=1)))"`"
$DOTFILES/tasks/sudo_all.sh $RANDSTRING

# copy the user init script
cp $DOTFILES/tasks/charles_init.sh /home/$USER/.
chown $USER:$USER /home/$USER/charles_init.sh

# run user init script as user
sudo -H -i -u $USER /home/$USER/charles_init.sh

