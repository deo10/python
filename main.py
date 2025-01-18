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