#!/bin/bash

export GTD="/www/gitea/bin"

# Run a gitea web server
cd ${GTD}

/usr/bin/screen -d -m -S gitea \
    sudo -H -u git ${GTD}/gitea web 
