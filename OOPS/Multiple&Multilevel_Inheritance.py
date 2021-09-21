"""
Multiple Inheritance, the feature of all base classes are inherited into a delivered class
"""
class base1:
    pass
class base2:
    pass
class MultiDelivered(base1,base2):
    pass
"""
Multi-level Inheritance, features of the base class and the derived class are inherited into the 
newly delivered class
"""
class Base:
    pass
class deliveredClass(Base):
    pass
class deliveredClass1(deliveredClass):
    pass

