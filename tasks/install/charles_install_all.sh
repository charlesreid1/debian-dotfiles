#!/bin/bash

install_dir=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

$install_dir/charles_install_pyenv.py
$install_dir/charles_install_conda.py
$install_dir/charles_install_python.sh

if [ "$HOSTNAME" == "jupiter" ]; then
    $install_dir/charles_jupiter_install.sh
fi

