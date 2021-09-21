"""
oops is a special concept that deal with real world entities to solve problems by creating objects 
oops stand for object oriented programming language
everythingwe create here are classes and objects 
objects have two properties namely attributes and behaviour
"""
#creating a parrot class with attributes 
#attributes are two types class and instance attributes 
#instance attributes are defined under speacial method called as __init__()
#every class is like a blue print for objects and objects posses every property of class
class Parrot:

    # class attributes
    species = "bird"

    #instaniate attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #instance methods
    def sing(self, song):
        return "{} sings {}".format(self.name,song)

    def dance(self):
        return "{} is now dancing".format(self.name)

"""
Inheritance is a way of creating a new class for using details of an existing class without modifying it.
The newly formed class is called delivered class or child class
Similarlly, the existing class is called as base or parent class
"""
#parent class
class Bird:

    def __init__(self):
        print("Bird is ready")

    def WhoIsThis(self):
        print("Bird")
    
    def swim(self):
        print("Swim faster")

#child class
class Penguin(Bird):

    def __init__(self):
        #calling super function
        super().__init__()
        print("Penguin is ready")

    def WhoIsThis(self):
        print("Penguin")

    def run(self):
        print("Run Faster")

"""
Encapsulation : using this we can restrict access to methods and variables. This prevents data
from direct modification.
In python we denote private attributes using underscore as prefix i.e '_' or '__'
"""
class computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Sellng Price: {}".format(self.__maxprice))

    def setMaxPrice(self,price):
        self.__maxprice = price

#object for class computer
c = computer()
c.sell()

#change the price
c.__maxprice = 1000
c.sell()

#using setter method
c.setMaxPrice(1000)
c.sell()

"""
Polymorphism is an ability to use a common interface for multiple forms
Suppose, we need to color a shape, there are multiple shapes(rectangle, square, circle). However
we could use the same method to color any shape
"""

class pegion:
    def fly(self):
        print("Pegion can fly.")
    
    def swim(self):
        print("Pegion can't swim")

class seal:
    def fly(self):
        print("Seal can't fly")

    def swim(self):
        print("seal can swim")

#common interface
def flying_test(bird):
    bird.fly()

def swimming_test(bird):
    bird.swim()

#instance objects for birds
peu = pegion()
seel = seal()

#passing the objects
flying_test(peu)
flying_test(seel)
swimming_test(peu)
swimming_test(seel)

#instantiate the Parrot class
blu = Parrot("Blu",19)
woo = Parrot("Woo",15)

# access the class attributes
# to access the class attributes we need a special keyword called as __class__ 
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# acces the instance attributes
#where as instance attribues are accessed by object name.attribute name
print("{} is {} years old.".format(blu.name, blu.age))
print("{} is {} years old.".format(woo.name, woo.age))

#calling our instance methods
print(blu.sing("Happy"))
print(blu.dance())

#creating an object for child class penguin
peggy = Penguin()
peggy.WhoIsThis()
peggy.swim()
peggy.run()