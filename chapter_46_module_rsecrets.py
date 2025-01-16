# working with secrets module in python

import secrets
import string

# randbelow() function - random integer below a given number
print(secrets.randbelow(10))

# randbits() function - random integer with k random bits
print(secrets.randbits(4))

# choice() function - random choice from a list
print(secrets.choice([1, 2, 3, 4, 5]))

# token_bytes() function - random bytes
print(secrets.token_bytes(16))

# token_hex() function - random hex string
print(secrets.token_hex(16))

# token_urlsafe() function - random URL-safe string
print(secrets.token_urlsafe(16))


print(string.ascii_letters)
# ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(string.ascii_digits)
# ascii_digits = '0123456789'
print(string.punctuation)
# punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

all_chars = string.ascii_letters + string.ascii_digits + string.punctuation

# empty string + join() function where we generate random characters from all_chars 16 times
print(''.join(secrets.choice(all_chars) for i in range(16))) # random password
# output: 'Q!@v7#1z^UcF9bN2'

