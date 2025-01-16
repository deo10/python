# working with recursive functions in python

# factorial of a number
def factorial(n):
    if n.type() != int:
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be a positive integer")
    if n == 0:
        return 1 # base case - factorial of 0 is 1
    else:
        return n * factorial(n - 1) # recursive case
    
print(factorial(5)) # 120

