#!/bin/bash

deployment_dir=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

$deployment_dir/charles_setup_pelican.py
$deployment_dir/charles_setup_www.py

