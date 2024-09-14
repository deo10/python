# str class

my_name = 'Andrei'
print(len(my_name)) # len - длина строки - lenght
# 6

print(my_name[0]) # print first letter from index
# A

print(my_name[3:6]) # print from 4 till 7 letters (start from 0)
# rei

# methods for str

# upper()
# lower()
# replace()
# index()
# capitalize()
# count()

print(my_name.replace("And", "Bad"))
print(my_name.count('r'))
# print(my_name.index()) # check with chatGPT

# methods for int

user_comment = input("Enter something :") # input is always a str
print(type(user_comment)) # check that type is str
number = int(user_comment) # change type to int

print(type(number)) # check that type is changed

pow_value = (pow(20, number)) # power - возведение в степень
print(pow_value)
print(type(pow_value))  # int

# methods for float (10.9 or 10,9)

float_value = 10.9 # power - возведение в степень
print(float_value)
print(type(float_value))  # float

print(round(float_value))  # округление к целому
print(type(round(float_value))) # int

# complex int

complex_a = 7 + 5j
complex_b = 3 + 6j
sum = complex_a + complex_b

print(sum)
# 10 + 11j

print(type(sum))
# complex



# bool

is_authorize = True # bool - true or false
print(is_authorize)
print(type(is_authorize))  # bool

print(5 > 3)  # True

print(5 < 3)  # False

print('Long string' > 'Long')  # True
print('long string' > 'Short')  # False ! посимвольное сравнение
print('Long string' > 'long')  # False ! 

print([1, 2, 3] == [1, 2, 3])  # True
print({'a': 3} == {'a': 3})  # True
print({'a': 3} == {'a': 5})  # False

print(bool(10)) # True
print(bool('abc')) # True
print(bool([]))  # False !
print(bool([1, 2]))  # True
print(bool(None))  # False !

