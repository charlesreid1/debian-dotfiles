#!/bin/bash
set -x

secrets_dir=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

$secrets_dir/sudo_fix_ssh.sh
$secrets_dir/sudo_gen_ssh_keys.sh
$secrets_dir/sudo_install_certbot.sh

$secrets_dir/charles_gen_ssh_keys.sh

if [[ "$HOSTNAME" == "blackbeard" ]]; then
    # aws only:
    # copy authorized key
    # from ubuntu to charles
    cp /home/ubuntu/.ssh/authorized_keys /home/charles/.ssh/authorized_keys
    chown charles:charles /home/charles/.ssh/authorized_keys
fi

# If we are on another host, 
# we need to set the password manually.
# boooooo.
# 
# alternatively, grab a public key
# using wget or something.

