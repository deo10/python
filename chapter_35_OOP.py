# Encapsulation
# attributes and methods are enclapsulated in class

class Email:
    def __init__(self, sender, recipient, subject, body): # attributes
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body
        
    def send_email(self): # methods
        # logic to send email
        pass
    
    def read_email(self): # methods
        # logic to read email
        pass
    
# Inheritance
# https://www.w3schools.com/python/python_inheritance.asp


class Vehicle: # parent class
    def __init__(self, make, model): # attributes
        self.make = make
        self.model = model
        
    def start(self): # methods
        # logic to start the vehicle
        pass
    
    def stop(self): # methods
        # logic to stop the vehicle
        pass
    
class Car(Vehicle): #child class with additions to Vehicle class
    def __init__(self, make, model, doors_qty):
        super().__init__(make, model) # init for parent class
        self.doors_qty = doors_qty
    
    def lock_doors(self): # methods
        # logic to lock the door
        pass
    
    def open_doors(self): # methods
        # logic to open the door
        pass
    

# Polymorphism
# common part is calc_area, but shapes are different with their own method to get it
# so child classed having same method calc_area but with own formula
# https://www.w3schools.com/python/python_polymorphism.asp

import math

class Shape: 
    def calc_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def calc_area(self):
        return math.pi * self.radius * self.radius # math.pi * pow(self.radius, 2) another option
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def calc_area(self):
        return self.width * self.height
    
# creating instances of each class with params
shapes = [Circle(5), Rectangle(10, 2), Circle(7), Rectangle(12, 4)]

# creating cycle for to calc shape area, where we use parent class - Shape
for shape in shapes:
    print(shape.calc_area())   
# 78.53981633974483
# 20
# 153.93804002589985
# 48


# Abstraction
from abc import ABC, abstractmethod


class Payment(ABC): # Helper class that provides a standard way to create an ABC using inheritance.
    @abstractmethod #mandatory to have method process_payment in all child classes
    def process_payment(self):
        pass

class CreditCardPayment(Payment):
    def process_payment(self):
        pass
    
class StripePayment(Payment):
    def process_payment(self):
        pass
    
class PayPalPayment(Payment):
    def process_payment(self):
        pass