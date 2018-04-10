#!/bin/bash
#
# Install SSH server
# Replace stale image SSH keys
# Enable SSH service on boot
#
# This will cause an authentication error
# if you have already logged into the node.
# This is because the RSA fingerprint of 
# the machine that's sent to SSH will change.

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

