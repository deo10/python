# отступы в python
# 1отступ = 4 пробела (не использовать ТАБ)

def my_name(name):
    print(name)


my_name('Andrey')

# ---
# style guide PEP 8
# https://peps.python.org/pep-0008/

my_list = [1, 2, 3]

print(my_list)

# cmd(ctrl) + shift + P - format document with (Python) -> auto format with pep8

# комментарий cmd + / or cnt + / (win)


# functions обзор #

def function_name(block_of_parameters):
    # function_block_of_code
    print("hello there")


function_name()  # execute function


def name(name_var):  # name_var is a variable inside function (parameter)
    # function_block_of_code
    print("hello there", name_var)


name("Andrei")  # execute function, required to put something as argument

# return #

def sum_nums(a, b):  # create function with two parameters
    sum = a + b     # add variable sum with action
    print(sum)


sum_nums(10, 10)    # execute function with two args


def sum_nums(a, b):  # create function with two parameters
    sum = a + b     # add variable sum with action
    return sum      # statement (stop for a function)


external_var = sum_nums(10, 10)  # ext_var got value from return
print(external_var)

print(sum_nums(5, 10))  # show value of function exec with result from return

# run 1st with 5 & 10, then use result as "a" + 30, and finnaly print
print(sum_nums(sum_nums(5, 10), 30))
