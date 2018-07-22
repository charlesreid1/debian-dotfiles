#!/bin/bash

: '
Captain Hook Canary Script


Note: this needs an associated systemd service.
See the services directory of the dotfiles repo.

This is a canary script for connecting
the Captain Hook container to the host 
machine, and triggering tasks on the 
host machine with webhooks.

The Captain Hook container mounts the 
following host directory inside the 
container (same location for host/container):

/tmp/triggers/

When a webhook in Captain Hook wants to 
trigger an event on the host (blackbeard),
it puts a file in /tmp/triggers/.

Meanwhile, on the host, this script checks
every 10 seconds for trigger files.

Each webhook can create its own trigger file,
and this script processes each trigger differently.
'

while true
do
    # bootstrap-pull captain hook
    if [ -f "/tmp/triggers/push-b-captain-hook-master" ]; then
        echo "CAPTAIN HOOK'S CANARY:"
        echo "Running trigger to update Captain Hook on the host machine (user charles)"
        sudo -H -u charles python /home/charles/blackbeard_scripts/captain_hook_pull_host.py
        echo "All done."
        rm -f "/tmp/triggers/push-b-captain-hook-master"
        touch /tmp/canary-yup-host-works
    fi

    sleep 10;
done

