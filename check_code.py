my_fruits = ['apple', 'banana', 'orange']
quantities = [10, 12, 14]

fruit_quan_zip = zip(my_fruits, quantities)

print(fruit_quan_zip)
#<zip object at 0x000001C96C6E3B00>

fruit_quan_dict = dict(fruit_quan_zip)
print(fruit_quan_dict)