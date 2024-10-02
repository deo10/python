# Tuple
# cannot delete or add items in tuple

my_fruits = ('apple', 'banana', 'lime')
other_fruits = ('lime', 'apple', 'banana')

print(my_fruits == other_fruits)
# False
# order is crucial in tuple

print(my_fruits[0])
# apple

print(my_fruits[-1])
# lime

# you can change values inside tuples if they are dict (example)

users = (
    {
        'user_id': 132,
        'user_name': "Alice"
    },
    {
        'user_id': 122,
        'user_name': "Andrei"
    }
)

print(users[0]['user_id'])
# 132
users[0]['user_id'] = 100
print(users[0]['user_id'])
# 100

#tuple from vars
brand = 'Honda'
bike_price = 25000
engine_vol = 1.2

my_bike_tuple = (brand, bike_price, engine_vol)

print(my_bike_tuple)
# tuple will take values from variables

#get values by index
#print(my_bike_tuple[10])
# error of index

#add one tuple to another
all_in_one = users + my_bike_tuple
print(all_in_one)
# union completed

# methods for tuple - count and index

#count
print(my_bike_tuple.count(25000))
# 1

#index
print(my_bike_tuple.index(25000))
# 1 - index value for 25000 is 1
print(my_bike_tuple.index(1.2))
# 2

#convert to list and back to tuple

my_bike_tuple_list = list(my_bike_tuple)
my_bike_tuple_list.append("value_to_add")

print(my_bike_tuple_list)

my_bike_tuple = tuple(my_bike_tuple_list)
print(my_bike_tuple)

#practical with tuple
my_nums = (10, 5, 12, 5, 44, 5, 100)
my_nums_1 = my_nums.index(5)
print(my_nums_1)
my_nums_2 = my_nums.index(5, my_nums_1 + 1)  #looking for 5 starting from 1 (my_nums_1)
print(my_nums_2)
my_nums_3 = my_nums.index(5, my_nums_2 + 1)  #looking for 5 starting from 3 (my_nums_2)

print(my_nums_3)