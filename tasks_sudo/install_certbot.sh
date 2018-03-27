#!/bin/bash
# 
# https://certbot.eff.org/lets-encrypt/ubuntuxenial-nginx

apt-get update
apt-get install software-properties-common
add-apt-repository ppa:certbot/certbot
apt-get update
apt-get install python-certbot-nginx 
