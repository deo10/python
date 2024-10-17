# change merge_lists_to_dict to use keyword args
# add another func invoke with one positional arg and one keyword arg


def merge_lists_to_dict(fruits, qty):
    convert_to_zip = zip(fruits, qty) #union lists
    return dict(convert_to_zip) #convert to dict
    #or return dict(zip(fruits, qty)) - less lines

result_merge_lists_to_dict = merge_lists_to_dict(fruits=['apple', 'banana'], qty=[10, 20])
print(type(result_merge_lists_to_dict))
print(result_merge_lists_to_dict)

one_more = merge_lists_to_dict(['apple', 'banana'], qty=[11, 12]) # works only if the first is position arg
print(type(one_more))
print(one_more)


#task 2
# create fun update_car_info where all keyword args would be union into dict car
# add key (boolean) is_available with value True
# return changed dict
# invoke fun with keyword args brand and price

def update_car_info(**car):
    car['is_available'] = True
    return car

print(update_car_info(brand = 'Honda', price = 1000))