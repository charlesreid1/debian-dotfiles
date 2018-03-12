#!/bin/bash

adduser --quiet charles
echo "charles:zeno135" | chpasswd
usermod -aG sudo charles

mkdir /home/charles/.ssh
chown charles:charles /home/charles/.ssh
chmod 700 /home/charles/.ssh
touch /home/charles/.ssh/authorized_keys
chmod 600 /home/charles/.ssh/authorized_keys

