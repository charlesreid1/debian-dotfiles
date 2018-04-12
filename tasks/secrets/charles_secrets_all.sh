#!/bin/bash
set -x

secrets_dir=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

$secrets_dir/charles_gen_ssh_keys.sh

