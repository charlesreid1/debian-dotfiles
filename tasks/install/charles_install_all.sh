#!/bin/bash

./charles_install_pyenv.py
./charles_install_conda.py
./charles_install_python.sh

if [ "$HOSTNAME" == "jupiter" ]; then
    ./charles_jupiter_install.sh
fi

