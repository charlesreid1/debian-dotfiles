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

    system_dir=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

    $system_dir/sudo_set_machine_name.sh $1
    $system_dir/sudo_make_user_charles.sh
    $system_dir/sudo_add_charles_to_groups.sh
    $system_dir/sudo_set_time.sh

fi

