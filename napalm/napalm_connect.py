#!/usr/bin/env python
from __future__ import print_function
from napalm_base import get_network_driver
from getpass import getpass
from pprint import pprint

driver = get_network_driver('eos')
device = driver('arista5.twb-tech.com', 
                username='interop',
                password=getpass())

print()
print(">>>Test device open")
device.open()
