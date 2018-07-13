import testinfra

localhost = testinfra.get_host('local://')


def test_containers():

    # Check container exists
    localhost.check_output('docker container inspect container1-test')

    # Check container doesn't exist
    cmd = localhost.run('docker container inspect anotherhost')
    assert cmd.rc == 1

    # Check network has been created
    localhost.check_output('docker network inspect ansible-boot-docker-net')


def test_port_bindings():
    cmd = localhost.run(
        "docker inspect -f '{{.HostConfig.PortBindings}}' container1-test"
    )

    assert 'map[80/tcp:[{0.0.0.0 8080}]]' in cmd.stdout


def test_volumes_binds():
    cmd = localhost.run(
        "docker inspect -f '{{.HostConfig.Binds}}' container1-test"
    )

    assert '/tmp:/tmp/host_tmp:ro' in cmd.stdout
