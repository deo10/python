# create two vars and define them same values type set ( not copy one to another)
# no order, only unique items, generally same type objects


my_fruits = {'apple', 'banana', 'lime'} 
other_fruits = {'apple', 'banana', 'lime'} 

# print result of the comparison

print(my_fruits == other_fruits) # True
print(id(my_fruits)) #2404347122336
print(id(other_fruits)) #2404347121888

# == or __eq__ checks object in set (both have same unique objects
# id's are different

#compare it with is operator

print(my_fruits is other_fruits) # False
print(my_fruits is not other_fruits) # True
# id's are different

# check if there are specific elements in set using in operator

print('apple' in my_fruits) # True
print('apple' not in my_fruits) # False
print('mango' not in my_fruits) # True





