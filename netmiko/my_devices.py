from getpass import getpass

password=getpass()

cisco1 = dict(
    device_type='cisco_ios',
    host='cisco1.twb-tech.com',
    username='interop',
    password=password
)

cisco2 = dict(
    device_type='cisco_ios',
    host='cisco2.twb-tech.com',
    username='interop',
    password=password
)

arista5 = dict(
    device_type='cisco_ios',
    host='arista5.twb-tech.com',
    username='interop',
    password=password
)

arista6 = dict(
    device_type='cisco_ios',
    host='arista6.twb-tech.com',
    username='interop',
    password=password
)

arista7 = dict(
    device_type='cisco_ios',
    host='arista7.twb-tech.com',
    username='interop',
    password=password
)

arista8 = dict(
    device_type='cisco_ios',
    host='arista8.twb-tech.com',
    username='interop',
    password=password
)


device_list = [
    cisco1,
    cisco2,
    arista5,
    arista6,
    arista7,
    arista8,
]
