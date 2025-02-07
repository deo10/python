#CYCLE for in short
# comprehension

# works with list tuple set


# Without list comprehension you will
# have to write a for statement with a conditional test inside:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


# With list comprehension you can do all that with only one line of code:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


# Expression for Element in Subsequence if Condition
[x for x in fruits if "a" in x]

all_nums = [-3, 1, 0, 10, -20, 5]

absolute_nums = []

for num in all_nums:
    absolute_nums.append(abs(num))
    
print(absolute_nums)
# [3, 1, 0, 10, 20, 5]
print(all_nums)
# [-3, 1, 0, 10, -20, 5]

# comprehension option

all_nums = [-3, 1, 0, 10, -20, 5]

absolute_nums = [abs(num) for num in all_nums]
print(absolute_nums)
# [3, 1, 0, 10, 20, 5]


# another example

all_nums = [-3, 1, 0, 10, -20, 5]
positive_nums = []

for num in all_nums:
    if num > 0:
        positive_nums.append(num)
        
print(positive_nums)
#[1, 10, 5]
print(all_nums)
#[-3, 1, 0, 10, -20, 5]

# comprehension option

all_nums = [-3, 1, 0, 10, -20, 5]

positive_nums = [num for num in all_nums if num > 0]

print(positive_nums)
#[1, 10, 5]
print(all_nums)
#[-3, 1, 0, 10, -20, 5]


# another example with SET

my_set = {1, 10, 15}

new_set = set()

for val in my_set:
    new_set.add(val * val)

print(my_set)
# {1, 10, 15}
print(new_set)
# {1, 100, 225}

# comprehension option with SET

my_set = {1, 10, 15}

new_set = {val * val for val in my_set}

print(my_set)
# {1, 10, 15}
print(new_set)
# {1, 100, 225}

# another example with DICT

my_scores = {
    'a': 10,
    'b': 7,
    'c': 14
}

scores = {}

for key, value in my_scores.items():
    scores[key] = value * 10
    
print(scores)
# {'a': 100, 'b': 70, 'c': 140}

# comprehension option with DICT

my_scores = {
    'a': 10,
    'b': 7,
    'c': 14
}

scores = {key: value * 10 for key, value in my_scores.items()}
    
print(scores)
# {'a': 100, 'b': 70, 'c': 140}

# create DICT from LIST using comprehension option

my_scores = [-3, 1, 0, 10, -20, 5]

scores = {k: v for k, v in enumerate(my_scores)}

print(scores)
{0: -3, 1: 1, 2: 0, 3: 10, 4: -20, 5: 5}

# 
for x in [0, 2, 1, 3]:
    for y in [0, 4, 1, 2]:
        print('#')
# for each value in list it will print "#" symbol