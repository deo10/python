float_value = 10.9 # power - возведение в степень
print(float_value)
print(type(float_value))  # float

print(round(float_value))  # округление к целому
print(type(round(float_value))) # int


print('Andrei')
# print(dir("Python"))
# print(dir()) #all
# print(dir(__builtins__)) #all builtins


name = "Topchik"
print(name.upper())  # upper is attribute of the str


def my_fn(a, b):
    a = 1 + a
    c = a + b
    return c


# name = input("Enter your name: ")
# city = input("Enter your city: ")
# date = input("Enter your date: ")
# print(name, date, city)
# print(name.capitalize())  # variable as string has own methods
# print(name.count())
# print(name.replace)


number = 10             # create variable
print(id(number))       # print id of the variable

other_number = number   # copy var to another variable
print(id(other_number)) # print id of the new var - should be the same