# Lambda functions

# lambda parametrs: expressions

# no names (anon)

def mult(a, b):
    return a * b

lambda a, b: a* b
# same result using lambda

mult_lambda = lambda a, b: a* b

print(mult(10, 5))
# 50
print(mult_lambda(10, 5))
# 50

# where to use lambda

def greeting(greet):
    return lambda name: f"{greet}, {name}!"

# or using default function
def greeting(greet):
    def info(name):
        return f"{greet}, {name}!"
    return info


morning_greeting = greeting("Good Morning") # goes to greet

print(morning_greeting('Andrey')) # goes to name
# Good Morning, Andrey!
evening_greeting = greeting("Good Evening")

print(evening_greeting('Andrey'))
# Good Evening, Andrey!

