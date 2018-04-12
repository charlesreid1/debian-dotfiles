#!/bin/bash

if [[ "$HOSTNAME" == "blackbeard" ]]; then
    BOTS="$HOME/codes/bots"
    mkdir -p $BOTS
    cd $BOTS

    git clone https://git.charlesreid1.com/bots/b-captain-hook.git
    git clone https://git.charlesreid1.com/bots/b-rainbow-mind-machine.git
    git clone https://git.charlesreid1.com/bots/b-tripos.git
    git clone https://git.charlesreid1.com/bots/b-milton.git
    git clone https://git.charlesreid1.com/bots/b-ginsberg.git
    git clone https://git.charlesreid1.com/bots/b-apollo.git
    git clone https://git.charlesreid1.com/bots/b-melochaz-bot.git
    git clone https://git.charlesreid1.com/bots/b-charlesreid1.git
fi

