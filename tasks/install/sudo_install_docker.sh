#!/bin/bash
# 
# adding user to docker group
# requires log out and log back in
# before they can run docker

# docker
bash <( curl https://get.docker.com )
docker --version

# docker compose
sudo curl -L https://github.com/docker/compose/releases/download/1.20.1/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version

sudo gpasswd -a charles docker
