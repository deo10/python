#Union of the strings
# we can use + operator

'hello_' + 'Python'
# __add__

# using vars
hello = 'Hello'
world = 'World'

greeting = hello + ' ' + world
print(greeting)
# Hello World


# Format the stings - f-strings

hello = 'Hello'
world = 'World'
time = 8

greeting = f"{hello} {world} at {str(time)} o\'clock"
print(greeting)
# Hello World at 8 o'clock

#task all words should be from capital symbol
greeting = f" {hello} {world} at {str(time)} o\'clock".title()
print(greeting)
# Hello World At 8 O'Clock

#taks 2 - create f string with 4 vars of different types

string = 'number'
integer = 10
boolean = True
float_value = 10.9

greeting = f" {string} is {integer} for {boolean} or {float_value}".title()
print(greeting)
# Number Is 10 For True Or 10.9

