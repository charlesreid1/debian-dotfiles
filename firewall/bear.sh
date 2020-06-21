#!/bin/bash
#
# Set up the ufw firewall for bear.
# 22 - ssh
# 80 - http
# 443 - https
# 8080, 8888, 8000 - for something to use

if [ "$(id -u)" != "0" ]; then
    echo ""
    echo ""
    echo "This script must be run as root!"
    echo ""
    echo ""
    exit 1;
fi

set -x

# Start by setting defaults on ufw
ufw --force reset
ufw default deny incoming
ufw default allow outgoing
ufw allow 22
ufw allow 80
ufw allow 443
ufw --force enable

# allow ufw to nat connections from
# external interface to internal 
# (docker) interfaces
sed -i -e 's/DEFAULT_FORWARD_POLICY="DROP"/DEFAULT_FORWARD_POLICY="ACCEPT"/g' /etc/default/ufw
ufw reload

# enable packet masquerading so we can
# get the real IP of clients inside
# docker containers.
iptables -t nat -A POSTROUTING ! -o docker0 -s 172.17.0.0/16 -j MASQUERADE

