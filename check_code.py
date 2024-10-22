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