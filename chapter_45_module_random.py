# working with random module in python

import random

# random() function
print(random.random())

# randint() function - random integer between 1 and 10
print(random.randint(1, 10))

# choice() function - random choice from a list
print(random.choice([1, 2, 3, 4, 5]))

# shuffle() function - shuffle a list
list = [1, 2, 3, 4, 5]
random.shuffle(list)
print(list)

# seed() function - seed the random number generator
random.seed(10)
print(random.random())
print(random.randint(1, 10))

