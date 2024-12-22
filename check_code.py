import random

def is_user_auth():
    return random.choice([True, False]) 


def check_user_auth(fn):
    def wrapper(*args, **kwargs):
        if is_user_auth(): # if True
            print("User is authenticated")
            return fn(*args, **kwargs)
        else: # if False
            raise Exception("ERROR: User is not authenticated")
    
    return wrapper

@check_user_auth
def do_sensetive_job():
    # do some tasks if only user authenticated
    print("Results of the some sensetive tasks")

try:
    do_sensetive_job()
    do_sensetive_job()
    do_sensetive_job()
    do_sensetive_job()
except Exception as e:
    print(e)