# ZIP
# example of union for 2 list into pairs (tuple)

my_fruits = ['apple', 'banana', 'orange']
quantities = [10, 12, 14]

fruit_quan_zip = zip(my_fruits, quantities) # without limit of objects

print(fruit_quan_zip)
#<zip object at 0x000001C96C6E3B00>

fruit_quan_list = list(fruit_quan_zip)
print(fruit_quan_list)
#[('apple', 10), ('banana', 12), ('orange', 14)]


# example of union for 2 list into dict

my_fruits = ['apple', 'banana', 'orange']
quantities = [10, 12, 14]

fruit_quan_zip = zip(my_fruits, quantities) # only two objects !

print(fruit_quan_zip)
#<zip object at 0x000001C96C6E3B00>

fruit_quan_dict = dict(fruit_quan_zip)
print(fruit_quan_dict)
# {'apple': 10, 'banana': 12, 'orange': 14}

