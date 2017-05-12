from __future__ import print_function

my_dict = {
    'device_name': 'router1',
    'device_type': 'arista_eos',
    'ip_addr': '1.1.1.1',
    'username': 'admin',
    'password': 'hello',
}

print(my_dict)

# Access a given key:
print(my_dict['ip_addr'])

# Change a key:
my_dict['ip_addr'] = '200.1.17.2'
print(my_dict['ip_addr'])

# Add a new element:
my_dict['port'] = 22

# Keys (iterable)
print(my_dict.keys())

# Key-Value (iterable)
print(my_dict.items())
