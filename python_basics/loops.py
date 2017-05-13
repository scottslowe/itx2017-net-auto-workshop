from __future__ import print_function

my_dict = {
    'device_name': 'router1',
    'device_type': 'arista_eos',
    'ip_addr': '1.1.1.1',
    'username': 'admin',
    'password': 'hello',
}

my_list = [
    1,
    2,
    'whatever',
    'something',
    2.0,
    True,
    None,
    17,
]


# Loop over the elements in my_list
for element in my_list:
    print(element)
print(">>>>Done1\n\n")

# Loop and break
for element in my_list:
    if element == 'something':
        break
    print(element)
print(">>>>Done2\n\n")

# Loop and continue
for element in my_list:
    if element == 'something':
        continue
    print(element)
print(">>>>Done3\n\n")

# Loop over a dict (will loop over keys automatically)
for key in my_dict:
    print(key)
print(">>>>Done4\n\n")

# Loop over a dict (keys and values)
for k, v in my_dict.items():
    print("{} ----> {}".format(k, v))
print(">>>>Done5\n\n")
