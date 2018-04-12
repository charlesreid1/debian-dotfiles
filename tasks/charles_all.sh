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

    root_dir=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

    $root_dir/system/charles_system_all.sh
    $root_dir/install/charles_install_all.sh
    $root_dir/deployment/charles_deployment_all.sh

fi

