# How to work with files in Python

# modules
# OS
# pathlib


# example with os (functional programming)

from os import path # import the path function from the os module

# Print the absolute path of the current directory
print(path.abspath('.'))
# C:\Users\Andrei_Panov\Documents\code\python

print(type(path))
# <class 'module'>

# example with pathlib (object-oriented programming)

from pathlib import Path # import the Path class from the pathlib module

# Print the absolute path of the current directory
print(Path('.').absolute())
# C:\Users\Andrei_Panov\Documents\code\python

print(type(Path))
# <class 'type'>


# methods of the class Path

# Path.cwd() - returns the current working directory
# Path.home() - returns the home directory of the user
# Path.exists() - returns True if the path exists
# Path.is_dir() - returns True if the path is a directory
# Path.is_file() - returns True if the path is a file
# Path.mkdir() - creates a directory
# Path.rmdir() - removes a directory
# Path.unlink() - removes a file
# Path.rename() - renames a file or directory
# Path.glob() - returns an iterator over all files in a directory
# Path.open() - opens a file
# Path.read_text() - reads the content of a file
# Path.write_text() - writes content to a file
# Path.read_bytes() - reads the content of a file as bytes


from pathlib import Path

file_path = Path('example.txt')

# shows all methods of the class Path and not magic methods
print([m for m in dir(file_path) if not m.startswith('_')])
# ['absolute', 'anchor', 'as_posix', 'as_uri', 'chmod', 'cwd', 'drive', 'exists', 'expanduser', ...]


# print the current working directory
print(Path.cwd())
# C:\Users\Andrei_Panov\Documents\code\python

# creating new path using joinpath method mac and linux
print(Path('usr').joinpath('local').joinpath('bin'))
# usr\local\bin

print(Path('usr') / 'local' / 'bin')
# usr\local\bin

# creating new path using joinpath method windows
print(Path('C:/').joinpath('Program Files').joinpath('Python'))
# C:\Program Files\Python

print(Path('C:/') / 'Program Files' / 'Python')
# C:\Program Files\Python


# check if the file exists and if it's a file or a directory
print("path exists?", Path('main.py').exists())
print("is a file?", Path('main.py').is_file())
print("is a dir?", Path('main.py').is_dir())
# path exists? True
# is a file? True
# is a dir? False

print(Path('/Users/Andrei_Panov/Documents/code/python/main.py').exists())
# True
print(Path('other.py').exists())
# False


# get list of files and directories in the current directory, first 10
print(list(Path('.').iterdir())[:10])

# all files and directories in the current directory
for f in Path('.').iterdir():
    print(f)

# [WindowsPath('chapter_40_work_with_files.py'), WindowsPath('example.txt')]

# another example
# create variable for folder path
my_dir = Path('/Users/Andrei_Panov/Documents/code/python/temp')

# check if the directory exists if not create it
if not my_dir.exists():
    my_dir.mkdir()

# check if the directory exists if yes remove it    
if my_dir.exists():
    my_dir.rmdir()



# example of file deletion

# check if the file exists
print(Path('example.txt').exists())
# True

# delete the file
Path('example.txt').unlink()

# check if the file exists
print(Path('example.txt').exists())
# False
