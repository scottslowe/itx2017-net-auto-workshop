from __future__ import print_function

# Numbers
number1 = 7
number2 = 2
number3 = 2.0

print("\nNumbers")
print('-' * 80)
print(type(number1))
print(type(number3))

print("Add: {}".format(number1 + number2))
print("Subtract: {}".format(number1 - number2))
print("Multiply: {}".format(number1 * number2))
print("Division (what?): {}".format(number1 / number2))
print("Division Float: {}".format(number1 / number3))
print('-' * 80)
print("\n\n")



# Strings
str1 = 'hello'
str2 = 'whatever'
str3 = '10.100.17.8'
str4 = 'hello world\n\n\n'

print("\nStrings")
print('-' * 80)
print(type(str1))
# String concatenation
print(str1 + " " + str2)
# Split a string (returns a list)
octets = str3.split(".")
print(octets)
# Strip leading and trailing whitespace
print(str4.strip())
print('-' * 80)
print("\n\n")



# Some other data types
print("\nSome other data types")
print('-' * 80)

my_var = None
print(type(my_var))

bool1 = True
bool2 = False
print(type(my_var))
print(bool1 and bool2)
print(bool1 or bool2)
print('-' * 80)
print("\n\n")
