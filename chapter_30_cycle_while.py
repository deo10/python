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
