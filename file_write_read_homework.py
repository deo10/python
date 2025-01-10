# create folder files in the current directory

from pathlib import Path

my_dir = Path('/Users/Andrei_Panov/Documents/code/python/files')


# add two files to the folder first.txt and second.txt and write 3 lines to each file

if not my_dir.exists():
    my_dir.mkdir()
    
with open(my_dir / 'first.txt', 'w') as test_file:
    test_file.write('str1\n') # write to file
    test_file.write('str2\n') # write to file
    test_file.write('str3\n') # write to file
    
with open(my_dir / 'second.txt', 'w') as test_file:
    test_file.write('str1\n') # write to file
    test_file.write('str2\n') # write to file
    test_file.write('str3\n') # write to file
    
# read all the lines of the first file and print it

with open(my_dir / 'first.txt', 'r') as test_file:
    print(test_file.read()) # read from file
    
# read line by line the second file and print it

with open(my_dir / 'second.txt', 'r') as test_file:
    while True:
        line = test_file.readline() # read from file line by line
        print(line)
        if not line:
            break

# change lines in the first file to uppercase and write them back to the file

with open(my_dir / 'first.txt', 'r') as test_file:
    lines = test_file.readlines() # read from file as list of lines [line1, line2, ...]
    for line in lines:
        print(line.upper())
        
with open(my_dir / 'first.txt', 'w') as test_file:
    for line in lines:
        test_file.write(line.upper())
        
# delete files

(my_dir / 'first.txt').unlink()
(my_dir / 'second.txt').unlink()

# delete folder
if my_dir.exists():
  my_dir.rmdir()