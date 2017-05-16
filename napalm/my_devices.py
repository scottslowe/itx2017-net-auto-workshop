from getpass import getpass

password=getpass()

cisco1 = dict(
    device_type='cisco_ios',
    host='cisco-p1.twb-tech.com',
    username='interop',
    password=password
)

cisco2 = dict(
    device_type='cisco_ios',
    host='cisco-p2.twb-tech.com',
    username='interop',
    password=password
)

arista1 = dict(
    device_type='arista_eos',
    host='arista-p1.twb-tech.com',
    username='interop',
    password=password
)

arista2 = dict(
    device_type='arista_eos',
    host='arista-p2.twb-tech.com',
    username='interop',
    password=password
)

arista3 = dict(
    device_type='arista_eos',
    host='arista-p3.twb-tech.com',
    username='interop',
    password=password
)

arista4 = dict(
    device_type='arista_eos',
    host='arista-p4.twb-tech.com',
    username='interop',
    password=password
)

juniper1 = dict(
    device_type='juniper_junos',
    host='juniper-p1.twb-tech.com',
    username='interop',
    password=password
)

juniper2 = dict(
    device_type='juniper_junos',
    host='juniper-p2.twb-tech.com',
    username='interop',
    password=password
)

device_list = [
    cisco1,
    cisco2,
    arista1,
    arista2,
    arista3,
    arista4,
    juniper1,
]

device_list_mv = [
    cisco1,
    arista1,
    juniper1,
]
