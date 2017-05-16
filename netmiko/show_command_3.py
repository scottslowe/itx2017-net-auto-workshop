#!/usr/bin/env python
from __future__ import print_function
from netmiko import ConnectHandler
from getpass import getpass


pwd = getpass()

device1 = dict(
    device_type='cisco_ios',
    host='cisco-p5.twb-tech.com',
    username='interop',
    password=pwd
)

device2 = dict(
    device_type='arista_eos',
    host='arista-p5.twb-tech.com',
    username='interop',
    password=pwd
)


for device in [device1, device2]:

    net_connect = ConnectHandler(**device)

    print(net_connect.find_prompt())

    # Send show command down channel
    show_ip = net_connect.send_command("show ip int brief")

    # Display output
    print("\n")
    print("-" * 80)
    print(show_ip)
    print("-" * 80)
    print("\n")
