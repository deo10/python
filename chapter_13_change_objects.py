## non changeable objects ##
# same id for var and value

my_number = 10
print(id(my_number))
# 140735836130008
other_number = 10
print(id(other_number))
# 140735836130008
print(id(10))
# 140735836130008

first_num = 10
second_num = first_num

print(id(first_num))
print(id(second_num))
# 140735836130008
# 140735836130008

second_num += 5
print(second_num)
print(first_num)
# 15 - new object created
# 10

print(id(second_num))
print(id(first_num))
# 140735836130168 - changed !
# 140735836130008

########################
## Changeable objects ##

my_list = [1, 2, 3]
print(id(my_list))
# 1997143415040
other_list = [1, 2, 3]
print(id(other_list))
# 1997143413120 - different !
print(id([1, 2, 3]))
# 1997143702400 - also unique

other_list.append(4)
print(other_list)  # [1, 2, 3, 4]
print(id(other_list))
# 2350193643904 - changed !

my_dict = {
    'name': 'Andrei',
    'title': "DevOps"
}
print(id(my_dict))
# 2071527782656
dict_copy = my_dict # copy (actually a link)
# dict_copy = my_dict.copy() # this copy will create unique id and would be separate, no a link
print(id(dict_copy))
# 2071527782656 - same !

my_dict['review_num'] = 5
print(my_dict)
# {'name': 'Andrei', 'title': 'DevOps', 'review_num': 5}
print(id(my_dict))
# 2071527782656
print(id(dict_copy))
# 2071527782656 - still the same

# another example with unique dicts

dict_info = {
    'name': 'Andrei',
    'title': "DevOps"
}

dict_info_2 = {
    'name': 'Andrei',
    'title': "DevOps"
}

print(id(dict_info))
# 1836074479616 - unique
print(id(dict_info_2))
# 1836074548992 - unique

dict_info['review_num'] = 5
print(dict_info)
# {'name': 'Andrei', 'title': 'DevOps', 'review_num': 5}
print(id(dict_info))
# 1836074479616 - same after change
print(dict_info_2)
# {'name': 'Andrei', 'title': 'DevOps'}
print(id(dict_info_2))
# 1836074548992 - same and no change in values


# example with dict that has list (changeable object) and because of this
# we will have unique id for copy of dict, but link for a list inside

dict_with_list = {
    'name': 'Andrei',
    'list_name': []
}

copy_dict_with_list = dict_with_list.copy()

print(id(dict_with_list))
# 2209852042368 - unique
print(id(copy_dict_with_list))
# 2209848654080 - unique

# but if we change value in list it would be updated on both
copy_dict_with_list['list_name'].append('Great job!')
print(copy_dict_with_list)
# {'name': 'Andrei', 'list_name': ['Great job!']} - updated
print(id(dict_with_list))
# 2209852042368 - no change for id
print(id(copy_dict_with_list))
# 2209848654080 - no change for id

#but
print(dict_with_list)
# {'name': 'Andrei', 'list_name': ['Great job!']} - list updated too

###
# example of deepcopy - full copy with all included values

from copy import deepcopy

new_dict_with_list = {
    'name': 'Andrei',
    'list_name': []
}

deepcopy_dict_with_list = deepcopy(new_dict_with_list) # copy using deepcopy

deepcopy_dict_with_list['list_name'].append('Great job!') # update the list

#check the change
print(new_dict_with_list)
print(deepcopy_dict_with_list)
# {'name': 'Andrei', 'list_name': []}
# {'name': 'Andrei', 'list_name': ['Great job!']}


