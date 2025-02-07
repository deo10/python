# list

my_fruits = ['apple', 'banana', 'orange']

post_ids = [1, 2, 5]

user_inputs = [123, 'abc', True, 10.5]

# ! порядок элементов в списке имеет значение
my_fruits = ['apple', 'banana', 'orange']
other_fruits = ['apple', 'orange', 'banana']

print(my_fruits == other_fruits)
# False

my_fruits = ['apple', 'banana', 'orange']
print(len(my_fruits))
# 3 - длина списка

print(my_fruits[0])
# apple
print(my_fruits[1])
# banana
print(my_fruits[2])
# orange
print(my_fruits[-1])
# orange ! last element in the list

my_fruits[0] = 'banana'
print(my_fruits[0])
# banana
print(my_fruits)
# [banana, 'banana', 'orange'] - список изменен через индекс значения

del my_fruits[0]
print(my_fruits)
# ['banana', 'orange'] - список изменен через удаление значения

#список словарей
users = [
    {
        'user_id': 134,
        'user_name': 'Alice'
    },
    {
        'user_id': 831,
        'user_name': 'Bob'
    }
]

print(len(users))
# 2 (list with 2 items)
print(users[1]['user_id'])
# 831 (индекс второго элемента и ключ в словаре)


#использование переменных
my_fruit = 'apple'
other_fruit = 'banana'
new_fruit = 'lime'

all_fruits = [my_fruit, other_fruit, new_fruit]
print(all_fruits)
# ['apple', 'banana', 'lime']

#методы списков

#append - add to the list, in the end of the list
happy_fruits = []

happy_fruits.append('apple')
happy_fruits.append('banana')
happy_fruits.append('lime')

print(happy_fruits)
# ['apple', 'banana', 'lime']

#pop - remove from the list, last item in the list

happy_fruits.pop() #last
happy_fruits.pop(0) #first
removed_element = happy_fruits.pop()
# removed 'apple'
print(removed_element)
# apple - it's possible to save removed item via adding it to the variable

#sort - sort items in the list

post_ids = [245, 151, 762, 167]
post_ids.sort()

print(post_ids)
# [151, 167, 245, 762] - sort by number A-Z

post_ids.sort(reverse=True)
print(post_ids)
# [762, 245, 167, 151] - sort by number Z-A


#конвертация в список
greeting = "Hello from"
greeting_letters = list(greeting)

print(greeting_letters)
# ["H", 'e', 'l', ...] - each letter is item in the list

my_dict = {'a': 10, 'b': True}
my_dict_keys = list(my_dict)

print(my_dict_keys)
# ['a', 'b'] - only keys added to the list

#math functions in list

rating = [2.5, 5.0, 4.3, 3.7]
print(min(rating)) # 2.5
print(max(rating)) # 5.0
print(sum(rating)) # 15.5

print(sum(rating)/len(rating))
# 3.875

#list union
other_rating = [1.2, 4.5, 6.0]

all_ratings = rating + other_rating
print(all_ratings)
# [2.5, 5.0, 4.3, 3.7, 1.2, 4.5, 6.0]

# cut values in list
rating = [2.5, 5.0, 4.3, 3.7]

first_two_ratings = rating[:2]
middle_ratings = rating[1:-1]  # from 1 till the end except last
last_two_ratings = rating[-2:]

list1 = [1, 66, "python", [11, 55, "cat"], [ ], 2.22, True]
print(list1[0:4]) 
# 0 - Start from the element at index 0 (the first element).
# 4 - Go up to, but not including, the element at index 4.
# [1, 66, 'python', [11, 55, 'cat']]

# This line prints a slice of `list1` using the slicing syntax `list1[::3]`.
list1 = [10, 11, 12, 13, 14]
print(list1[::3])
# [10 13]

#    The slicing syntax `list1[::3]` means:
#    - `:` - Start from the beginning of the list.
#    - `:` - Go until the end of the list.
#    - `3` - Use a step of `3`.


# copy lists

my_cars = ['BMW', 'Mercedes']
copied_my_cars = my_cars  #copy by the link

copied_my_cars.append('Audi')  #adding item in one list

print(copied_my_cars)
# ['BMW', 'Mercedes', 'Audi']
print(my_cars)
# ['BMW', 'Mercedes', 'Audi'] - item added on both lists

print(id(my_cars) == id (copied_my_cars))
# True - id of the list is the same

#---copy with new list id - option 1

my_cars = ['BMW', 'Mercedes']
copied_my_cars = my_cars[:]  #copy by slice

copied_my_cars.append('Audi')  #adding item in one list

print(copied_my_cars)
# ['BMW', 'Mercedes', 'Audi']
print(my_cars)
# ['BMW', 'Mercedes'] - item added on one list !

print(id(my_cars) == id (copied_my_cars))
# False - id of the list is NOT the same

#---copy with new list id - option 2

my_cars = ['BMW', 'Mercedes']
copied_my_cars = my_cars.copy()  #copy by copy method

copied_my_cars.append('Audi')  #adding item in one list

print(copied_my_cars)
# ['BMW', 'Mercedes', 'Audi']
print(my_cars)
# ['BMW', 'Mercedes'] - item added on one list !

print(id(my_cars) == id (copied_my_cars))
# False - id of the list is NOT the same

#---copy with new list id - option 3

my_cars = ['BMW', 'Mercedes']
copied_my_cars = list.my_cars  #copy by list function

copied_my_cars.append('Audi')  #adding item in one list

print(copied_my_cars)
# ['BMW', 'Mercedes', 'Audi']
print(my_cars)
# ['BMW', 'Mercedes'] - item added on one list !

print(id(my_cars) == id (copied_my_cars))
# False - id of the list is NOT the same

