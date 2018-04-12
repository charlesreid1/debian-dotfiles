#!/bin/bash

install_dir=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

$install_dir/sudo_install_packages.sh
$install_dir/sudo_remove_packages.sh
$install_dir/sudo_install_system_python.sh
if [ -d /var/lib/docker ]; then
    echo "Found existing docker install, skipping docker install."
    echo "You can manually install it later if you want."
else
    $install_dir/sudo_install_docker.sh
fi
