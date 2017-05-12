#!/usr/bin/env python
from __future__ import print_function
from netmiko import ConnectHandler
from getpass import getpass

net_connect = ConnectHandler(
    device_type='cisco_ios',
    host='cisco1.twb-tech.com',
    username='interop',
    password=getpass()
)

print(net_connect.find_prompt())

# Send show command down channel
show_ip = net_connect.send_command("show ip int brief")

# Display output
print("\n")
print("-" * 80)
print(show_ip)
print("-" * 80)
print("\n")
