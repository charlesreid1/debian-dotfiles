#!/bin/bash

if [[ "$#" -eq 0 ]]
then
    echo ""
    echo ""
    echo "This script should be run with an argument (the hostname to set)."
    echo ""
    echo ""
    exit 1;
elif [ "$(id -u)" != "0" ]; then
    echo ""
    echo ""
    echo "This script should be run as root."
    echo ""
    echo ""
    exit 1;
fi

    root_dir=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
    
    $root_dir/system/sudo_system_all.sh
    $root_dir/install/sudo_install_all.sh
    $root_dir/secrets/sudo_secrets_all.sh
    $root_dir/deployment/sudo_deployment_all.sh

fi

