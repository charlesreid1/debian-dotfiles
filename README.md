# Debian Server Dotfiles

Repository containing dotfiles appropriate for use on Debian servers.

[Link to instructions](https://charlesreid1.com:3000/dotfiles/vanilla)

## run order 

cloud init runs these scripts in a particular order:

As sudo:

* `make_user_charles.sh`
* `install_packages.sh`
* `remove_packages.sh`
* `fix_ssh.sh`
* `get-docker.sh`
* `add_charles_to_docker.sh`
* `set_machine_name.sh`

As user charles:

* `charles_tasks.sh`

Also see [cloud-init](https://charlesreid1.com:3000/dotfiles/cloud-init)

