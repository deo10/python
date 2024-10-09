# SET

# no order, only unique items, generally same type objects

my_fruits = {'apple', 'banana', 'lime'}  # set

post_ids = {151, 245, 167, 167, 151}
print(post_ids)
# {151, 245, 167} - duplicates were removed

# useful when you have a list with duplicates, then you convert it to set and all duplicates were removed

my_fruits = {'apple', 'banana', 'lime'} 
other_fruits = {'lime', 'banana', 'apple'}

print(my_fruits == other_fruits)
# True
# useful to check if the items are the same even the order is different

# there is no way to get value by index in set
# it's not possible to add list or dict inside the set
# it's not possible to remove items from set using del

post_ids = {(151, 245), 167, 167, 151}
print(post_ids)
# {(151, 245), 167, 167, 151} - it's fine to add tuple as it's non changeble

# adding values to set
post_ids = {151, 245, 167, 167, 151}
post_ids.add(1024)
print(post_ids)
# {151, 245, 167, 1024} - value added to the set


# union of the sets
post_ids = {151, 245, 167}
other_ids = {161, 265, 157, 167}

union_ids = post_ids.union(other_ids) # union_ids = post_ids | (other_ids)
print(union_ids)
# {151, 245, 167, 161, 265, 157} - duplicates removed


# intersection (what is present on both)
post_ids = {151, 245, 167}
other_ids = {161, 265, 157, 167}

intersection_ids = post_ids.intersection(other_ids)
print(intersection_ids)
# {167} - shows what is present on both sets
print(post_ids.intersection(other_ids)) # print(post_ids & (other_ids))
# {167} - shows what is present on both sets



# issubset - check that is one set is part of the other set
post_ids = {10, 5, 35}
other_ids = {20, 5, 12, 10, 35, 161, 265, 157, 167}

issubset_ids = post_ids.issubset(other_ids)
print(issubset_ids)
# True - all the items from the post_ids are present on other_ids

# difference
post_ids = {10, 5, 35}
other_ids = {20, 5, 12, 10, 35, 161, 265, 157, 167}

diff_ids = other_ids.difference(post_ids) # diff_ids = other_ids - (post_ids) 
print(diff_ids)
# {161, 167, 265, 12, 20, 157}

# discard - remove from values from set
other_ids = {20, 5, 12, 10, 35, 161, 265, 157, 167}

print(other_ids.discard(10)) # discard will NOT throw an error if there is no such value !
# None
print(other_ids)
# {20, 5, 12, 35, 161, 265, 157, 167}

# remove 
other_ids = {20, 5, 12, 10, 35, 161, 265, 157, 167}

print(other_ids.remove(10)) # remove will throw an error if there is no such value !
# None
print(other_ids)
# {20, 5, 12, 35, 161, 265, 157, 167}

# copy
other_ids = {20, 5, 12, 10, 35, 161, 265, 157, 167}
copied_ids = other_ids.copy()

print(copied_ids)
# {20, 5, 12, 10, 35, 161, 265, 157, 167}

# simmetric diff

post_ids = {151, 245, 167, 10}
other_ids = {151, 245, 167, 11}

print(other_ids.symmetric_difference(post_ids))
# {11, 10} - unique present on both

a = {151, 245, 167, 10}
b = {151, 245, 167, 11}

print((a | b) - (a & b))  # | is union; - is diff; & is intersection;
# {11, 10} - unique present on both
