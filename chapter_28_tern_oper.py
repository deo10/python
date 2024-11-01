#tern operator
# conditional operator

var = value_1 if condition else value_2

my_num = 21.5

print("is int") if type(my_num) is int else print("is not int")

my_num = 21

if type(my_num) is int:
    print("is int")
else:
    print("is not int")
    
#---
# with function
def img():
    pass

def send_img():
    pass
def process_and_send_img():
    pass


send_img(img) if img.get('is_processed') else process_and_send_img(img)

#---

prod_qty = 10

print("in stock" if prod_qty > 0 else "out of stock")

#---

temp = +24

weather = "hot" if temp > 18 else "cold"

print(weather)

#---
my_img = ('1920', '1080')

print(f"{my_img[0]}x{my_img[1]}") if len(my_img) == 2 else print("incorrect image formatting")

my_img = ('1920', '1080', True)
print(f"{my_img[0]}x{my_img[1]}") if len(my_img) == 2 else print("incorrect image formatting")
# incorrect image formatting

my_img = ('1920', '1080')
info = f"{my_img[0]}x{my_img[1]}" if len(my_img) == 2 else "incorrect image formatting"

print(info)

# rewrite code with if else

def image_resolution(*image_info): #convert args into tupple
    if len(image_info) == 2: # check lenght
        result = print(f"{image_info[0]}x{image_info[1]}")
    else:
        result = print("incorrect image formatting")
    return result   

image_resolution('1920', '1080')
# '1920'x'1080'
image_resolution('1920', '1080', True)
# incorrect image formatting

# check str size

var_string = "incorrect image formatting incorrect image formatting"
print("string is long" if len(var_string) >= 19 else "string is short")