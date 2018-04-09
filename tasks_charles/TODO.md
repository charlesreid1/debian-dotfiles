pyenv:
- <s>python installation: pyenv installs ok, but just prints out what you're supposed to do
- need to add next step, install conda/py distribution</s>


python:
- move python install to install python


install conda:
- <s>add install conda script: https://git.charlesreid1.com/dotfiles/dahak-yeti/raw/branch/master/tasks_user/install_conda.py
- fix install conda script - this script is causing trouble because we don't source `~/.bash_profile` before running it, so it can't find pyenv
- add install conda to charles initial task script
- install conda is .sh and should be .py
- set executable bit on install conda</s>


docker:
- remove docker init


no interactivity:
- if a private key already exists, interactive, asks y/n, just answer n and use existing key


codes deployment:
- deploy_codes_docker.sh points to wrong git loc
- setup_charlesreid1_htdocs.py tries to modify /www
- need to check hostname when /www
- setup_charlesreid1_pelican.py line 20 env -> environ
- https on port 3000 is broken - exposed directly - requires gitea server to have a cert for charlesreid1.com
- deploy_codes_docker.sh should not make, should fix git@git


sudo script:
- add_charles_to_groups.sh should include SUDO
- if that doesn't work, make passwordless sudo access: "ubuntu ALL=(ALL) NOPASSWD:ALL" to /etc/sudoers
- print instructions: if you are on AWS, you need to add your public key to the user's authorized keys, or enable password ssh

