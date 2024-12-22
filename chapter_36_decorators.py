# Decorator
# is a special function that takes another function
# to apply add - @name_of_decorator function before the original function
# 


def decorator_function(original_fn): # my_function function as a parametr
    def wrapper_function(*args, **kwargs): #universal params requied as we have it in original function
        # this will be executed before my_function
        print("Executed before function")
        
        # required for wrapper function to invoke original function
        result = original_fn(*args, **kwargs) #universal params requied as we have it in original function
        
        # actions with my_function results
        print("Function result", result)
        
        # this will be executed after my_function
        print("Executed after function")
        
        return result

    return wrapper_function

@decorator_function # pass function below to the decorator function
def my_function(a, b):
     print("This is my function")
     return (a, b)

# Executed before function
# Function result (100, 500)
# Executed after function


# each execution of the my_function will invoke decorator function
# and pass whole my_function, then run wrapper function with params from my_function

result = my_function(100, 500)
print(result)
# (100, 500)




# another example for logging


def log_function_call(fn):
    def wrapper(*args, **kwargs):
        # this will be executed before my_function
        print(f"Executed before {fn.__name__} function", args)
        
        result = fn(*args, **kwargs)
        
        # this will be executed after my_function
        print(f"Executed after {fn.__name__} function", kwargs)
        print(f"Function {fn.__name__} result:", result)
        return result
    
    return wrapper



@log_function_call
def mult(a, b):
    return a * b
    
print(mult(5, 10))
# Executed before mult function (5, 10)
# Executed after mult function {}
# Function mult result: 50

# 50

# another function is called thru the same decorator
@log_function_call
def sum(a, b):
    return a + b
    
print(sum(5, 10))
# Executed before sum function (5, 10)
# Executed after sum function {}
# Function sum result: 15

# 15


### another example of decorator


def validate_args(fn):
    def wrapper(*args, **kwargs):
        for arg in [*args, *kwargs.values()]:  # Unpack args and get values
            if not isinstance(arg, (int, float)):
                print(ValueError(f"Type of {arg} is {type(arg)}", "All args must be int or float"))
                return  # Skip the function execution, allow to continue
        return fn(*args, **kwargs)
    return wrapper

@validate_args
def sum_nums(a, b):
    return a + b

try:
    print(sum_nums(10, 10))
    #20
    print(sum_nums(10.2, 10.4))
    #20.6
    print(sum_nums("bukva", 10.4))
    # ValueError: ("Type of the bukva is <class 'str'>", 'All args must be int or float')

    print(sum_nums(a = 10.4, b =  "bukva")) # works because of line 3 in the code
    # ValueError: ("Type of the bukva is <class 'str'>", 'All args must be int or float')
except ValueError as e:
    print(e)
    
    
    
### one more example of the decorator
    
import random

def is_user_auth():
    return random.choice([True, False]) 


def check_user_auth(fn):
    def wrapper(*args, **kwargs):
        if is_user_auth(): # if True
            print("User is authenticated")
            return fn(*args, **kwargs)
        else: # if False
            raise Exception("ERROR: User is not authenticated")
    
    return wrapper

@check_user_auth
def do_sensetive_job():
    # do some tasks if only user authenticated
    print("Results of the some sensetive tasks")

try:
    do_sensetive_job()
    do_sensetive_job()
    do_sensetive_job()
    do_sensetive_job()
except Exception as e:
    print(e)