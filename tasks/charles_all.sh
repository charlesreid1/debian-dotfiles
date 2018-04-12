#!/bin/bash

if [[ "$#" -gt 0 ]]
then
    echo ""
    echo ""
    echo "This script should not be run with any arguments." 
    echo ""
    echo ""
    exit 1;
elif [ "$(id -u)" == "0" ]; then
    echo ""
    echo ""
    echo "This script should be run as user charles, not as root!"
    echo ""
    echo ""
    exit 1;
fi


tasks_dir=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

$tasks_dir/system/charles_system_all.sh
$tasks_dir/install/charles_install_all.sh
$tasks_dir/secrets/charles_secrets_all.sh
$tasks_dir/deployment/charles_deployment_all.sh

(
cd $tasks_dir/../dotfiles
./bootstrap.sh -f
)

