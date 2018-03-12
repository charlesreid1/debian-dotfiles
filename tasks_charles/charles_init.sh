#!/bin/bash

./pre_bootstrap.sh
./bootstrap.sh -f
./install_pyenv.sh
./python_install.sh
./python_setup.sh
./gen_ssh_keys.sh
./docker_init.sh

