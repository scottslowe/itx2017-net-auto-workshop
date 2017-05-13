from __future__ import print_function

my_ip = '22.17.7.9'

if '8' in my_ip:
    print("I found 8")
elif my_ip == '22.17.':
    print("I found 22.17")
elif my_ip == '22.17.7.9':
    print("I found 22.17.7.9")
else:
    print("I never found it.")
