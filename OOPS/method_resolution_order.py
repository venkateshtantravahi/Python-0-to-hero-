"""
MRO --> Method Resolution Order
It defines the order in which th base classes are searched when executing a method.
"""
class A:
    def rk(self):
        print("In class A")
class B(A):
    def rk(self):
        print("In class B")
class C(A):
    def rk(self):
        print("In class C")
#Multiple Inheritance
class D(B,C):
    pass
class E(B,C):
    def __init__(self):
        print("Constructor C")
    
#MRO working for single inheritance        
r = B()
r.rk()

#MRO working for multiple inheritance [D,B,C]
t = D()
t.rk()

#MRO working
f = E()
print(E.__mro__)
print(E.mro())

#checking object class
print(issubclass(list,object))
print(isinstance("Python",object))