# Function args

def sum_nums(a, b): # a & b are params
    c = a + b
    return (c)

print(sum_nums(2, 5)) # 2 , 5 those args are positional args - order is important 

# another example of positioning args

def get_post_info(name, post_num):
    info = f"{name} napisal {post_num} postov" # create a string with dinamic values
    return info

info = get_post_info('Bogdan', 25)
print(info)
#Bogdan wrote 25 posts

info = get_post_info(100, 'Bad')
print(info)
#100 wrote Bad posts


# union of the args in tuple

def sum_nums_tuple(*args): # this function can take unlim of args
    print(args)
    print(type(args)) # class tuple
    
    print(args[0]) # check first value in tuple
    return sum(args) # using embeded function sum to sum args

print(sum_nums_tuple(2, 4, 6)) 
# 12

# keyword args - order is not important

def get_post_info(name, post_num):
    info = f"{name} napisal {post_num} postov" # create a string with dinamic values
    return info

info = get_post_info(name='Bogdan', post_num=25) # args with keywords, order is not important
print(info)
#Bogdan wrote 25 posts
info = get_post_info(post_num=25, name='Bogdan') # args with keywords, order is not important
print(info)
#Bogdan wrote 25 posts - same result

# union args in dict

def get_pers_info(**person):  # do dict
    print(person)
    # {'name': 'Bogdan', 'posts_qty': 25}
    print(type(person))  #class dict
    info = (
        f"{person['name']} napisal "
        f"{person['posts_qty']} postov"
    ) # it's actually a one string but wrap for style purpose
    return info

info = get_pers_info(name='Bogdan', posts_qty=25) # only keyword args allowed, it can take more args than function params
print(info)
#Bogdan napisal 25 postov

