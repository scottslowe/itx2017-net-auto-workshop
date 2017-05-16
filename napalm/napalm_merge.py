#!/usr/bin/env python
from __future__ import print_function
from napalm_base import get_network_driver
from getpass import getpass
from pprint import pprint

device1 = {
    'device_type': 'eos',
    'hostname': 'arista-p1.twb-tech.com',
    'username': 'interop',
    'password': getpass(),
    'optional_args': {},
}


for device in [device1,]:

    # Retrieve device_type and driver
    device_type = device.pop('device_type')
    driver = get_network_driver(device_type)

    napalm_conn = driver(**device)

    print()
    print(">>>Test device open")
    napalm_conn.open()

    print(">>>Load merge from file: {}".format(device['hostname']))
    filename = "{}/ntp_config.txt".format(device_type)
    napalm_conn.load_merge_candidate(filename=filename)

    print(">>>Diff")
    print(napalm_conn.compare_config())

    if False:
        print("\n>>>Discard changes")
        print(napalm_conn.discard_config())
        print(napalm_conn.compare_config())

    if True:
        print(">>>Commit change")
        napalm_conn.commit_config()
