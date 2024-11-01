#conditional instructions

# if

# if ... else

# if ... elif

#---

# IF
# check for false values - python\chapter_21_false_values.py
# all other are true values:
# non empty - dict, list, tuple, set, range, str
# non null - int, float, complex
# logical - True


# if Condition:
     # code block
     
my_number = 25

if my_number > 0:
    print(my_number, "is positive number")
    

# example with not

person_info = {
    'age': 20
}

if not person_info.get('name'):
    # action when
    # 1. key 'name' is not present for object 'person'
    # 2. key 'name' is present, but it's value is false
    print("Name is not present")
    
num_one = 10
num_two = 5.3 # not True

if (num_one > 0 and
    num_two > 0 and 
    isinstance(num_one, int) and 
        isinstance(num_two, int)):
    print("both numbers are ints and positive")

#---

# IF ELSE

# if Condition:
    # code block if True
# else:
    # code block if False

my_number = 25

if type(my_number) is int:
    print(my_number, "is integer") # True
else:
    print(my_number, "is not an integer") # False


my_phone = {
    'price': 200
}

if my_phone.get('brand'):
    print("Phone's brand is ", my_phone['brand'])
else:
    print("Pnone's brand not found")
    
# ---

# IF ELIF

# if Condition #1:
    # code block if cond#1 True
# elif Condition #2:
    # code block if
    # cond#1 False and cond#2 True
# else:
    # code block if False
    
my_number = -25

if my_number > 0:
    print(my_number, "is positive number") # if cond#1 true
elif my_number < 0:
    print(my_number, "is negative number") # if xond#1 false, cond#2 true
else:
    print(my_number, "is zero") # if false
    


# ---
# IF in functions

def nums_info(a, b):
    if (type(a) is not int) or (type(b) is not int):
        return "One of the args is not integer"
    
    if a >= b: # execute if cond#1 is False, because of return
        return f"{a} is bigger or equal as {b}"
    
    return f"{a} is less than {b}"

print(nums_info(True, 10))
# One of the args is not integer
print(nums_info(10, 2))
# 10 bigger or equal as 2
print(nums_info(4, 15))
# 4 less than 15


# same function with IF ELIF ELSE
def nums_info(a, b):
    if (type(a) is not int) or (type(b) is not int):
        info = "One of the args is not integer"
    elif a >= b: # execute if cond#1 is False, because of return
        info = f"{a} is bigger or equal as {b}"
    else:
        info = f"{a} is less than {b}"
    return info    

print(nums_info(True, 10))
# One of the args is not integer
print(nums_info(10, 2))
# 10 bigger or equal as 2
print(nums_info(4, 15))
# 4 less than 15    