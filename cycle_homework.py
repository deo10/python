# TASK1
# create function dict_to_list that will
# convert dict to list of tuple
# function should take dict and return list of tuples
# each tuple shoudl have pair of key and value from dict
# if the value is int then we need to *2 and put it in tuple


my_dict = {
    'brand': 'Ducati',
    'price': 25000,
}

def dict_to_list(dict_to_change):
    return list(dict_to_change.items())

print(dict_to_list(my_dict)) # gives list of the tuple
# [('brand', 'Ducati'), ('price', 25000)]

my_dict = {
    'brand': 'Ducati',
    'price': 25000
}

def dict_to_list(dict_to_change):
    list_to_change = [] # creating empty list
    for key, value in dict_to_change.items(): # taking key and value from dict as tuple
        if type(value) == int: # check that value is int
            value *= 2 # *2 if yes
        list_to_change.append((key, value)) # adding key and value (tuple) to the list
    return list_to_change
        
print(dict_to_list(my_dict))


# TASK #2
# create function filter_list that would filter list
# function should have two params - list and type of value
# function should return new list that will have only
# values of type that was passed in function invoke as 2nd arg
# func possible to invoke like this filter_list([35, True, 'abc', 10], int) and get [35, 10]

def filter_list(list_param, type_param):
    new_list = []
    for item in list_param:
        if isinstance(item, type_param): # not working correctly, as bool is subclass of int
           new_list.append(item)
    return new_list


print(filter_list([35, True, 'abc', 10], int))

# option #2

def filter_list(list_param, type_param):
    new_list = []
    for item in list_param:
        if type(item) is type_param:
           new_list.append(item)
    return new_list


print(filter_list([35, True, 'abc', 10], int))
print(filter_list([35, True, 'abc', 10], str))
print(filter_list([35, True, 'abc', 10], bool))
# [35, 10]
# ['abc']
# [True]


#option # 3 with filter

def filter_list(list_param, type_param):
    def check_element_type(elem):
        return type(elem) is type_param
    
    return list(filter(check_element_type, list_param))

print(filter_list([35, True, 'abc', 10], int))
print(filter_list([35, True, 'abc', 10], str))
print(filter_list([35, True, 'abc', 10], bool))
# [35, 10]
# ['abc']
# [True]

#option #4 with lambda function

def filter_list(list_param, type_param):
    return list(filter(lambda elem: type(elem) is type_param, list_param))

print(filter_list([35, True, 'abc', 10], int))
print(filter_list([35, True, 'abc', 10], str))
print(filter_list([35, True, 'abc', 10], bool))
# [35, 10]
# ['abc']
# [True]