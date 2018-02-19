#!/bin/bash

port="443"
/sbin/iptables -A INPUT   -p tcp           --dport ${PORT} -j ACCEPT
/sbin/iptables -A FORWARD -p tcp -j ACCEPT --dport ${PORT} -m state --state NEW

/sbin/service iptables save

