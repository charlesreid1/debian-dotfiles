#!/bin/bash
#
# Install tincd on krash
#
# krash = 10.6.0.36

if [ "$(id -u)" != "0" ]; then
    echo ""
    echo ""
    echo "This script should be run as root."
    echo ""
    echo ""
    exit 1;
fi

LABEL="master"

apt-get install -y tinc

mkdir -p /etc/tinc/$LABEL

cat > /etc/tinc/$LABEL/tinc.conf <<EOL
Name = krash
AddressFamily = any
Mode = switch
EOL

cat > /etc/tinc/$LABEL/tinc-up <<EOL
#!/bin/sh
ifconfig $INTERFACE 10.6.0.36 netmask 255.255.0.0
EOL

cat > /etc/tinc/$LABEL/tinc-down <<EOL
#!/bin/sh
ifconfig $INTERFACE down
EOL

