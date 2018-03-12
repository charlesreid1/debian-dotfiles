#!/bin/bash

sudo su -c "useradd charles -s /bin/bash -m -g charles -G sudo"
sudo chpasswd << 'END'
charles:zeno135
END

#mkdir /home/charles/.ssh
#chown charles:charles /home/charles/.ssh
#chmod 700 /home/charles/.ssh
#touch /home/charles/.ssh/authorized_keys
#chmod 600 /home/charles/.ssh/authorized_keys

