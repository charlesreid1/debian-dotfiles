#!/bin/sh
#
# Run a set of bot scripts, each in their own screen.
# To see a list of screens, run:
# $ screen -ls
#
# -d -m 
# Start screen in "detached" mode. 
# Create new session but do not attach to it.
# Useful for scripts. 
#
# -S 
# This option can give a name to the new screen.
#
# We change dir every time to keep the log files clean/organized
# and ensure scripts can find keys.

# Apollo bot flock
DIR="/home/charles/codes/apollospacejunk/bot"
cd $DIR
/usr/bin/screen -d -m -S apollo /usr/bin/python3 $DIR/ApolloBotFlock.py

# Ginsberg bot flock
DIR="/home/charles/codes/ginsberg/bot"
cd $DIR
/usr/bin/screen -d -m -S ginsberg /usr/bin/python3 $DIR/GinsbergBotFlock.py

# Milton bot flock
DIR="/home/charles/codes/milton/bot"
cd $DIR
/usr/bin/screen -d -m -S milton /usr/bin/python3 $DIR/MiltonBotFlock.py

# Tripos bot 
DIR="/home/charles/codes/tripos-bot"
cd $DIR
/usr/bin/screen -d -m -S tripos /usr/bin/python3 $DIR/Tripos.py

cd ${HOME}/scripts

