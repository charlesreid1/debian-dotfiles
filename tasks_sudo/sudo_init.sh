#!/bin/bash

if [[ "$#" -eq 1 ]] 
then

    DOTFILES="/root/codes/dotfiles"
    DEBIAN="$DOTFILES/debian"
    cd $DEBIAN/tasks_sudo

    ./make_user_charles.sh
    ./install_packages.sh
    ./remove_packages.sh
    ./fix_ssh.sh
    ./set_time.sh
    ./get_docker.sh
    ./instal_certbot.sh
    ./add_charles_to_docker.sh
    ./set_machine_name.sh $1

else

    echo "No machine name specified"
    exit 1;

fi
