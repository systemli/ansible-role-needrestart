import pytest

from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


@pytest.mark.parametrize("name", [
    ("needrestart"),
])
def test_packages(Package, name):
    assert Package(name).is_installed
