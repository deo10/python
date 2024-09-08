# epressions

import datetime  # импортирование модуля
5 + 5
"Hello " + "World!"
5 > 4

print(5 + 5)  # sum
print("Hello " + "World!")  # str
print(5 > 4)  # True

# statements (instructions)

my_name = "Andrei"  # присвоение значения

if my_name:  # условная инструкция
    print(my_name)


print(datetime.MAXYEAR)  # использование модуля и его аттрибутов
print(datetime.MINYEAR)


def my_function(a):
    b = datetime.MINYEAR + a
    return b


print(my_function(10))


def sum_nums(a, b):  # create function with two parameters
    sum = a + b     # add variable sum with action
    return sum


print(sum_nums(10, 20))
