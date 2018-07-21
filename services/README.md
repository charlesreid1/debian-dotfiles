# systemd services

the systemd services are named `X.service`.

## General procedure

Define the service: create a file `X.service` to perform your task.

Here's an example that persistently restarts a service anytime it stops:

```
[Unit]
Description=< your description here >
Requires=< any requirements, for example docker.service >
After=< requirements to wait for, for example docker.service >

[Service]
Restart=always
ExecStart=<command to run your service, usually docker-compose -f /my/docker-compose.yml up >
ExecStop=<command to stop running your serivce, usually docker-compose -f /my/docker-compose.yml down >

[Install]
WantedBy=default.target
```

Install the service: put it in the `/etc/systemd/system` directory.

Enable/disable the service: add/remove service in the list of available services via:

```
sudo systemctl enable X.service
sudo systemctl disable X.service
```

Start/stop the service: use the start/stop verbs to start/stop the service:

```
sudo systemctl start X.service
sudo systemctl stop X.service
```

<br />
<br />

## krash: charlesreid1 docker pod

Runs pod-charlesreid1 on krash.

To run a docker pod on boot, create a systemd service 
called `dockerpod-charlesreid1.service` that calls docker-compose
with the desired docker-compose file.

This boils down to the docker-compose command with
the `-f` flag to point to the particular docker-compose file:

```
docker-compose -f $HOME/codes/docker/pod-charlesreid1/docker-compose.yml up
```

### The service

The service is defined in the file `dockerpod-charlesreid1.service`.

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

<br />
<br />


## blackbeard: bots docker pod

Runs pod-bots the Apollo, Ginsberg, and Paradise Lost bot flocks on blackbeard.

To run the bots docker pod on boot, install the systemd service
for the bot pod.

### The service

The service is defined in the file `dockerpod-bots.service`.

### Installing the service

To install the service, put it in the `/etc/systemd/system/` directory.

### Running the service

To install the bot pod service:

```
sudo systemctl enable dockerpod-bots.service
```

To start the bot pod service: 

```
sudo systemctl start dockerpod-bots.service
```

To stop the containers:

```
sudo systemctl stop dockerpod-bots.service
```

<br />
<br />

## blackbeard: webhook docker pod

This runs pod-webhooks on blackbeard (webhooks server and nginx server serving subdomains).

This boils down to the docker-compose command with
the `-f` flag to point to the particular docker-compose file:

```
docker-compose -f $HOME/codes/docker/pod-webhooks/docker-compose.yml up
```

The webhooks pod runs two services:

* Static content server for subdomain pages (nginx)
   * [d-nginx-subdomains](https://git.charlesreid1.com/docker/d-nginx-subdomains)
   * Example: hook.charlesreid1.com
   * Example: pages.charlesreid1.com

* Captain Hook webhook server (python + flask)
   * [b-captain-hook](https://git.charlesreid1.com/bots/b-captain-hook)
   * Also runs captain hook canary







