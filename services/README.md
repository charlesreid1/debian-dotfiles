# systemd services

## docker-compose

To run a docker pod on boot, create a systemd service 
called `dockerpod-charlesreid1.service` that calls docker-compose
with the desired docker-compose file.

This boils down to the docker-compose command with
the `-f` flag to point to the particular docker-compose file:

```
docker-compose -f $HOME/codes/docker/pod-charlesreid1/docker-compose.yml up
```

### The service

The service is in the file `dockerpod-charlesreid1.service`

### Installing the service

To install the service, put it in the `/etc/systemd/system/` directory.

### Running the service

Run the command by starting or stopping the dockerpod-charlesreid1 service.

Enable the service at startup:

```
sudo systemctl enable dockerpod-charlesreid1.service
```

Now start up the service:

```
sudo systemctl start dockerpod-charlesreid1.service
```

Monitor the docker containers using docker ps:

```
docker ps
```

To stop the containers, use systemctl:

```
sudo systemctl stop dockerpod-charlesreid1.service
```


