# Functions

## best practices ##
# name based on purpose
# name should have a verb like convert_data
# one function should do one task
# it's not recommended to change external variables (use copy)


# define function sum
def sum(a, b):
    c = a + b
    print(c)

# add values for variables    
a = 5
b = 4


# invoke function sum
sum(a, b)
# 9 - will be printed as a result of the function

# function is an object
print(type(sum))
# <class 'function'>

# define function with 2 params, add some action in function body,
# return c - to get result (else will return None)
def my_fn(a, b):
    a = a + 1
    c = a + b
    return c

#invoke function and provide values for arguments
res = my_fn(10, 12)
print(res)
# 23

# example of function with changeable object
# in this case both var and function result would be the same, so we changed var value

def increase_person_age(person):
    person['age'] +=1
    return person

person_one = {
    'name': 'Bob',
    'age': 21
}

increase_person_age(person_one)
print(person_one['age'])  #22

# to prevent changing var we can use copy

def increase_person_age(person):
    person_copy = person.copy() # copy the dict (we can use deepcopy for multi stage)
    person_copy['age'] +=1
    return person_copy

person_one = {
    'name': 'Bob',
    'age': 21
}

new_person = increase_person_age(person_one)
print(new_person['age']) #22
print(person_one['age']) #21 did not changed

