#!/bin/bash

# wireless
apt-get install -y wireless-tools
apt-get install -y aircrack-ng
apt-get install -y net-tools
apt-get install -y reaver
apt-get install -y john
apt-get install -y lua5.3
apt-get install -y liblua5.3-0
apt-get install -y liblua5.3-dev

## Ideally, would add wifite to a 
## directory that is on $PATH
#curl -o /tmp/wifite.tar.gz http://http.debian.net/debian/pool/main/w/wifite/wifite_2.0.87+git20170515.918a499.orig.tar.gz
