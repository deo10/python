# error handling

try:
    # executing code block
    pass
except [ErrorType]:
    # this block run if there is an error in try block
    pass

# code example
try:
    # executing code block
    print(10 / 0)
except ZeroDivisionError:
    # this block run if there is an error in try block
    print("error - division by zero!")

print("Code continue to work")


# enhance
try:
    # executing code block
    print(10 / 0)
except ZeroDivisionError as e:
    # this block run if there is an error in try block
    print(type(e))
    # <class 'ZeroDivisionError'>
    print(e)
    # division by zero

print("Code continue to work")



#other error handling
try:
    # executing code block
    print('10' / 0)
except ZeroDivisionError as e:
    print(e)
    # division by zero
except TypeError as e:
    print(type(e))
    # <class 'TypeError'>

print("Code continue to work")



# Else in error handling
try:
    # executing code block
    print(10 / 2)
except ZeroDivisionError as e:
    print(e)
    # division by zero
except TypeError as e:
    print(type(e))
    # <class 'TypeError'>
else:
    print("There is no error")
finally: # run everytime
    print("Code continue to work")



# any errors handling
try:
    # executing code block
    print(10 / 0)
except Exception as e:
    print(e)
    #division by zero

# or
try:
    # executing code block
    print(10 / 0)
except:
    print("Some error occurred..")
    # Some error occurred..
    
# Error creation

def devide_nums(a, b):
    if b == 0:
        raise TypeError("Second argument can't be 0")
    return a / b

try:
    # executing code block
    devide_nums(10, 0)
except ZeroDivisionError as e:
    print(e)
    # division by zero
except TypeError as e:
    print(e)
    # CUSTOM ERROR - Second argument can't be 0

print("Code continue to work")