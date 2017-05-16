#!/usr/bin/env python
from napalm_base import get_network_driver
from getpass import getpass

driver = get_network_driver('eos')
device = driver('arista-p2.twb-tech.com', username='interop', password=getpass())
device.open()
