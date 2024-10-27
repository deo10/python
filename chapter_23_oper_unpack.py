# DICT Unpack operator 
# check previous details about * and ** on
# chapter_15_func_args.py

# Adding one DICT to another using unpack operator

button = {
    'width': 200,
    'text': 'Buy'
}

red_button = {
    **button,  # you cannot add var inside Dict without **
    'color': 'red'
}

print(red_button)
# {'width': 200, 'text': 'Buy', 'color': 'red'}

print(button)
# {'width': 200, 'text': 'Buy'}


# Union DICTs using unpack operator

button_info = {
    'text': 'Buy'
}

button_style = {
    'color': 'red',
    'width': 200,
    'height': 300
}

#union
button = {
    **button_info, 
    **button_style
}

# or - same result
button = button_info | button_style

print(button)
# {'text': 'Buy', 'color': 'red', 'width': 200, 'height': 300}




