#!/bin/bash
#
# use iptables to ban jerks
# from accessing the server

if [ "$(id -u)" != "0" ]; then
    echo ""
    echo ""
    echo "This script should be run as root."
    echo ""
    echo ""
    exit 1;
fi

# some incredibly obnoxious marketing spammer that was (is?) DDOSing me
CIDR_IP="46.229.168.0/24"
/sbin/iptables -A INPUT -s ${CIDR_IP} -j DROP

# fail2ban
for IPADDR in $(cat /var/log/fail2ban.log | /bin/grep "Ban " | sed 's/^.*Ban \(.*\)$/\1/g' | sort | uniq); do

    /sbin/iptables -A INPUT -s ${IPADDR} -j DROP

done

