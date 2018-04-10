#!/bin/sh
#
# Lays the groundwork for dotfile installation;
# creates vim swap/undo directories and sets bash
# as the user's shell.

# Actually make the swap directory vim is going to use
mkdir -p ~/.vim/swap
mkdir -p ~/.vim/undo
mkdir -p ~/.vim/backups
mkdir -p ~/.logs

