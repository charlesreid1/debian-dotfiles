#!/bin/bash
# 
# https://certbot.eff.org/lets-encrypt/ubuntuxenial-nginx
set -x

if [ "$(id -u)" != "0" ]; then
    echo ""
    echo ""
    echo "This script should be run as root."
    echo ""
    echo ""
    exit 1;
fi

apt-get update
apt-get -y install software-properties-common
add-apt-repository -y ppa:certbot/certbot
apt-get update
apt-get -y install python-certbot-nginx 
