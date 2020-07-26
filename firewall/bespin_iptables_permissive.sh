#!/bin/bash
set -e

ipt="sudo /sbin/iptables"

# start by flushing all rules and setting defaults
$ipt -F
# should we do this?
#$ipt -P INPUT DROP
#$ipt -P FORWARD DROP
$ipt -P INPUT ACCEPT
$ipt -P FORWARD ACCEPT
$ipt -P OUTPUT ACCEPT
$ipt -t nat -F
$ipt -t mangle -F
$ipt -F
$ipt -X

$ipt -A INPUT -p icmp --icmp-type echo-request -j ACCEPT

##################################
# PIA VPN Tunnels

# These are PIA tunnels that handle traffic from APs
PIA_AP_TUNNELS="tun1"
for TUN in TUNNELS; do
    # Accept all traffic coming in from tunnel
    $ipt -A INPUT -i ${TUN} -j ACCEPT
    # Masquaerade outgoing traffic leaving via the tunnel
    $ipt -t nat -A POSTROUTING -o ${TUN} -j MASQUERADE
done

##################################
# AP-PIA Tunneling

# Forward outgoing traffic for APs through tunnel
AP="wlan1"
TUN="tun1"
$ipt -A FORWARD -i ${AP} -o ${TUN} -j ACCEPT
$ipt -A FORWARD -i ${TUN} -o ${AP} -m state --state ESTABLISHED,RELATED -j ACCEPT

##################################
# DNS Tunneling

# Forward outgoing DNS traffic from lo:1 (PiHole) through PIA tunnel
DNS="lo:1"
TUN="tun1"
PROTOCOLS="udp tcp"
for PROTOCOL in $PROTOCOLS; do
    # PiHole can always send DNS queries out through tunnel
    $ipt -A FORWARD -p ${PROTOCOL} -i ${DNS} -o ${TUN} --dport 53 -j ACCEPT
    # Responses to PiHole can always return via tunnel
    $ipt -A FORWARD -p ${PROTOCOL} -i ${TUN} -o ${DNS} --dport 53 -m state --state ESTABLISHED,RELATED -j ACCEPT
done

# Enable logging
$ipt -N LOGGING
$ipt -A INPUT -j LOGGING
$ipt -A LOGGING -m limit --limit 2/min -j LOG --log-prefix "iptables dropped: " --log-level 4
$ipt -A LOGGING -j DROP

# Make rules persistent
sudo netfilter-persistent save

# Restore docker iptables rules
sudo service docker restart
