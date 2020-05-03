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
