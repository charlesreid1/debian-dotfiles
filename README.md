# Debian Server Dotfiles

Repository containing dotfiles and scripts for bootstrapping 
from a fresh bare-metal cloud node to a fully-configured node.

This hard-codes the user `charles` so it should be edited before general use.


## Components

This repo has the following components:

* tasks to run on boot
* dotfiles (and scripts) to install on boot

The user is also provided with:

* crontabs
* startup services


## Quick Start

The quickest way to get started with this repo is to use the scripts in `cloud_init`.

This directory contains `user_data_machinename`, 
a one-liner pipe-to-bash that will:

* bootstrap the entire repository from scratch
* run the sudo tasks as sudo
* switch to the regular user
* run the regular user tasks as regular user

This gives you a fully hands-free configuration.

You should create a new `user_data` script 
for each new machine.

[Link to dotfile instructions](https://git.charlesreid1.com/dotfiles/vanilla)


## The `tasks/` Directory

The entrypoint for everything is the `tasks/` directory.

`tasks/sudo_all.sh` script should be run as sudo to run all sudo tasks.

`tasks/charles_all.sh` script should be run as charles to run all regular user tasks.

The task scripts are path-independent and can be run from anywhere.

They automatically detect the location of the script to determine the location
of neighboring task scripts that need to be initiated.


### `sudo_all.sh` script

The `sudo_all.sh` script runs the tasks in the following order:

* system tasks
* install tasks
* secrets tasks
* deployment tasks
* clone tasks

Run with the hostname as the only argument:

```
$ /path/to/dotfiles/tasks/sudo_all.sh <hostname>
```


### `charles_all.sh` script

The `charles_all.sh` script runs the tasks in the following order:

* system tasks
* install tasks
* secrets tasks
* deployment tasks
* clone tasks

Run without an argument:

```
$ /path/to/dotfiles/tasks/charles_all.sh 
```


## The `dotfiles/` Directory

This directory contains a set of dotfiles to install to set up the machine.

Run the `bootstrap.sh` script to copy these dotfiles into the home directory.

```
$ cd dotfiles
$ ./bootstrap.sh    # ask confirmation
$ ./bootstrap.sh -f # do not ask confirmation
```

**NOTE:** This is run by the main tasks scripts.
It should be manually re-run anytime your dotfiles
change.

**NOTE:** On running the bootstrap script, any changes
to your dotfiles in your home directory will be 
wiped out, so make sure you save any changes
(or, make them to the dotfiles in the repository).



## The `crontab/` Directory

Contains regular user and sudo crontab files for various hosts.

Install by editing your crontab, `crontab -e`.

See [`crontab/README.md`](/crontab/README.md).


## The `services/` Directory

Contains startup services that can be installed.

* `dockerpod-charlesreid1.service` - runs docker-compose pod running site

See [`services/README.md`](/services/README.md).


## The `motd/` Directory

Contains a special message of the day to display at login for each machine.

See [`motd/README.md`](/motd/README.md).

