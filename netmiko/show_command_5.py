#!/usr/bin/env python
from __future__ import print_function
from netmiko import ConnectHandler
from my_devices import device_list


try:
    command = raw_input("Enter command: ")
except NameError:
    command = input("Enter command: ")

for device in device_list:
    net_connect = ConnectHandler(**device)

    # Send show command down channel
    output = net_connect.send_command(command)

    # Display output
    print("\n")
    print(net_connect.find_prompt())
    print("-" * 80)
    print(output)
    print("-" * 80)
    print("\n")
