#!/bin/bash

if [ "$(id -u)" != "0" ]; then
    echo ""
    echo ""
    echo "This script should be run as root."
    echo ""
    echo ""
    exit 1;
fi

if [ "$HOSTNAME" != "jupiter" ]; then
    echo ""
    echo ""
    echo "This script should only be run on jupiter."
    echo ""
    echo ""
    exit 1;
fi

# wireless
apt-get install -y wireless-tools
apt-get install -y aircrack-ng
apt-get install -y net-tools
apt-get install -y reaver
apt-get install -y john

