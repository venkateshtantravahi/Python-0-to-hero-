class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Points:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Points(x,y)

    def __lt__(self, other):
        self_mag = (self.x ** 2) + (self.y ** 2)
        other_mag = (other.x ** 2) + (other.y ** 2)
        return self_mag < other_mag

p1 = Point(2,3)
p2 = Points(4,5)
p3 = Points(5,6)
print(p1)
print(p2)
print(p2+p3)
print(p2<p3)
print(p1+p2)

