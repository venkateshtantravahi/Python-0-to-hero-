"""
It refers to creation of a new class with extracted properties of existing class
new_class refers to child or delivered class
existing_class refers to base or parent class
"""

"""
syntax : 

class BaseClass:
    body of base class
class DeliveredClass(BaseClass):
    body of inherited class
"""

class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter Side "+str(i+1)+ " : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])


class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)

    def findArea(self):
        a,b,c = self.sides
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print("The area of triangle is %0.2f" %area)

t = Triangle()
t.inputSides()
t.dispSides()
t.findArea()   