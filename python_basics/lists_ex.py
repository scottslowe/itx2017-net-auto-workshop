from __future__ import print_function

# Create a list (zero-indexed)
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

print(my_list)

# Access a list element
print(my_list[3])

# Change a list element
my_list[3] = 'new value'
print(my_list)

# Access last element of list
print(my_list[-1])

# List slices
print(my_list[2:5])
