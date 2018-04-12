#!/bin/bash

install_dir=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

$install_dir/sudo_install_packages.sh
$install_dir/sudo_remove_packages.sh
$install_dir/sudo_install_system_python.sh
$install_dir/sudo_install_docker.sh

