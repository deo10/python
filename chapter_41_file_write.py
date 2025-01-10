# read and write files in python

    
with open('chapter_41_file_write.txt', 'r') as test_file:
    print(test_file.read()) # read from file

with open('chapter_41_file_write.txt', 'r') as test_file:
    print(test_file.readlines()) # read from file as list of lines

with open('chapter_41_file_write.txt', 'w') as test_file:
    test_file.write('Hello, World!') # write to file
    
with open('chapter_41_file_write.txt', 'a') as test_file:
    test_file.write('Hello, World!') # append to file



# another example
test_file = open('test.txt', 'w') # open the file in write mode

print(test_file)
# <_io.TextIOWrapper name='test.txt' mode='w' encoding='cp1252'>

print(type(test_file))
# <class '_io.TextIOWrapper'>

test_file.write('Hello, World!\n') # write to file
test_file.write('abracadabra') # write to file

test_file.close() # close the file

test_file = open('test.txt', 'r') # open the file in read mode

print(test_file.read()) # read from file

test_file.close() # close the file


# option with, close is not required

with open('test.txt', 'w') as test_file:
    test_file.write('str1\n') # write to file
    test_file.write('str2\n') # write to file
    test_file.write('str3\n') # write to file
    
with open('test.txt', 'r') as test_file:
    print(test_file.read()) # read from file
    
with open('test.txt', 'r') as test_file:
    lines = test_file.readlines() # read from file as list of lines [line1, line2, ...]
    for line in lines:
        print(line)
# Hello, World!
# abracadabra
# focus

with open('test.txt', 'r') as test_file:
    while True:
        line = test_file.readline() # read from file line by line
        print(line)
        if not line:
            break
