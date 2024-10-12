# create 2 lists

list_1 = ['name1', 'name2', 'name3']
list_2 = [100, 200, 300]

convert_to_zip = zip(list_1, list_2)

convert_to_list = list(convert_to_zip)
print(convert_to_list)
print(convert_to_zip)
# [('name1', 100),('name2', 200),('name3', 300)]
convert_to_dict = dict(convert_to_list)
print(convert_to_dict)
# {'name1': 100, 'name2': 200, 'name3': 300}