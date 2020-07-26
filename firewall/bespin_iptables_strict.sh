#!/bin/bash
set -e

ipt="sudo /sbin/iptables"

# Set default policies
$ipt -P INPUT DROP
$ipt -P FORWARD DROP
$ipt -P OUTPUT ACCEPT

# Flush and clear everything
$ipt -t nat -F
$ipt -t mangle -F
$ipt -F
$ipt -X

# Name of PIA VPN tunnel device
PIATUN="tun1"
# Name of loopback interface for PiHole DNS server
PHDNS="lo:1"
# Name of loopback interface for dnsmasq DNS server
DDNS="lo"
# Name of hostapd AP device
AP="wlan1"

########### LOOPBACK ##########
$ipt -A INPUT -i lo -j ACCEPT
$ipt -A INPUT -i lo:1 -j ACCEPT

########### INCOMING ##########
# Allow any established connection to come in or out
$ipt -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT
$ipt -A OUTPUT -m state --state RELATED,ESTABLISHED -j ACCEPT

########### PING ##############
# Allow incoming ping requests
$ipt -A INPUT -p icmp --icmp-type echo-request -j ACCEPT

########### SSH ###############
# Allow incoming SSH sessions, new or established
$ipt -A INPUT -p tcp --dport 22 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
# Allow incoming SSH traffic, if part of established conversation
$ipt -A INPUT -p tcp --sport 22 -m conntrack --ctstate ESTABLISHED -j ACCEPT

########### VPN ###############
# Allow incoming VPN sessions destined for 1194, new or established
$ipt -A INPUT -p udp --dport 1194 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
# Allow incoming VPN traffic coming from 1194, part of established conversation
$ipt -A INPUT -p udp --sport 1194 -m conntrack --ctstate ESTABLISHED -j ACCEPT

########### HTTP/HTTPS ########
# Allow incoming HTTP/HTTPS traffic, part of established conversation
$ipt -A INPUT -p tcp --sport 80 -m conntrack --ctstate ESTABLISHED -j ACCEPT
$ipt -A INPUT -p tcp --sport 443 -m conntrack --ctstate ESTABLISHED -j ACCEPT

########### DHCP ##############
# Allow any DHCP traffic to come in or out
$ipt -A INPUT  -p udp --dport 67:68 --sport 67:68 -j ACCEPT
$ipt -A OUTPUT -p udp --dport 67:68 --sport 67:68 -j ACCEPT

########### PIA VPN ##############
# This is a PIA VPN tunnel that handles traffic from APs
# Accept all traffic coming in from tunnel
$ipt -A INPUT -i ${PIATUN} -j ACCEPT
# Masquaerade outgoing traffic leaving via the tunnel
$ipt -t nat -A POSTROUTING -o ${PIATUN} -j MASQUERADE

########### DNS ###############
PROTOCOLS="tcp udp"
for prot in $PROTOCOLS; do
    # General DNS Traffic:
    # Allow incoming DNS traffic coming from 53, part of established conversation
    $ipt -A INPUT  -p $prot --sport 53 --dport 1024:65535 -m state --state ESTABLISHED -j ACCEPT

    # PiHole self-accept traffic from port 53
    $ipt -A INPUT -p $prot -i ${PHDNS} --dport 53 -j ACCEPT

    # PiHole DNS (lo:1) <-> PIA VPN Tunnel (tun0):
    # PiHole can always send DNS queries out through tunnel
    $ipt -A FORWARD -p $prot -i ${PHDNS} -o ${PIATUN} --dport 53 -j ACCEPT
    # Responses to PiHole can always return via tunnel
    $ipt -A FORWARD -p $prot -i ${PIATUN} -o ${PHDNS} --dport 53 -m state --state ESTABLISHED,RELATED -j ACCEPT

    # dnsmasq DNS (lo) <-> PiHole DNS (lo:1)
    # Allow all DNS traffic from local dnsmasq DNS server to local PiHole DNS server
    $ipt -A FORWARD -p $prot -i ${DDNS} -o ${PHDNS} --dport 53 -j ACCEPT
    # Allow responses to dnsmasq to return via the PiHole DNS server
    $ipt -A FORWARD -p $prot -i ${PHDNS} -o ${DDNS} --dport 53 -m state --state ESTABLISHED,RELATED -j ACCEPT

    # hostapd AP (wlan1) <-> dnsmasq DNS (lo)
    # Allow DNS traffic to travel both ways between AP and dnsmasq
    $ipt -A FORWARD -p $prot -i ${AP} -o ${DDNS} --dport 53 -j ACCEPT
    $ipt -A FORWARD -p $prot -o ${AP} -i ${DDNS} --sport 53 -j ACCEPT
done

########### PIHOLE UI #########
# 8080/8443

## Enable logging
#$ipt -N LOGGING
#$ipt -A INPUT -j LOGGING
#$ipt -A LOGGING -m limit --limit 2/min -j LOG --log-prefix "iptables dropped: " --log-level 4
#$ipt -A LOGGING -j DROP

# Make rules persistent
sudo netfilter-persistent save

# Restore docker iptables rules
sudo service docker restart
