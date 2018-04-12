#!/bin/bash

if [ -f "${PWD}/${HOSTNAME}" ]; then
    cp ${PWD}/${HOSTNAME} /etc/motd
fi
