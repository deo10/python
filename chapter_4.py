# objects

# imutable objects - if new value is assign then new object will be created

str
int
bool
float
tuple
range
None

# mutable objects - if new value would be assign then existing object will be changed

list
dict
set
#user-defined-classes

#  id of the variable

number = 10             # create variable
print(id(number))       # print id of the variable

other_number = number     # copy var to another variable
print(id(other_number))   # print id of the new var - should be the same
print(type(other_number)) # print class type of var

# example of the multi string with """ message """
test_msg = """trata
ta
ta
tttra"""

print(test_msg)
