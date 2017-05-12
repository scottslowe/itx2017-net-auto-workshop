#!/usr/bin/env python
from __future__ import print_function
from napalm_base import get_network_driver
from getpass import getpass
from pprint import pprint


pwd = getpass()

arista5 = {
    'device_type': 'eos',
    'hostname': 'arista5.twb-tech.com', 
    'username': 'interop',
    'password': pwd,
    'optional_args': {},
}

cisco1 = {
    'device_type': 'ios',
    'hostname': 'cisco1.twb-tech.com', 
    'username': 'interop',
    'password': pwd,
    'optional_args': {},
}

for device in [arista5, cisco1]:
    device_type = device.pop('device_type')
    driver = get_network_driver(device_type)
    napalm_conn = driver(**device)

    print()
    print(">>>Test device open")
    napalm_conn.open()

    pprint(napalm_conn.get_facts())
