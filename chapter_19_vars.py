# Variable area of visibility
# defines border of variable availability

# global variables vs local variables

a = 10 # global var availability area

def sum_nums():
    a = 20  # var availability area is func area - local variable
    b = 30
    sum = a + b
    return sum  

# if the var is not found on any local level, python will try to find it on higher level, till global


a = 10 # global var

def my_fn():
    a = True # local (fn) var
    b = 30
    print(a) # True
    print(b)
    
my_fn() # all vars in fn would be deleted

print(a) # 10
# print(b) # Error - var not defined



# creating global var in function

def my_fn():
    global a # creating global var inside fn
    a = 10
    
my_fn()

print(a) #10


