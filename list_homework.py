# task 1
# create list with 5 elements (different type)

list_with_five_elements = [True, 1, 4.5, 'Word', 100]

# delete 3rd element

#list_with_four_elements = list_with_five_elements[:]
list_with_five_elements.pop(2)
print("One element deleted",list_with_five_elements)

# print lenght of the list
print("list lenght",len(list_with_five_elements))
# 4

# change order in the list
#list_with_four_elements.pop(2)  #remove str as not supported by reverse
#print(list_with_four_elements)
#list_with_four_elements.sort(reverse=True)
#print(list_with_four_elements)

list_with_five_elements.reverse()
print("Using different order",list_with_five_elements)

# create new list with 2 elements
new_list = [12, 109]

# add values from 1st list to the second list
#union_list = new_list + list_with_five_elements
list_with_five_elements.extend(new_list)
print("Adding one list to another",list_with_five_elements)

#task 2
# create 2 lists
list_1 = [4, 5, 6]
list_2 = [1, 2, 3]

# union lists
union_lists = list_1 + list_2
# print(dir(list))

# union via magic __add__
union_list_magic = list_1.__add__(list_2)
print("Adding one list to another using magic",union_list_magic)

