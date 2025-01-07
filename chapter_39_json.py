# JSON format
# {
#   "id": 235,
#   "brand": "Nike",
#   "qty": 84,
#   "status": {
#     "isForSale": true
#   }
# }



import json

#put JSON into str
# important to use '' to pass the JSON format
json_str = '{"id":235, "brand": "Nike", "qty":84, "status": {"isForSale":true}}'
json_array = '[1, 2, 3]'

#load str in Python DICT
sneakers = json.loads(json_str)

# load array in PYTHON LIST
my_list_from_JSON = json.loads(json_array)

print(type(sneakers))
#<class 'dict'>

print(type(my_list_from_JSON))
#<class 'list'>

print(my_list_from_JSON)
# [1, 2, 3]


print(sneakers['brand'])
# Nike

print(sneakers['qty'])
# 84

print(sneakers['status']['isForSale'])
# True

back_json = json.dumps(sneakers, indent=2)

print(back_json)
# {
#   "id": 235,
#   "brand": "Nike",
#   "qty": 84,
#   "status": {
#     "isForSale": true
#   }
# }