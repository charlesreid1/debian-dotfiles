#!/usr/bin/env python3
import subprocess
import os
import time

"""
Captain Hook: Pull Captain Hook on the Host 

This script is called by the host machine 
(blackbeard) running the Captain Hook container.

This is triggered by push actions to the 
master branch of b-captain-hook.

The action is to update (git pull) the copy 
of Captain Hook running on the host, and
restart the container pod.
"""

work_dir = os.path.join('/home','charles','codes','docker','pod-webhooks','b-captain-hook')
pod_dir = os.path.join('/home','charles','codes','docker','pod-webhooks')

# Step 1:
# Update Captain Hook
co_cmd = ['git','checkout','master']
subprocess.call(co_cmd, cwd=work_dir)

pull_cmd = ['git','pull','origin','master']
subprocess.call(pull_cmd, cwd=work_dir)

time.sleep(10)

# Step 2:
# Restart Captain Hook pod
pod_restart = ['docker-compose','restart']
subprocess.call(pod_restart, cwd=pod_dir)

