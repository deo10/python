# Example of generaor in for in cycle
# major key feature of the generator is SIZE

from sys import getsizeof

squares_gen = (num * num for num in range(100000)) # main pointer that it's generator is ()

print(getsizeof(squares_gen))
# 200

print(type(squares_gen))
# <class 'generator'>

for elem in squares_gen:
    print(elem)
    if elem == 100:
        break
# 0
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
# 100


squares_list = [num * num for num in range(100000)]

print(getsizeof(squares_list))
# 800984

print(type(squares_list))
# <class 'list'>