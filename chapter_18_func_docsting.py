# Docstring

# use to document your function, class or module

def mult_by_factor(value, mult=1):
    """Multiplies number by multiplicator"""  # adding descroption for function
    return value * mult

mult_by_factor(5)


def print_number_info(num):
    """
    Prints whether number is even or odd
    
    Args:
        num (int): Number to be evaluated
    """ # adding description for args
    if (num % 2) == 0:
        print("Entered number is even")
    else:
        print("Entered number is odd")

print_number_info(20)

