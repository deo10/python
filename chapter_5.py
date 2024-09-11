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


