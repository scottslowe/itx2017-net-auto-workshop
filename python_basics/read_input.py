from __future__ import print_function

# Python2/3 why do you need to be this way:
try:
    ip_addr = raw_input("Enter an IP address: ")
except NameError:
    ip_addr = input("Enter an IP address: ")

print("You entered: {}".format(ip_addr)) 
