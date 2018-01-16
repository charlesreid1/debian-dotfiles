#!/bin/sh
#
# Lays the groundwork for dotfile installation;
# creates vim swap/undo directories and sets bash
# as the user's shell.

# Actually make the swap directory vim is going to use
mkdir -p ~/.vim/swap
mkdir -p ~/.vim/undo

# Change shell to bash
BASH="/bin/bash"
echo "About to set shell to ${BASH}"
chsh -s ${BASH}


