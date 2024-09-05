## Classes ##

# class string
# object str - str 'Andrei'
# method
# function

# class integer
object - int('10')

# class bool
bool - True - False

# class list
[1, 2, 3, 4]

# class dictionary
{'min': 5, 'max': 10}

## Functions ##

print  # embedded function
print("Hello World")
type()
id()
sum()
input()
int()
str()
# etc.

# def - defenition custom function


def my_fn(a, b):
    a = a + 1
    c = a + b
    return c


name = input("Enter your name: ")  # variable name with embedded function
# embedded function to view the variable, by default it's str!
print(name)

# function dir()
# shows all the possible names of attributes of an object
print(dir("Python"))  # all for string
print(dir())  # all
print(dir(__builtins__))  # all builtins


name = "Topchik"
print(name.upper())  # upper is methods of the str
print(name.capitalize())  # variable as string has own methods
