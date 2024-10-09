# create set with some int values
set_name = {124, 10, 15, 22}
print(set_name)
# add one item
set_name.add(200)
print(set_name)
#create another set with some values, some of them should be same as on the first set
set_other = {124, 8, 15, 20}

#find common values on both sets and put it in another set
set_intersection = set_name.intersection(set_other)
print(set_intersection)

#convert final set to list and print
set_to_list = list(set_intersection)
print(set_to_list)

