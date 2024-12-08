# Classes
# examples:
# https://www.w3schools.com/python/python_classes.asp


# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.

# The self parameter is a reference to the current instance of the class,
# and is used to access variables that belong to the class.
# It does not have to be named self, you can call it whatever you like,
# but it has to be the first parameter of any function in the class.


class Car: # description of the class methods are below
    def move(self): # self - is a reference to the current instance of the class
        print("Car is moving")
        
    def stop(self):
        print("Car stopped")

my_car = Car()
print(type(my_car)) # <class '__main__.Car'>
print(isinstance(my_car, Car))  # True

my_car.move() # Car is moving
my_car.stop() # Car stopped

class Person:
  def __init__(mysillyobject, name, age): # Use the words mysillyobject and abc instead of self
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()


# The __init__() Function
# The examples above are classes and objects in their simplest form,
# and are not really useful in real life applications.
# To understand the meaning of classes we have to understand the
# built-in __init__() function.
# All classes have a function called __init__(), which is always executed
# when the class is being initiated.
# Use the __init__() function to assign values to object properties,
# or other operations that are necessary to do when the object is being created.

class Comment:
    def __init__(self, text): # first attribute will be created by python, second is required from user
        self.text = text
        self.votes_qty = 0
        
    def upvote(self):
        self.votes_qty += 1
        
first_comment = Comment("First comment")

print(first_comment.text) # First comment
print(first_comment.votes_qty) # 0
first_comment.upvote()
print(first_comment.votes_qty) # 1

first_comment = Comment("Second comment")
print(first_comment.text) # Second comment
print(first_comment.votes_qty) # 0 !

second_comment = Comment("Second comment")

print(second_comment.text) # Second comment
print(second_comment.votes_qty) # 0 ! each object have their own values

# option with second arg on votes qty

class Comment:
    def __init__(self, text): # first attribute will be created by python, second is required from user
        self.text = text
        self.votes_qty = 0
        
    def upvote(self, qty): # bound method
        self.votes_qty += qty
        
first_comment = Comment("First comment")

print(first_comment.text) # First comment
print(first_comment.votes_qty) # 0
first_comment.upvote(5)
print(first_comment.votes_qty) # 5
first_comment.upvote(15)
print(first_comment.votes_qty) # 20


# Bound Methods
# method is bound if the first param is "self"

print(first_comment.upvote)
# <bound method Comment.upvote of <__main__.Comment object at 0x000001D2971C7C20>>

print(Comment.upvote)
# <function Comment.upvote at 0x000001D2971ED940>

first_comment.upvote()  # invoke for exact the instance

Comment.upvote(first_comment) # invoke method of object from class


# Static Methods

class Comment:
    def __init__(self, text):
        self.text = text
    
    @staticmethod # decarator - method can be invoked on class or method level
    # works without self
    def merge_comments(first, second):
        return f"{first} {second}"

my_comment = Comment("My comment")

n_1 = Comment.merge_comments("Thanks!", "Excellent.")
print(n_1)
# Thanks! Excellent.

n_2 = my_comment.merge_comments("Great", "Ok")
print(n_2)
# Great Ok


# Class Atributes

class Comment:
    total_comments = 0  # class atribute
    
    def __init__(self, text): # first attribute will be created by python, second is required from user
        self.text = text
        self.votes_qty = 0
        Comment.total_comments += 1
        
first_comment = Comment("First comment")

print(Comment.total_comments) # 1

second_comment = Comment("Second comment")

print(Comment.total_comments) # 2