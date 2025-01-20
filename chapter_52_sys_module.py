import sys

print(sys.argv)
# ['c:/Users/Andrei_Panov/Documents/code/python/chapter_52_sys_module.py']

# when run the py file it will wait for 3 args in list (path of the py file and 2 more)
# so correct run would be file.py arg1 arg2
if len(sys.argv) < 3:
    raise IOError("You must provide user and password")
