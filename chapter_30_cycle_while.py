# Cycle WHILE

# while Condition(if true):
    # block of code that exec on each eteration

i = 10

while i < 50:
    print(i)
    i += 10
# 10
# 20
# 30
# 40

# infinity loop
while True:
    print('infinity loop')

#exit from while via break

while True:
    answer == input("Enter yes or no: ")
    if answer == 'no':
        break
    
# continue
import random

random_num = random.randint(1, 5)
while True:
    num = int(input("Guess the number from 1 to 5: "))
    if num != random_num:
        print("Try again...")
        continue # back to num input
    print("Congrats!", random_num)
    break

#another example
i = 5
while True:
    if i%0o11 == 0: #first comment below
        break
    print(i)
    i += 1

# This line checks if the value of `i` is divisible by `0o11`
# (octal representation of the decimal number `9`).
# The `%` operator is the modulus operator, which returns the remainder of the division.
# If `i` is divisible by `9`, the condition will be `True`.

### Summary of the Loop Execution:
# - The loop starts with `i` initialized to `5`.
# - It checks if `i` is divisible by `9` (since `0o11` in octal is `9` in decimal).
# - If `i` is not divisible by `9`, it prints the value of `i` and increments `i` by `1`.
# - The loop continues until `i` becomes `9`, at which point the condition `i % 0o11 == 0` becomes `True`, and the loop breaks.

### Output:
# The output of the code will be:
# 5
# 6
# 7
# 8