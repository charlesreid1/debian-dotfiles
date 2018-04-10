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
    ./charles_system_all.sh
    )

    (
    cd install
    ./charles_install_all.sh
    )
    
    (
    cd secrets
    ./charles_secrets_all.sh
    )

    (
    cd deployment
    ./charles_deployment_all.sh
    )

fi

