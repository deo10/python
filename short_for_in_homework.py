#CYCLE short for in Homework

#task #1
# create DICT with values as str
# create new dict based on dict_1 where keys should be in Upper case


dict_1 = {
    'a': 'abc',
    'b': 'def',
    'c': 'ghj'
}

new_dict = {key.upper(): value for key, value in dict_1.items()}
new_dict_1 = {key: value.upper() for key, value in dict_1.items()}
new_dict_2 = {key.upper(): value.upper() for key, value in dict_1.items()}

print(new_dict)
print(new_dict_1)
print(new_dict_2)
#{'A': 'abc', 'B': 'def', 'C': 'ghj'}
#{'a': 'ABC', 'b': 'DEF', 'c': 'GHJ'}
# {'A': 'ABC', 'B': 'DEF', 'C': 'GHJ'}

#task #2
# create LIST with values as str
# create new list based on lsit_1 where keep values if the lenght >3

list_1 = ['abcd', 'ab', 'adcdef']

new_list = [elem for elem in list_1 if len(elem) > 3]

print(new_list)
# ['abcd', 'adcdef']