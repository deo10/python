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


name = input("Enter your name: ")
city = input("Enter your city: ")
date = input("Enter your date: ")
print(name, date, city)
print(name.capitalize())  # variable as string has own methods
print(name.count())
print(name.replace)
