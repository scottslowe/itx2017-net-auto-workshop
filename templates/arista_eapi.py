#!/usr/bin/env python

from jsonrpclib import Server
from jsonrpclib import ProtocolError
from pprint import pprint
import ssl

# Disable SSL Certificate validation for self-signed certs
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

user = 'interop'
passwd = 'netauto42'
host = 'arista5.twb-tech.com'

switch = Server('https://{}:{}@{}/command-api'.format( user, passwd, host))

print "\n### Human format:"
response = switch.runCmds(1, ['show version'], 'text')
pprint(response)

print "\n### Machine format:"
response = switch.runCmds(1, ['show version'])
pprint(response)

print "\n### Use the structured data:"
model = response[0]['modelName']
version = response[0]['version']
print "Device {} is {} running EOS version {}\n".format(host, model, version)
