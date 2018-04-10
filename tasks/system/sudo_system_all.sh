#!/bin/bash
# 
# initial entry point

if [[ "$#" -eq 0 ]]
then
    echo ""
    echo ""
    echo "This script should be run with an argument (the hostname to set)."
    echo ""
    echo ""
    exit 1;
else

    ./sudo_set_machine_name.sh $1
    ./sudo_make_user_charles.sh
    ./sudo_add_charles_to_groups.sh
    ./sudo_set_time.sh

fi

