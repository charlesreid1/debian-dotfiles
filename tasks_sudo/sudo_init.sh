#!/bin/bash

if [[ "$#" -eq 1 ]] 
then

    DOTFILES="/root/codes/dotfiles"
    DEBIAN="$DOTFILES/debian"
    cd $DEBIAN/tasks_sudo

    ./make_user_charles.sh
    ./set_time.sh
    ./set_machine_name.sh $1
    ./install_packages.sh
    ./remove_packages.sh
    ./fix_ssh.sh
    (
    cd ../
    ./gen_ssh_keys.sh
    )
    ./get_docker.sh
    ./add_charles_to_docker.sh
    ./install_certbot.sh

else

    echo "No machine name specified"
    exit 1;

fi
