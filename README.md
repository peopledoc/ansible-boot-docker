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

This role need a `project_name` variable to name the docker network used by the
hosts to communicate.

This role suppose the following inventory :

```ini
[sae]
sae.lxc docker_image=sae-base

[rabbitmq]
rabbitmq.lxc docker_image=sae-rabbitmq

```

`docker_image` is a docker image already created and pushed to the registry when
using that role.

This role also read the `JOB_ID` environment variable to containerized Jenkins builds.

Example Playbook
----------------

```yaml
- hosts: localhost
  roles:
    - role: peopledoc.boot-docker
      vars:
        project_name: sae
```

License
--------

BSD
