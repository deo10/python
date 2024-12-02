import random
random.seed(12)
print(random.random())
#0.4745706786885481

random.seed(12)
print(random.random())
#0.4745706786885481


from random import randint
print(str(randint(0, 1)) + str(randint(0, 1)), end='')
#10 - 100

from random import randrange
print("randrange#1: ",randrange(0, 1))
#0

print("randrange#2: ", randrange(0, 20, 5))
#0


from random import choice
name = 'Yoon'
print("Name is: ", choice(name))
# o

# from random import sample
# teachers = ('Pak', 'Kim', 'Yoon')
# print("sample is: ", sample(teachers))
# Error!

###
# Add necessary imports here
from random import seed, random

# Write the function random_seed

def random_seed(s):
    seed(s)
    return random()


s = float(input("Enter a value: "))
print(random_seed(s))
# 0.5714025946899135

###
# Open the file cards.py, and write a function
# that takes as arguments a list of suits and a list of ranks.
# Inside the function create the list of the deck and return a random group of 4 cards.
# The output should be in the format of <rank>-<suit>, e.g Jack-Hearts

from random import sample

def cards_sample(suits, ranks):
    deck = [str(x)+'-'+y for x in ranks for y in suits] # create format str(RANK)+'-'+SUIT
    return sample(deck, 4) #get 4 cards from deck


suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
ranks = [i for i in range(1, 11)] + ['Jack', 'Queen', 'King'] #create range 1-11 cards in deck + roles

print(cards_sample(suits, ranks))
# ['4-Diamonds', '8-Hearts', '3-Hearts', '10-Clubs']