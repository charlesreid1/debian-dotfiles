#!/bin/bash

secrets_dir=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

$secrets_dir/sudo_fix_ssh.sh
$secrets_dir/sudo_gen_ssh_keys.sh
$secrets_dir/sudo_install_certbot.sh

