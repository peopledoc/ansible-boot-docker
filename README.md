Boot-docker
==============

This role creates the docker containers for the hosts who ends with `.lxc` and
add them to the dynamic inventory of ansible with the right variables
(`ansible_connection=docker`, ...).

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
* `boot_docker_image` is an available docker image


Example
-------

### Inventory

This role suppose the following inventory :

```ini
[python]
app1.lxc boot_docker_image=registry.fedoraproject.org/f26/python3

[debian]
app2.lxc boot_docker_image=debian:stable
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
