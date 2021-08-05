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

# Name of main ethernet connection device
ETH="wlan0"
# Name of PIA VPN tunnel device
PIATUN="tun1"
# Name of tinc tunnel device
TINCTUN="master"
# Name of loopback interface for PiHole DNS server
PHDNS="lo:1"

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

########### TINC ##############
# Allow incoming VPN sessions destined for 655, new or established
$ipt -A INPUT -p udp --dport 655 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
# Allow incoming VPN traffic coming from 655, part of established conversation
$ipt -A INPUT -p udp --sport 655 -m conntrack --ctstate ESTABLISHED -j ACCEPT

########### HTTP/HTTPS ########
# Allow incoming HTTP/HTTPS traffic, part of established conversation
$ipt -A INPUT -p tcp --sport 80 -m conntrack --ctstate ESTABLISHED -j ACCEPT
$ipt -A INPUT -p tcp --sport 443 -m conntrack --ctstate ESTABLISHED -j ACCEPT

# Allow incoming HTTP/HTTPS requests from tinc tunnel
$ipt -A INPUT -p tcp -i ${TINCTUN} --dport 80 -j ACCEPT
$ipt -A INPUT -p tcp -i ${TINCTUN} --dport 443 -j ACCEPT

# Allow incoming HTTP/HTTPS requests from local ethernet
$ipt -A INPUT -p tcp -i ${ETH} --dport 80 -j ACCEPT
$ipt -A INPUT -p tcp -i ${ETH} --dport 443 -j ACCEPT

########### PIHOLE UI #########
# Allow incoming requests to 8888/8443 via tinc tunnel
$ipt -A INPUT -p tcp -i ${TINCTUN} --dport 8888 -j ACCEPT
$ipt -A INPUT -p tcp -i ${TINCTUN} --dport 8443 -j ACCEPT

########### TELEMETRY #########
# Allow node exporter traffic from source port 9100
$ipt -A INPUT -p tcp --dport 9100 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
$ipt -A INPUT -p tcp --sport 9100 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
# Allow cadvisor on port 8080
$ipt -A INPUT -p tcp --dport 8080 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
$ipt -A INPUT -p tcp --sport 8080 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
# Allow nginx on port 9113
$ipt -A INPUT -p tcp --dport 9113 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
$ipt -A INPUT -p tcp --sport 9113 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT

########### DHCP ##############
# Allow any DHCP traffic to come in or out
$ipt -A INPUT  -p udp --dport 67:68 --sport 67:68 -j ACCEPT
$ipt -A OUTPUT -p udp --dport 67:68 --sport 67:68 -j ACCEPT

########### DNS ###############
PROTOCOLS="tcp udp"
for prot in $PROTOCOLS; do
    # General DNS Traffic:
    # Allow incoming DNS traffic coming from 53, part of established conversation
    $ipt -A INPUT  -p $prot --sport 53 --dport 1024:65535 -m state --state ESTABLISHED -j ACCEPT

    # PiHole self-accept traffic from port 53
    $ipt -A INPUT -p $prot -i ${PHDNS} --dport 53 -j ACCEPT

    # # PiHole DNS (lo:1) <-> PIA VPN Tunnel (tun0):
    # # PiHole can always send DNS queries out through tunnel
    # $ipt -A FORWARD -p $prot -i ${PHDNS} -o ${PIATUN} --dport 53 -j ACCEPT
    # # Responses to PiHole can always return via tunnel
    # $ipt -A FORWARD -p $prot -i ${PIATUN} -o ${PHDNS} --dport 53 -m state --state ESTABLISHED,RELATED -j ACCEPT

    # PiHole DNS (lo:1) <-> ethernet
    # PiHole can always send DNS queries out through tunnel
    $ipt -A FORWARD -p $prot -i ${PHDNS} -o ${ETH} --dport 53 -j ACCEPT
    # Responses to PiHole can always return via ethernet
    $ipt -A FORWARD -p $prot -i ${ETH} -o ${PHDNS} --dport 53 -m state --state ESTABLISHED,RELATED -j ACCEPT

done

# # Enable logging
# $ipt -N LOGGING
# $ipt -A INPUT -j LOGGING
# $ipt -A LOGGING -m limit --limit 2/min -j LOG --log-prefix "iptables dropped: " --log-level 4
# $ipt -A LOGGING -j DROP

# Make rules persistent
sudo netfilter-persistent save

# Restore docker iptables rules
sudo service docker restart
