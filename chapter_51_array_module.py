# Working with ARRAY module in python

from array import array

# create array (massive)
my_int_array = array('i', [4, 10, 5, 7]) # i for array content type - int
# array('i', [4, 10, 5, 7])

print(my_int_array)

# adding value to the array
my_int_array.append(15)
print(my_int_array)
# array('i', [4, 10, 5, 7, 15])
print(my_int_array.count(5))
# 1

# remove value from array
my_int_array.pop(0) # by index
print(my_int_array)
# array('i', [10, 5, 7, 15])

print(len(my_int_array))
#4

for elem in my_int_array:
    print(elem)
# 10
# 5
# 7
# 15

# write array as file
with open('my_array.bin', 'wb') as my_file:
    my_int_array.tofile(my_file)
    
    
#reading array from file

imported_array = array('i') # create new empty array
with open('my_array.bin', 'rb') as my_file:
    imported_array.fromfile(my_file, 3)
    print(imported_array)
# array('i', [10, 5, 7])    

imported_array.reverse()
print(imported_array)
# array('i', [7, 5, 10])