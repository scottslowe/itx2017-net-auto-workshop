""" format() method is helpful. """
from __future__ import print_function

router1 = '10.1.1.1'
router2 = '10.1.17.1'
router3 = '10.1.207.1'

print("\nPrint out three variables in a string")
print("{}  {}  {}".format(router1, router2, router3))

print("\nPrint out three variables in columns 20 chars wide")
print("{:20}{:20}{:20}".format(router1, router2, router3))

print("\nPrint out three variables in columns 20 chars wide (right justify)")
print("{:>20}{:>20}{:>20}".format(router1, router2, router3))

# Print header/trailer lines
print()
print("-" * 80)
print("{:>20}{:>20}{:>20}".format(router1, router2, router3))
print("-" * 80)

print()
