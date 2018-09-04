Boot-docker
==============

This role creates the docker containers for the hosts for which
`boot_docker_image` variable is defined and adds them to the dynamic inventory
of ansible with the right variables (`ansible_connection=docker`, ...).

It will start the containers and join them in the same docker network.

Requirements
------------

* Docker CE
* `docker` python package

Role Variables
--------------

Following variables are optional:
* `boot_docker_network`: name the docker network used by the hosts to
communicate, Docker default network is used if not specified.
* `boot_docker_network_aliases`: list of network aliases for the host
  on the network. Works only if used with `boot_docker_network`.
* `boot_docker_network_ipv4`: ipv4 address of the container in the
  network. Works only if used with `boot_docker_network`.
* `boot_docker_network_ipv6`: ipv6 address of the container in the
  network. Works only if used with `boot_docker_network`.
* `boot_docker_purge_networks`: Remove container from other
  networks when using `boot_docker_network`. Defaults to `true`.
* `boot_docker_host` name and hostname of the container, by default
`inventory_hostname` is used (and available using `host` variable).
* `boot_docker_command`: command to execute when the container starts.
* `boot_docker_ports`: list of published ports following the Docker CLI syntax
  (`['8080:80']`, etc.).
* `boot_docker_volumes`: list of volumes to bind following the Docker CLI syntax
  (`['/host:/container[:ro|rw]']`).

Following variable is required:
* `boot_docker_image` is an available docker image. When this variable isn't
defined or is equal to `False`, container isn't created.

Example
-------

### Inventory

This role supposes the following inventory :

```ini
[python]
app1.example boot_docker_image=registry.fedoraproject.org/f26/python3

[debian]
app2.example boot_docker_image=debian:stable

[container_not_created]
app3.example
```

You should then use `host_vars` or `group_vars` to define other variables :

```yaml
# host_vars/debian.yml

boot_docker_command: sleep infinity
boot_docker_volumes:
  - /tmp/data:/mnt/data:ro
boot_docker_ports:
  - 8080:80
```

### Playbook
------------

```yaml
- hosts: localhost
  roles:
    - role: peopledoc.boot-docker
      vars:
        boot_docker_network: demo-net
        boot_docker_host: 'demo-{{ host }}'
```

License
--------

BSD
