#!/bin/bash
#
# make the directory 
# that will hold
# all charlesreid1 files
#
# TODO: check hostname

mkdir -p /www
chown -R charles:charles /www
chmod -R 775 /www
