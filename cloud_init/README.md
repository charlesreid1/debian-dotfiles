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

