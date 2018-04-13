#!/bin/bash
#
# Install tincd
#
# krash = 10.6.0.1
# blackbeard = 10.6.0.244
# jupiter = 10.6.0.36
#
# hard-coded to avoid string variable mixups.

if [ "$(id -u)" != "0" ]; then
    echo ""
    echo ""
    echo "This script should be run as root."
    echo ""
    echo ""
    exit 1;
fi

LABEL="master"
USER="charles"

apt-get install -y tinc

mkdir -p /etc/tinc/$LABEL

# -----------

if [[ "$HOSTNAME" == "krash" ]]; then

    cat > /etc/tinc/$LABEL/tinc.conf <<EOL
Name = krash
AddressFamily = any
Mode = switch
EOL

    cat > /etc/tinc/$LABEL/tinc-up <<EOL
#!/bin/sh
ifconfig $INTERFACE 10.6.0.36 netmask 255.255.0.0
EOL

# -----------

elif [[ "$HOSTNAME" == "blackbeard" ]]; then

    cat > /etc/tinc/$LABEL/tinc.conf <<EOL
Name = blackbeard
AddressFamily = any
Mode = switch
EOL

    cat > /etc/tinc/$LABEL/tinc-up <<EOL
#!/bin/sh
ifconfig $INTERFACE 10.6.0.244 netmask 255.255.0.0
EOL

# -----------

elif [[ "$HOSTNAME" == "jupiter" ]]; then

    cat > /etc/tinc/$LABEL/tinc.conf <<EOL
Name = blackbeard
AddressFamily = any
Mode = switch
EOL

    cat > /etc/tinc/$LABEL/tinc-up <<EOL
#!/bin/sh
ifconfig $INTERFACE 10.6.0.36 netmask 255.255.0.0
EOL

# -----------

else

    cat > /etc/tinc/$LABEL/tinc.conf <<EOL
Name = unknown
AddressFamily = any
Mode = switch
EOL

    cat > /etc/tinc/$LABEL/tinc-up <<EOL
#!/bin/sh
ifconfig $INTERFACE 10.6.0.x netmask 255.255.0.0
EOL

fi

# -----------

cat > /etc/tinc/$LABEL/tinc-down <<EOL
#!/bin/sh
ifconfig $INTERFACE down
EOL

git clone https://git.charlesreid1.com/charlesreid1/tinc-hosts.git /etc/tinc/$LABEL/hosts
sudo chown -R $USER:$USER /etc/tinc/$LABEL/hosts

