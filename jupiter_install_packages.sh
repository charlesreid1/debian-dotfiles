#!/bin/bash

if [ "$(id -u)" != "0" ]; then
    echo ""
    echo ""
    echo "This script should be run as root."
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

## Ideally, would add wifite to a 
## directory that is on $PATH
#curl -o /tmp/wifite.tar.gz http://http.debian.net/debian/pool/main/w/wifite/wifite_2.0.87+git20170515.918a499.orig.tar.gz
