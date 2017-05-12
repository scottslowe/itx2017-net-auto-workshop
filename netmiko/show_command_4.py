#!/usr/bin/env python
from __future__ import print_function
from netmiko import ConnectHandler
from my_devices import device_list


for device in device_list:

    net_connect = ConnectHandler(**device)
    command = 'show ip int brief'

    # Send show command down channel
    show_ip = net_connect.send_command(command)

    # Display output
    print("\n")
    print(net_connect.find_prompt())
    print("-" * 80)
    print(show_ip)
    print("-" * 80)
    print("\n")
