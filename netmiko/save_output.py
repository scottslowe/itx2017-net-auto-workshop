#!/usr/bin/env python
from __future__ import print_function
from netmiko import ConnectHandler
from my_devices import device_list


command = "show run"
base_dir = "/home/kbyers/configs"

for device in device_list:
    net_connect = ConnectHandler(**device)

    # Determine name of device
    hostname = net_connect.base_prompt
    filename = "{}/{}.txt".format(base_dir, hostname)

    # Send show command down channel
    print("Retrieving output: {}".format(hostname))
    output = net_connect.send_command(command)

    with open(filename, "wt") as f:
        f.write(output)
