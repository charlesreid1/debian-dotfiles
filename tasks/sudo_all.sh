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

    (
    cd system
    ./sudo_system_all.sh
    )

    (
    cd install
    ./sudo_install_all.sh
    )
    
    (
    cd secrets
    ./sudo_secrets_all.sh
    )

    (
    cd deployment
    ./sudo_deployment_all.sh
    )

fi

