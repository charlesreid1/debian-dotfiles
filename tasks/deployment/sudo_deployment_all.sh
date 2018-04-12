#!/bin/bash

deployment_dir=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

$deployment_dir/sudo_setup_www.py
