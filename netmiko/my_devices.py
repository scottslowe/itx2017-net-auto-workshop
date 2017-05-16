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

arista5 = dict(
    device_type='arista_eos',
    host='arista-p1.twb-tech.com',
    username='interop',
    password=password
)

arista6 = dict(
    device_type='arista_eos',
    host='arista-p2.twb-tech.com',
    username='interop',
    password=password
)

arista7 = dict(
    device_type='arista_eos',
    host='arista-p3.twb-tech.com',
    username='interop',
    password=password
)

arista8 = dict(
    device_type='arista_eos',
    host='arista-p4.twb-tech.com',
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
