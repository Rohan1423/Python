# # Class & Object

# # creating class
# class Student:
#     name = "rohan"

# # creating object (instance of class)
# s1 = Student()
# print(s1.name)    

# class Car:
#     color = "blue"
#     brand = "mercedes"

# car1 = Car() # constructor function (_init_()) always executed
# print(car1.color)
# print(car1.brand)    

# class Factory:
#     name = "PVT"
#     def __init__(self):
#         print(self)
#         print("adding new factory in Database...")

# f1 = Factory()

# class Studentt:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student ot database...")

# n1 = Studentt("Karan",20)
# print(n1.name,n1.marks)
# n2 = Studentt("Rohan",30)
# print(n2.name,n2.marks)

# # default constructor 
# def __init__(self):
#     print(self)
#     print("adding new factory in Database...")

# # parameterized constructor
# def __init__(self,name,marks):
#     self.name = name
#     self.marks = marks

# # Methods (User defined functions in class)
# class Studenttt:
#     college_name = "ABC College" # class attribute
#     def __init__(self,name,marks):
#         self.name = name # object attribute
#         self.marks = marks # object attribute

#     def Hello(self): # Hello Method
#         print("welcome",self.name)    

#     def get_marks(self): # get_marks Method
#         return self.marks 

# m1 = Studenttt("Nikhil",70)
# print(m1.get_marks())
# m1.Hello()       

# # Practice Question
# # Create student calss that takes name & marks of 3 subjects as arguments in constructor.Then create a method to print the average.

# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

#     def average_score(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("HI ",self.name," YOUR AVERAGE SCORE IS ",sum/3)

# s1 = Student("Rohan",[99,98,70])
# s1.average_score()

# s1.name = "NIKHIL" # also we can directly change our attributes values
# s1.average_score()

# # Static Method

# class Student:
        
#     @staticmethod    # without this it will give error as no self param in Hello Method
#     def Hello():
#         print("Hello")

# s1 = Student()
# s1.Hello()        

# # Abstarction 
# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("CAR STARTED...")
        
# car1 = Car()
# car1.start()    

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
