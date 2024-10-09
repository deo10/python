# DICT

my_motorbike = {
    'brand': 'Ducati',
    'price': 25000,
    'engive_vol': 1.2
}

# there is no index in dict, no order 

print(my_motorbike['brand'])  #get value
# Ducati

my_motorbike['price'] = 20000  #change value
print(my_motorbike['price'])
# 20000

my_motorbike['new_key'] = True  #add new key and value
print(my_motorbike['new_key'])

del my_motorbike['new_key']  #delete key and value
print(my_motorbike)

# use variables in dict #

var_key_name = 'brand'
my_motorbike[var_key_name] = 'BMW'  #adding variable into dict with new value

print(my_motorbike)
# brand will be changed to "BMW"

brand = 'Honda'
bike_price = 25000
engine_vol = 1.2

my_bike_via_var = {
    'brand': brand,
    'price': bike_price,
    'engine_vol': engine_vol,
}

print(my_bike_via_var)
# dict will take values from variables


# dict levels #

my_motorbike_dict = {
    'brand': 'Ducati',
    'engive_vol': 1.2,
    'price_info': {
        'price': 25000,
        'is_available': True
    }
}

print(my_motorbike_dict['price_info']['price'])
# 25000

print(len(my_motorbike_dict))
# 3

# get values from dict without an error if there is no such key

print(my_motorbike_dict.get('model'))  # there is no such key, but it's fine for python = no error
# None
print(my_motorbike_dict.get('brand'))
# Ducati
print(my_motorbike_dict.get('model', 'New_value_if_there_is_no_such_key'))  #default value if there is no key
# New_value_if_there_is_no_such_key

# method __doc__

my_dic = {}
print(my_dic.__doc__)
# will share how to work dict, like dict()


#practice with dict

my_disk = {}
print(type(my_disk))
print(id(my_disk))

my_disk['Brand'] = 'Samsung'
my_disk['Price'] = 80000

print(len(my_disk))
# 2

#print(my_disk)

print(my_disk.items())
# dict_items([('Brand', 'Samsung'), ('Price', 80000)])

print(my_disk.keys())
# dict_keys(['Brand', 'Price'])

print(my_disk.popitem())
# delete first item in dict

#print(my_disk.__delitem__)
# better to delete items in dict

print(my_disk.get('Type'))  # no error even if there is no such key
print(my_disk.get('Brand'))


# creating new dict by copy
new_disk = my_disk.copy()

new_disk['Type'] = 'External'
new_disk['Port'] = 'USB'
print(new_disk)

# creating from list

new_list = [['a', 0], ['abc', True]]  # will convert to key and value from the list to a dict
my_dict = dict(new_list)
print(my_dict)

