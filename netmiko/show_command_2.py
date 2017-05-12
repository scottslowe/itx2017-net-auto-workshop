#!/usr/bin/env python
from __future__ import print_function
from netmiko import ConnectHandler
from getpass import getpass

device1 = dict(
    device_type='cisco_ios',
    host='cisco1.twb-tech.com',
    username='interop',
    password=getpass()
)

for device in [device1,]:

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
