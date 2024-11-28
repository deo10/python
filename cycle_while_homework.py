# create cycle where user need to input 2 numbers (it's str so need to convert to float (better))
# print result of num1:num2
# ask user to continue (yes or no)
# no - exit from cycle
# yes - back to start with 2 nums

while True:
    try:
        num1 = float(input("Enter number 1: "))
        num2 = float(input("Enter number 2: "))
    except ValueError as e:
        print(e)
        print("You must enter numbers!")
        continue
        
    num_result = num1 / num2
    print("Here is the result: ", num_result)
    ask_user = input("Want to continue? Enter yes or no: ")
    if ask_user != 'no':
        continue
    print("Bye Bye")
    break
