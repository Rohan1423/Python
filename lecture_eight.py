# Class & Object

# creating class
class Student:
    name = "rohan"

# creating object (instance of class)
s1 = Student()
print(s1.name)    

class Car:
    color = "blue"
    brand = "mercedes"

car1 = Car() # constructor function (_init_()) always executed
print(car1.color)
print(car1.brand)    

class Factory:
    name = "PVT"
    def __init__(self):
        print(self)
        print("adding new factory in Database...")

f1 = Factory()

class Studentt:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("adding new student ot database...")

n1 = Studentt("Karan",20)
print(n1.name,n1.marks)
n2 = Studentt("Rohan",30)
print(n2.name,n2.marks)

# default constructor 
def __init__(self):
    print(self)
    print("adding new factory in Database...")

# parameterized constructor
def __init__(self,name,marks):
    self.name = name
    self.marks = marks
