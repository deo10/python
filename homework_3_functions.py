# create function merge_lists_to_dict
# function should have 2 params
# function should union two lists using embedded function zip
# convert object zip to dict and return it from functiion
# invoke function using two lists as args
# print result of the function invoke

def merge_lists_to_dict(list1, list2):
    convert_to_zip = zip(list1, list2) #union lists
    return dict(convert_to_zip) #convert to dict
    #or return dict(zip(list1, list2)) - less lines

var_list1 = ['apple', 'banana', 'orange']
var_list2 = ['grape', 'mango', 'peach']

result_merge_lists_to_dict = merge_lists_to_dict(var_list1, var_list2)
print(type(result_merge_lists_to_dict))
print(result_merge_lists_to_dict)

print(var_list1) # not changed

#new vars
var_list1 = ['book']
var_list2 = ['took']
result_merge_lists_to_dict = merge_lists_to_dict(var_list1, var_list2)
print(type(result_merge_lists_to_dict))
print(result_merge_lists_to_dict)
