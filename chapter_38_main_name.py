# __main__ & __name__
# can be used in condition to run only if file is not imported as module
# like if __name__ == "__main__":
       # do some actions

# we have two local py files:
#####
# main.py
# import from other my_fn

# results from module.other.py !!!
# __other__
# False

print("main.py :", __name__)
# __main__
print("main.py :", __name__ = "__main__")
# True

#####
# other.py
def my_fn():
    pass

print("other.py :", __name__)
# __main__
print("other.py :", __name__ == "__main__")
# True