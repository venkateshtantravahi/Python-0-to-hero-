class Person:
    """Class is a mimic of real time object"""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def isEmployee(self):
        return False


# single inheritance
class Employee(Person):
    def __init__(self, name: str, age: int, empid: int, emp_desg: str) -> None:
        self.empid = empid
        self.emp_desg = emp_desg

        # invoke the parent class
        Person.__init__(self, name, age)

    def isEmployee(self):
        return True


class Student(Person):
    def __init__(
        self,
        name: str,
        age: int,
        id: int,
        stream: str,
        grade: str,
        contact: int,
        email: str,
    ) -> None:
        self.id = id
        self.stream = stream
        self.grade = grade
        self.contact = contact
        self.email = email

        Person.__init__(self, name, age)


p1 = Person(name="Guido Van Russom", age=56)
emp = Employee("Guido", 56, 1256, "computer scientist")
std = Student(
    name="Ram",
    age=12,
    id=125,
    stream="CSE",
    grade="A",
    contact=965841383,
    email="ram.t@gmail.com",
)
print(p1.name, p1.age)
print(emp.name, emp.age, emp.empid, emp.emp_desg)
print(std.name, std.age, std.stream, std.contact)
