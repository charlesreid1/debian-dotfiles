#!/bin/bash

groupadd charles
sudo su -c "useradd charles -s /bin/bash -m -g charles -G sudo"
chpasswd << 'END'
charles:zeno135
END

