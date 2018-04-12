#!/bin/bash
#
# Install SSH server
# Fix SSH keys
# Enable SSH service on boot

if [ "$(id -u)" != "0" ]; then
    echo ""
    echo ""
    echo "This script should be run as root."
    echo ""
    echo ""
    exit 1;
fi

apt-get install -y openssh-server

update-rc.d -f ssh remove
update-rc.d -f ssh defaults

cd /etc/ssh/
mkdir -p insecure_orig_keys/
mv ssh_host_* insecure_orig_keys/.

dpkg-reconfigure openssh-server

systemctl restart ssh

# public/private key pairs 
# are created by running
# ../gen_ssh_keys.sh
