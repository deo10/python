# function default values

def mult_by_factor(value, multiplier=1): # default value multiplier = 1
    return value * multiplier

print(mult_by_factor(10, 2)) #20
print(mult_by_factor(5)) #5

# example #2 default value from function

from datetime import date

def get_weekday():
    return date.today().strftime('%A')

def create_new_post(post, weekday=get_weekday()):
    post_copy = post.copy()
    post_copy['created_on_weekday'] = weekday
    return post_copy

initial_post = {
    'id': 243,
    'author': 'Andrei'
}

post_with_weekday = create_new_post(initial_post)

print(post_with_weekday)
# {'id': 243, 'author': 'Andrei',
# 'created_on_weekday': 'Sunday'}


# options for return date.today().strftime('%A'):
# %Y: Year with century as a decimal number, e.g., "2021".
# %m: Month as a zero-padded decimal number, e.g., "01" for January.
# %d: Day of the month as a zero-padded decimal number, e.g., "01".
# %H: Hour (24-hour clock) as a zero-padded decimal number.
# %M: Minute as a zero-padded decimal number.
# %S: Second as a zero-padded decimal number.