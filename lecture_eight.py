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

# Methods (User defined functions in class)
class Studenttt:
    college_name = "ABC College" # class attribute
    def __init__(self,name,marks):
        self.name = name # object attribute
        self.marks = marks # object attribute

    def Hello(self): # Hello Method
        print("welcome",self.name)    

    def get_marks(self): # get_marks Method
        return self.marks 

m1 = Studenttt("Nikhil",70)
print(m1.get_marks())
m1.Hello()       

# Practice Question
# Create student calss that takes name & marks of 3 subjects as arguments in constructor.Then create a method to print the average.

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def average_score(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("HI ",self.name," YOUR AVERAGE SCORE IS ",sum/3)

s1 = Student("Rohan",[99,98,70])
s1.average_score()

s1.name = "NIKHIL" # also we can directly change our attributes values
s1.average_score()

# Static Method

class Student:
        
    @staticmethod    # without this it will give error as no self param in Hello Method
    def Hello():
        print("Hello")

s1 = Student()
s1.Hello()        

# Abstarction 
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("CAR STARTED...")
        
car1 = Car()
car1.start()    

# Practice Question
# Create Account class with 2 Attributes - balance & account no.
# Create methods for debit, credit & printing the balance.

class Account:
    def __init__(self,balance,account_no):
        self.balance = balance
        self.account_no = account_no
    def debit(self,deduct):
        self.balance -= deduct
        print("Current Balance is ",self.current_balance())

    def credit(self,added):
        self.balance += added
        print("Current Balance is ",self.current_balance())    

    def current_balance(self):
        return self.balance   

acc1 = Account(10000,12345)
acc1.debit(400)
acc1.credit(1000)
print(acc1.current_balance())

# Private(like) attributes & Methods

class Person:
    __name = "anonymous"

    def __hello(self):
        print("HELLO")

    def welcome(self):
        self.__hello()

p1 = Person()        
print(p1.__name)
p1.__hello()
p1.welcome()

# Inheritance
# Single Inheritance

class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped.")    

class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name

car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Prius")
car1.start()
car1.stop()
print(car1.color)

# Multi-level Inheritance

class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped.")    

class ToyotaCar(Car):
        brand = "Toyota"

class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type = type

car1 = Fortuner("Petrol")
car2 = Fortuner("Electric")
car1.start()
car1.stop()
print(car1.color)
print(car1.brand)

# Multiple Inheritance

class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A,B):
    varC = "welcome to class C"

c1 = C()
print(c1.varA)
print(c1.varB)  
print(c1.varC)

# Property

class Student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"   

stu1 = Student(98,97,99)
print(stu1.percentage)
stu1.phy = 86
print(stu1.percentage)

# Polymorphism : Operator Overloading

class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i + ",self.img,"j")

    def __add__(self,num2): # dunder function
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)

num1 = Complex(1,3)
num1.showNumber()

num2 = Complex(4,8)
num2.showNumber()

num3 = num1 + num2 # operator overloading (polymorphism)-> here we changed the meaning of + operator using dunder function
num3.showNumber()