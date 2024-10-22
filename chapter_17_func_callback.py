# Callback function

def other_fn():
    # some actions
    pass

def fn_with_callback(callback_fn): # func as param - looking that will be invoke with func as arg
    callback_fn() #invoke callback_fn
    
fn_with_callback(other_fn) # not invoke other_fn but pass it as arg to func with callback

#example #2

# func 2
def print_number_info(num):
    if (num % 2) == 0:
        print("Entered number is even")
    else:
        print("Entered number is odd")

# func #2        
def print_square_num(num):
    print("Square of the num is ", num * num)

# callback function - invoke function        
def process_num(num, callback_fn1):
    callback_fn1(num)
    
entered_num = int(input('Enter any number: '))

process_num(num = entered_num, callback_fn1 = print_number_info)

process_num(num = entered_num, callback_fn1 = print_square_num) # invoke with another func

# example #3

def send_data(data):
    # sending data
    pass
def process_data(input_data, send_data_fn):
    updated_data = input_data.copy()
    # actions
    send_data_fn(updated_data)
    
process_data({'name': 'Andrei'}, send_data)