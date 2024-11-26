# !without cycle
i = 10

print(i) # 10
i *= 2

print(i) # 20
i *= 2

print(i) # 40
i *= 2

# get value from list !without cycle

my_fruits = ['apple', 'banana', 'lime']

print (my_fruits[0]) # apple
print (my_fruits[1]) # banana
print (my_fruits[2]) # lime

# get values from dict !without cycle

my_object = {
    'x': 10,
    'y': True,
    'z': 'abc'
}

print (my_object['x']) # 10
print (my_object['y']) # True
print (my_object['z']) # abc



# cycle used for DICT / LIST / TUPLE / SET / RANGE / STR

# types: for...in... / while

#CYCLE for..in..

# for Element in Subsequence:
  # Actions with each element 


# for in for LIST
my_fruits = ['apple', 'banana', 'lime']

for elem in my_fruits:
    print(elem)
# apple
# banana
# lime


# for in for TUPLE
video_info = ('1920x1080', True, 27)

for elem in video_info:
    print(elem)
# 1920x1080
# True
# 27

# for in for DICT
my_object = {
    'x': 10,
    'y': True,
    'z': 'abc'
}

for key in my_object:
    print(key, my_object[key]) # getting key and value
# x 10
# y True
# z abc

# with items that is available only in dict
for item in my_object.items():
    print(item) # tuple -> ('x', 10) / ('y', True) / ('z', 'abc')
    key, value = item # unpack the tuple (not dict, converted)
    print(key, value)
# x 10
# y True
# z abc


my_object = {
    'x': 10,
    'y': True,
    'z': 'abc'
}
for key, value in my_object.items():
    print(key, value)
# x 10
# y True
# z abc

# for in for SET

info = {1435, 4317, 2672, 5721}

for id in info:
    print(id)
# Note that the order is different as it's SET
# 2672
# 5721
# 1435
# 4317

# for in for RANGE

for num in range(5):
    print(num)
# 0
# 1
# 2
# 3
# 4

for odd_num in range (3, 10, 2): #start 3 end 10, step 2
    print(odd_num)
# 3
# 5
# 7
# 9

