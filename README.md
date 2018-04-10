# Debian Server Dotfiles

Repository containing dotfiles and scripts for bootstrapping 
from a fresh bare-metal cloud node to a fully-configured node.

This hard-codes the user `charles` so it should be edited before general use.

TODO: make username a parameter of the script (`$2`)



## Components

This repo has the following components:

* tasks to run on boot
* dotfiles to install on boot
* scripts to install on boot

The user is also provided with:

* crontabs
* startup services



## Quick Start

The quickest way to get started with this repo is to use the scripts in `cloud_init`.

This directory contains `user_data.sh`, a one-liner pipe-to-bash that will:

* bootstrap the entire repository from scratch
* run the sudo tasks as sudo
* switch to the regular user
* run the regular user tasks as regular user

This gives you a fully hands-free configuration.

[Link to instructions](https://git.charlesreid1.com/dotfiles/vanilla)



## The `tasks/` Directory

The entrypoint for everything is the `tasks/` directory.

`tasks/sudo_all.sh` script should be run as sudo to run all sudo tasks.

`tasks/charles_all.sh` script should be run as charles to run all regular user tasks.

The scripts depend on relative locations,
and should be run like this:

```
$ cd /path/to/debian/tasks
$ ./sudo_all.sh <hostname>
$ ./charles_all.sh
```

or in a script,

```
#!/bin/bash

DIR="/path/to/debian/tasks"
cd $DIR
./sudo_all.sh <hostname>
./charles_all.sh
```

### `sudo_all.sh` script

The `sudo_all.sh` script runs the tasks in the following order:

* system tasks
* install tasks
* secrets tasks
* deployment tasks
* clone tasks

Run without an argument:

```
$ ./sudo_all.sh <hostname>
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
$ ./charles_all.sh
```


## The `dotfiles/` Directory

This directory contains a set of dotfiles to install to set up the machine.

Run the `bootstrap.sh` script to copy these dotfiles into the home directory.

```
$ cd dotfiles
$ ./bootstrap.sh    # ask confirmation
$ ./bootstrap.sh -f # do not ask confirmation
```

## The `scripts/` Directory

Host specific installation scripts.

* `blackbeard/` - hook server
* `jupiter/` - beefy debian node
* `krash/` - charlesreid1 node

See [`scripts/README.md`](/scripts/README.md).


## The `crontab/` Directory

Contains regular user and sudo crontab files for various hosts.

See [`crontab/README.md`](/crontab/README.md).


## The `services/` Directory

Contains startup services that can be installed.

* `dockerpod-charlesreid1.service` - runs docker-compose pod running site

See [`services/README.md`](/services/README.md).


## The `motd/` Directory

Contains a special message of the day to display at login for each machine.

See [`motd/README.md`](/motd/README.md).

