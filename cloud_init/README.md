# cloud init scripts

This directory contains scripts that should be uploaded
when creating a new cloud node. This will run admin tasks,
user tasks, and install dotfiles.

In AWS, you can include the cloud init script as "User Data".
See [User Data](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html)
in the AWS docs for more info.

Using Linode, you can simply run the one-liner
to run the entire script immediately after logging 
in as the root user.

[digital ocean guide to cloud-init](https://www.digitalocean.com/community/tutorials/how-to-use-cloud-config-for-your-initial-server-setup)


## Notes

problems with pasting bash script with shebang
directly into aws user data.

## Machines

this has been tested out for blackbeard

krash was already too far along to need this

jupiter has not been addressed yet

