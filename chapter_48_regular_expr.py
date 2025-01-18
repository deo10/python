# working with regular expressions in python

import re

my_string = "Let's write RegEx!  Won't that be fun?  I sure think so.  Can you find 4 sentences?  Or perhaps, all 19 words?"

res = re.search(r'RegEx', my_string) # match
print(res)
# <re.Match object; span=(11, 16), match='RegEx'>

res = re.search(r'R...x', my_string) # match
print(res)
# <re.Match object; span=(11, 16), match='RegEx'>

res = re.search(r'R..x', my_string) # no match
print(res)
# None

res = re.search(r'^R*.x', my_string) # match start with R and end with x, any word in between
print(res)
# <re.Match object; span=(0, 16), match="Let's write RegEx">

# print(res.span())
# # (0, 16)
# print(res.start())
# # 0
# print(res.end())
# # 16

# Write a pattern to match sentence
my_pattern = re.compile(r'^L.*\!')
print(my_pattern)
# re.compile('^L.*\!')
print(my_pattern.search(my_string))
# <re.Match object; span=(0, 21), match="Let's write RegEx!"> 
print(my_pattern.match(my_string))
# <re.Match object; span=(0, 21), match="Let's write RegEx!">


# Write a pattern to match sentence endings: sentence_endings
sentence_endings = r"[.?!]"
# Split my_string on sentence endings and print the result
print(re.split(sentence_endings, my_string))
# ["Let's write RegEx", "  Won't that be fun", "  I sure think so", "  Can you find 4 sentences", "  Or perhaps, all 19 words", '']

# Find all capitalized words in my_string and print the result
capitalized_words = r"[A-Z]\w+"
print(re.findall(capitalized_words, my_string))
# ['Let', 'RegEx', 'Won', 'Can', 'Or']

# Split my_string on spaces and print the result
spaces = r"\s+"
print(re.split(spaces, my_string))
# ["Let's", 'write', 'RegEx!', "Won't", 'that', 'be', 'fun?', 'I', 'sure', 'think', 'so.', 'Can', 'you', 'find', '4', 'sentences?', 'Or', 'perhaps,', 'all', '19', 'words?']


# Find all digits in my_string and print the result
digits = r"\d+"
print(re.findall(digits, my_string))
# ['4', '19']

# Write a pattern to match sentence endings: sentence_endings
sentence_endings = r"[.?!]"
# Split my_string on sentence endings and print the result
print(re.split(sentence_endings, my_string))
# ["Let's write RegEx", "  Won't that be fun", "  I sure think so", "  Can you find 4 sentences", "  Or perhaps, all 19 words", '']

# Find all words in my_string and print the result
words = r"\w+"
print(re.findall(words, my_string))
# ["Let's", 'write', 'RegEx', 'Won', 't', 'that', 'be', 'fun', 'I', 'sure']


# Check email address
# \b - word boundary
# [A-Za-z0-9._%+-] - username
# @ - @ symbol
# [A-Za-z0-9.-] - domain name
# \. - dot
# [A-Z|a-z]{2,} - top-level domain
# \b - word boundary
import re

def check_email(email):
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email_check_pattern = re.compile(email_regex)
    validation_result = "valid" if email_check_pattern.fullmatch(email) else "invalid"
    return (email, validation_result)


print(check_email('user@home.com'))
# ('user@home.com', 'valid')
print(check_email('userhome.com'))
# ('userhome.com', 'invalid')
print(check_email('user@homecom'))
# ('userhome.com', 'invalid')

import re

# Check password 8 symbols, required values are uppercase, lowercase, digits, special characters
def check_password(password):
    password_regex = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8}$'
    password_check_pattern = re.compile(password_regex)
    validation_result = "Password is valid" if password_check_pattern.fullmatch(password) else "Password is invalid"
    return (password, validation_result)

# This regular expression pattern ensures:
# - `(?=.*[A-Z])` - at least one uppercase letter
# - `(?=.*[a-z])` - at least one lowercase letter
# - `(?=.*\d)` - at least one digit
# - `(?=.*[@$!%*?&])` - at least one special character from the set `@$!%*?&`
# - `[A-Za-z\d@$!%*?&]{8}` - exactly 8 characters long containing only allowed characters

# Prompt user for password input with length check
while True:
    user_password = input("Enter your password (exactly 8 characters): ")
    if len(user_password) == 8:
        break
    else:
        print("Password must be exactly 8 characters long. Please try again.")


print(check_password(user_password))


# print(check_password('user@hom'))
# # 
# print(check_password('User1hom'))
# # 
# print(check_password('1seR@hom'))
# # 