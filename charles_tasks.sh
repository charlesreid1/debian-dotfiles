#!/bin/bash

./install_pyenv.sh
./python_install.sh
./python_setup.sh
./gen_ssh_keys.sh

cd ~
(
mkdir codes
cd codes
(
mkdir docker
cd docker

git clone https://charlesreid1.com:3000/docker/d-mysql.git
(
cd d-mysql
make
)

git clone https://charlesreid1.com:3000/docker/d-phpmyadmin.git
(
cd d-phpmyadmin
make
)

git clone https://charlesreid1.com:3000/docker/d-mediawiki.git
(
cd d-mediawiki
make
)

git clone https://charlesreid1.com:3000/docker/d-charlesreid1-utils.git
)
)

