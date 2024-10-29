# DICT Unpack operator 
# check previous details about * and ** on
# chapter_15_func_args.py

# Adding one DICT to another using unpack operator

button = {
    'width': 200,
    'text': 'Buy'
}

red_button = {
    **button,  # you cannot add var inside Dict without **
    'color': 'red'
}

print(red_button)
# {'width': 200, 'text': 'Buy', 'color': 'red'}

print(button)
# {'width': 200, 'text': 'Buy'}


# Union DICTs using unpack operator

button_info = {
    'text': 'Buy'
}

button_style = {
    'color': 'red',
    'width': 200,
    'height': 300
}

#union
button = {
    **button_info, 
    **button_style
}

# or - same result
button = button_info | button_style

print(button)
# {'text': 'Buy', 'color': 'red', 'width': 200, 'height': 300}


# map values from list to vars using unpacking
# list antuple are ordered list of values - index important

my_fruits = ['apple', 'banana', 'lime']

# bad option
# my_apple = my_fruits[0]
# my_banana = my_fruits[1]
# my_lime = my_fruits[2]
# thru unpacking
my_apple, my_banana, my_lime = my_fruits # order is important

print(my_apple)
print(my_banana)
print(my_lime)
#apple
#banana
#lime

# map values from TUPLE to vars using unpacking
# list antuple are ordered list of values - index important

my_fruits = ('apple', 'banana', 'lime') # TUPLE - NO new elements can be added
# thru unpacking
my_apple, my_banana, my_lime = my_fruits # order is important

print(my_apple)
print(my_banana)
print(my_lime)
#apple
#banana
#lime

# unpacking with * - moves all under one var as new list

my_fruits = ['apple', 'banana', 'lime']

# thru unpacking
my_apple, *remaining_fruits = my_fruits # order is important

print(my_apple) # apple
print(remaining_fruits) # ['banana', 'lime'] - new list created


# unpacking DICT into args with key words

user_profile = {
    'name': ' Andrey',
    'comments_qty': 10,
}

def user_info(name, comments_qty=0): # two params and 2nd has 0 as default value
    if not comments_qty:
        return f"{name} has no comments"
    
    return f"{name} has {comments_qty} comments"

print(user_info(**user_profile)) # using ** to unpack key and value into function
# Andrey has 10 comments

# unpacking LIST into positional ARGS

user_data = ['Andrey', 0] # List, only two args or it would be error

def user_info(name, comments_qty): # two params and 2nd has 0 as default value
    if not comments_qty:
        return f"{name} has no comments"
        # Andrey has no comments
    return f"{name} has {comments_qty} comments"

print(user_info(*user_data)) # unpack for LIST
# Andrey has 10 comments


#task - create list with 3 dicts
users = [
    {
        'user_id': 134,
        'user_name': 'Alice'
    },
    {
        'user_id': 831,
        'user_name': 'Bob'
    },
        {
        'user_id': 531,
        'user_name': 'Crab'
    }
]

# unpack list into 3 vars

Alice, Bob, Crab = users

print(Alice)
print(Bob)
print(Crab) 

# create function with two args

def fun_two(user_name, user_id):
    return f"User name is {user_name} and ID is {user_id}"
    
#invoke function three times

print(fun_two(**Alice))
print(fun_two(**Bob))
print(fun_two(**Crab))