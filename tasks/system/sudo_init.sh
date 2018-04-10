#!/bin/bash

if [[ "$#" -eq 1 ]] 
then

    # Moar checks of hostname

    DOTFILES="/root/codes/dotfiles"
    DEBIAN="$DOTFILES/debian"
    cd $DEBIAN/tasks_sudo

    ./make_user_charles.sh
    ./set_time.sh
    ./set_machine_name.sh $1
    ./add_charles_to_groups.sh

else

    echo "No machine name specified"
    exit 1;

fi
