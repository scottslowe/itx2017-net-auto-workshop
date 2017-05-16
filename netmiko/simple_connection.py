#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

net_connect = ConnectHandler(device_type='cisco_ios', host='cisco-p1.twb-tech.com', username='interop', password=getpass())
print(net_connect.find_prompt())
