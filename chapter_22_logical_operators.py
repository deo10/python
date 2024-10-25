# logical opeartors

# not -> bool
# and -> values
# or -> values

not 10 # False
not 0 # True
not 'abc' # False
not '' # True
not True # False
not None # True

not not 10 # True
not not 0 # False
not not 'abc' # True
not not '' # False
not not True # True
not not None # False

my_list = [] # False
print(not my_list) # True
print(not not my_list) # False





# AND
#   value1 and value2

#   if value1 is False:
#       1. value2 ignored
#       2. return value1

my_list = [] # False
other_list = ['a', 'b'] # True
print(my_list and other_list) # my_list

my_list = [] # False
my_list and print('list is not empty', my_list)
# Nothing

my_list = [1, 2] # True
my_list and print('list is not empty', my_list)
# list is not empty [1, 2]


# OR
#   value1 or value2

#   if value1 is True:
#       1. value2 ignored
#       2. return value1

my_list = [1, 2] # True
other_list = ['a', 'b'] # True
print(my_list or other_list) # my_list


# create 2 dict with same keys\values
# print "dicts are queval" if first dict = second dict

dict1 = {
    'brand': 'Toyota',
    'price': 10000
}

dict2 = {
    'brand': 'Toyota',
    'price': 1000
}

compare = dict1 == dict2
compare and print('dicts are queval')
compare or print('dicts are NOT queval')