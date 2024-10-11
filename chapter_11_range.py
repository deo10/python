# RANGE

# unique index and cannot be changed

my_range = range(7)

print(type(my_range))
# class range

print(my_range)
# range(0, 7)

print(list(my_range))
# [0, 1, .... 6]

my_range = range(10, 20, 3) # 10 start, 20 end, 3 step

print(my_range.start) # 10
print(my_range.stop)  # 20
print(my_range.step)  # 3


print(my_range)
# range(10, 20, 3)
print(list(my_range))
# [10, 13, 16, 19]
print(my_range.index(13))
# 1
print(my_range.index(16))
# 2

print(my_range[0]) # 10
print(my_range[1]) # 13
print(my_range[2]) # 16
print(my_range[3]) # 19
print(my_range[4]) # out of range

for n in my_range:
    print(n)
    # 10
    # 13
    # 16
    # 19
    
print(my_range.count(10))
# 1 - 1 time present on range
print(my_range.count(11))
# 0 - 0 time present on range
