# конвертация типов

# явная конвертация типов

str
int
float
tuple
list
set

'10' + 5  # error str cannot add int

5 + int('10') # works явная конвертация

# неявная конвертация 

int_num = 5
float_num = 5.5

print(int_num + float_num)  # works 10.5

bool_val = True
int_val = 7

print(bool_val + int_val) # works 8

# summary
# name  | Change | Order | non unique values |
#  
# list  |    +   |   +   |        +          |
#
# dict  |    +   |   X   |        X          |
#
# tuple |    X   |   +   |        +          |
#
# set   |    +   |   X   |        X          |
#
# range |    X   |   +   |        X          |
#
# str   |    X   |   +   |        +          |