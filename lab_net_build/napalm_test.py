#!/usr/bin/env python
from getpass import getpass
from napalm_base import get_network_driver

import logging
logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")

ip_addr = raw_input("Enter IP: ")
password = getpass()
username = 'interop'
optional_args = {}
optional_args['port'] = 22
optional_args['inline_transfer'] = True

driver = get_network_driver('ios')
device = driver(ip_addr, username, password, optional_args=optional_args)

print
print ">>>Test device open"
device.open()
print device.device.timeout

print
print ">>>Test get facts"
device_facts = device.get_facts()
print device_facts

#print 
#print ">>>Load config change"
#device.load_merge_candidate(filename='merge.conf')
#print device.compare_config()
#device.discard_config()
#device.commit_config()

print 
print ">>>Load full config"
device.load_replace_candidate(filename='./INITIAL_CFGS/cisco2.txt')
print device.compare_config()
#device.commit()
