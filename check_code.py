users = [
    {
        'user_id': 134,
        'user_name': 'Alice'
    },
    {
        'user_id': 831,
        'user_name': 'Bob'
    },
        {
        'user_id': 531,
        'user_name': 'Crab'
    }
]

# using unpack list into 3 vars

Alice, Bob, Crab = users

print(Alice)
print(Bob)
print(Crab) 

# create function with two args

def fun_two(user_name, user_id):
    return f"User name is {user_name} and ID is {user_id}"
    
#invoke function three times

print(fun_two(**Alice))
print(fun_two(**Bob))
print(fun_two(**Crab))