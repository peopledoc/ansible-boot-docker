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
* `boot_docker_host` name and hostname of the container, by default
`inventory_hostname` is used (and available using `host` variable).

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
