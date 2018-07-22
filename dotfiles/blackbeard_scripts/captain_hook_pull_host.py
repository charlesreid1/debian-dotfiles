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

from datetime import datetime
d = datetime.now().strftime('%Y-m-%d')
with open('/tmp/captain_hook_pull_host_%s.log'%(d),'w') as f:

    # Step 1:
    # Update Captain Hook
    co_cmd = ['git','checkout','master']
    subprocess.call(co_cmd, cwd=work_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    stdout, stderr = proc.communicate()
    o = stdout.decode('utf-8')
    e = stderr.decode('utf-8')
    f.write(" ".join(co_cmd))
    f.write("\n")
    f.write("-"*40)
    f.write("\n")
    f.write(o)
    f.write("\n")
    f.write(e)
    f.write("\n\n")
    
    f_cmd = ['git','fetch','--all']
    subprocess.call(f_cmd, cwd=work_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    stdout, stderr = proc.communicate()
    o = stdout.decode('utf-8')
    e = stderr.decode('utf-8')
    f.write(" ".join(f_cmd))
    f.write("\n")
    f.write("-"*40)
    f.write("\n")
    f.write(o)
    f.write("\n")
    f.write(e)
    f.write("\n\n")
    time.sleep(5)
    
    pull_cmd = ['git','pull','origin','master']
    subprocess.call(pull_cmd, cwd=work_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    stdout, stderr = proc.communicate()
    o = stdout.decode('utf-8')
    e = stderr.decode('utf-8')
    f.write(" ".join(pull_cmd))
    f.write("\n")
    f.write("-"*40)
    f.write("\n")
    f.write(o)
    f.write("\n")
    f.write(e)
    f.write("\n\n")
    time.sleep(10)
    
    # Step 2:
    # Restart Captain Hook pod
    pod_restart = ['docker-compose','restart']
    subprocess.call(pod_restart, cwd=pod_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    stdout, stderr = proc.communicate()
    o = stdout.decode('utf-8')
    e = stderr.decode('utf-8')
    f.write(" ".join(pod_restart))
    f.write("\n")
    f.write("-"*40)
    f.write("\n")
    f.write(o)
    f.write("\n")
    f.write(e)
    f.write("\n\n")


