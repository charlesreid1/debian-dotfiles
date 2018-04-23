#!/usr/bin/env python3
import subprocess
import os

"""
Captain Hook: Pull Captain Hook on the Host 

This script is called by the host machine 
(blackbeard) running the Captain Hook container.

This is triggered by push actions to the 
master branch of b-captian-hook.

The action is to update (git pull) the copy 
of captain hook running on the host, and
restart the container pod.

TODO: stable/latest, /webhooks copy, etc.
"""

work_dir = os.path.join('/home','charles','codes','bots','b-captain-hook')

# Step 1:
# Update Captain Hook
pull_cmd = ['git','pull','origin','master']
subprocess.call(pull_cmd, cwd=work_dir)

# Step 2:
# Restart Captain Hook pod
pod_restart = ['docker-compose','restart']
subprocess.call(pod_restart, cwd=work_dir)

