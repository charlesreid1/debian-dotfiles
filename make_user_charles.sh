#!/bin/bash

adduser --quiet charles
passwd charles zeno135
usermod -aG sudo charles

mkdir /home/charles/.ssh
chown charles:charles /home/charles/.ssh
chmod 700 /home/charles/.ssh
touch /home/charles/.ssh/authorized_keys
chmod 600 /home/charles/.ssh/authorized_keys

