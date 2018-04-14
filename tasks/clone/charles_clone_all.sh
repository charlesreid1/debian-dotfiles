#!/bin/bash

clone_dir=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

$clone_dir/charles_clone_charlesreid1.sh
$clone_dir/charles_clone_docker.sh
$clone_dir/charles_clone_hacking.sh
$clone_dir/charles_clone_bots.sh
