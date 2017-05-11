#!/usr/bin/env python
from __future__ import print_function
from netmiko import ConnectHandler
from my_devices import device_list




try:
    command = raw_input("Enter command: ")
except NameError:
    command = input("Enter command: ")

for device in device_list:

    # Connect
    net_connect = ConnectHandler(**device)

    # Determine name of device
    hostname = net_connect.base_prompt
    filename = "{}.txt".format(hostname)

    # Send show command down channel
    print("Retrieving output: {}".format(hostname))
    output = net_connect.send_command(command)

    with open(filename) as f:
        f.write(output)


#    # Display output
#    print("\n")
#    print("-" * 80)
#    print(output)
#    print("-" * 80)
#    print("\n")
