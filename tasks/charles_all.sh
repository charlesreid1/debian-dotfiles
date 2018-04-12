#!/bin/bash

if [[ "$#" -eq 0 ]]
then
    echo ""
    echo ""
    echo "This script should be run with an argument (the hostname to set)."
    echo ""
    echo ""
    exit 1;
else

    tasks_dir=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

    $tasks_dir/system/charles_system_all.sh
    $tasks_dir/install/charles_install_all.sh
    $tasks_dir/deployment/charles_deployment_all.sh

    (
    cd $tasks_dir/../dotfiles
    ./bootstrap.sh -f
    )

fi

