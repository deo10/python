# task 1
# create empty dict

my_dict = {}

# three times ask user to
# enter key
# enter value
# in total should be 6 inputs

key_1 = input("Enter key_1: ")
value_1 = input("Enter value_1 for key_1: ")
key_2 = input("Enter key_2: ")
value_2 = input("Enter value_2 for key_2: ")
key_3 = input("Enter key_3: ")
value_3 = input("Enter value_3 for key_3: ")

my_dict[key_1] = value_1 
my_dict[key_2] = value_2
my_dict[key_3] = value_3

# my_dict = {
#     key_1: value_1,
#     key_2: value_2,
#     key_3: value_3,
# }

print(my_dict)

#add and del few keys

my_dict['New_key_1'] = 'New_key_value_1'
my_dict['New_key_2'] = 'New_key_value_2'

print(my_dict)

del my_dict["New_key_1"]
del my_dict["New_key_2"]

print(my_dict)

