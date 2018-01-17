#!/bin/bash
#
# Run like a regular old script, no args needed:
#
# ./set_machine_name.sh
#
# It will prompt you for the hostname you want to set.

echo "This script should be run as root."
echo ""
echo ""

echo "The current hostname is" $(cat /etc/hostname)

echo "Type the new hostname you want for your machine, then press [ENTER]:"
read newhostname

hostname $newhostname 
echo $newhostname > /etc/hostname
echo "127.0.0.1 $newhostname" >> /etc/hosts

echo "The new hostname is ${HOSTNAME}"
echo "The new hostname is" $(cat /etc/hostname)
echo "Try logging out and back in."

