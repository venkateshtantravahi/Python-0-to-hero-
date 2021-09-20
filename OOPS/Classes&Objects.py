"""
class is like a blueprint that we provide to get the final output
whereas object is collections of variables and methods that are
inherited from the class, to act on data to provide some output
"""
#We create a class using 'class' keyword
class myNewClass:
    '''This is a docstring. Created a new class'''
    pass

class Person:
    "This is a person class"
    age = 10

    def greet(self):
        print('Hello')

print(Person.age)
print(Person.greet)
print(Person.__doc__)

harry = Person()
print(harry.greet)
harry.greet() #Person.greet(harry)

"""
methods in classes that starts with __ are having special defn and properties, these are called as constructors 
"""
class ComplexNumbers:
    def __init__(self,r=0,i=0):
        self.real = r
        self.imag = i

    def get_data(self):
        print(f'{self.real}+{self.imag}j')

#Create a new complex number object
num1 = ComplexNumbers(2,3)

#call method get_data num1 instance
num1.get_data()

#creating another object with only one param
num2 = ComplexNumbers(5)

#call the method get_data for num2 instance
num2.get_data()

#deleting parameter imag of object 
#del num1.imag
#num1.get_data()
"""
Traceback (most recent call last):
  File ".\Classes&Objects.py", line 51, in <module>
    num1.get_data()
  File ".\Classes&Objects.py", line 35, in get_data
    print(f'{self.real}+{self.imag}j')
AttributeError: 'ComplexNumbers' object has no attribute 'imag'
"""

#we can delete a entire mathod of class by refering to it
#del ComplexNumbers.get_data
#num1.get_data()
"""
Traceback (most recent call last):
  File ".\Classes&Objects.py", line 63, in <module>
    num1.get_data()
AttributeError: 'ComplexNumbers' object has no attribute 'get_data'
"""
