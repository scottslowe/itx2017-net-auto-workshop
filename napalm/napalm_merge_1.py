#!/usr/bin/env python
from __future__ import print_function
from napalm_base import get_network_driver
from my_devices import device_list_mv
from pprint import pprint


def convert_dict(my_dict):
    """Convert dictionaries from Netmiko format to NAPALM format."""
    new_dict = {}
    for k, v in my_dict.items():
        new_dict[k] = v

    hostname = new_dict.pop('host')
    new_dict['hostname'] = hostname

    device_type = new_dict.pop('device_type')
    new_device_type = device_type.split('_')[1]
    new_dict['device_type'] = new_device_type

    return new_dict


for device in device_list_mv:

    # Modify dictionary format
    device = convert_dict(device)

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
    print(">>>Commit change")
    napalm_conn.commit_config()
