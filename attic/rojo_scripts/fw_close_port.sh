#!/bin/bash

port="3306"

# Block traffic on port $PORT
/sbin/iptables -A INPUT -p tcp --destination-port ${port} -j DROP

# block incoming port 80 except if source ip address 1.2.3.4
# /sbin/iptables -A INPUT -p tcp i eth1 -s ! 1.2.3.4 --dport 80 -j DROP

/sbin/service iptables save

