#create DICT wiht keys of different types

#convert DICT into JSON

import json

my_dict = {
    "brand": "Nike",
    "price": 2200,
    "available": True
}

my_dict_JSON = json.dumps(my_dict, indent=2)

print(type(my_dict_JSON))
# <class 'str'>
print(my_dict_JSON)
# {
#   "brand": "Nike",
#   "price": 2200,
#   "available": true
# }