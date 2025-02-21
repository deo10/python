#create empty list
my_list = []

#add elements
my_list.append('word')

val1 = input('Enter 1st element (str): ')
val2 = input('Enter 2nd element (str): ')
val3 = int(input('Enter 3rd element (int): '))
val4 = float(input('Enter 4th element (float): '))
val5 = int(input('Enter 5th element (int): '))

my_list.extend([val1, val2, val3, val4, val5])

print(my_list)

# ask user to change 2 element
new_val2 = input('Enter new 2nd element (str): ')
my_list[1] = new_val2
print(my_list)

# remove element (2 elements)
my_list.pop(1)
print(my_list)

# insert element
my_list.append('inserted')
print(my_list)

# sort the list (ascending order)
my_list = [True, 1, 4.5, 'Word', 100]
sorted_list = sorted(my_list, key=lambda x: (isinstance(x, str), x))
print(sorted_list)

# slice the list
my_list = [True, 1, 4.5, 'Word', 100]
print(my_list[0:2])

# Create a new list that contains the squares of all the numeric elements in `my_list`.
# Print the new list.
squared_list = [x**2 for x in my_list if isinstance(x, (int, float))]
print(squared_list)

