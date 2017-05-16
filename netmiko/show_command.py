#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

net_connect = ConnectHandler(device_type='cisco_ios', host='cisco-p6.twb-tech.com', username='interop', password=getpass())
show_arp = net_connect.send_command("show ip int brief")
print(show_arp)
