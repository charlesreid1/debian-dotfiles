#!/bin/bash

echo "Making 4096-bit RSA key for charlesreid1@gmail.com"
echo "Public key will be in ~/.ssh/id_rsa.pub"
echo "Private key will be in ~/.ssh/id_rsa"

ssh-keygen -t rsa -b 4096 -C "charlesreid1@gmail.com" -P "" -f ~/.ssh/id_rsa
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa

echo "-------------------"
echo "Your public key is:"
cat ~/.ssh/id_rsa.pub
