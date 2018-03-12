#!/usr/bin/env bash
#
# Installs all dotfiles in this directory
# into the home directory using rsync.
#
# ./bootstrap.sh

git pull origin master;

function doIt() {
	rsync \
		--exclude ".git/" \
		--exclude "add_charles_to_docker.sh" \
		--exclude "bootstrap.sh" \
		--exclude "fix_ssh.sh" \
		--exclude "gen_ssh_keys.sh" \
		--exclude "get-docker.sh" \
		--exclude "greenfield_codes.sh" \
		--exclude "install_packages.sh" \
		--exclude "install_pyenv.sh" \
		--exclude "jupiter-apt-stash.txt" \
		--exclude "jupiter_install_packages.sh" \
		--exclude "make_user_charles.sh" \
		--exclude "pre_bootstrap.sh" \
		--exclude "python_install.sh" \
		--exclude "python_setup.sh" \
		--exclude "remove_packages.sh" \
		--exclude "set_machine_name.sh" \
		--exclude "README.md" \
		--exclude "LICENSE" \
		-avh --no-perms . ~;
	source ~/.bash_profile;
}

if [ "$1" == "--force" -o "$1" == "-f" ]; then
	doIt;
else
	read -p "This may overwrite existing files in your home directory. Are you sure? (y/n) " -n 1;
	echo "";
	if [[ $REPLY =~ ^[Yy]$ ]]; then
		doIt;
	fi;
fi;
unset doIt;
