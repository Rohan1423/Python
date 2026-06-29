# Function 
def calculate_sum():
    n = int(input("Enter the no. of elements:"))
    sum = 0
    for i in range(n):
        c = int(input("Enter the element value:"))
        sum += c
    return sum
print(calculate_sum())

def sum(a,b):
    sum = a + b
    print(sum)
    return sum

sum(2,3)

def sum1(a,b): # parameters
    return a + b

sum1 = sum1(20,3) # function call; arguments
print(sum1)

def print_hello():
    print("hello")
output = print_hello() 
print(output) # None

def calculate_average():
    average = 1
    sum = 0
    for i in range(3):
        c = int(input("Enter the element value:"))
        sum += c
        average = sum / 3

    return average
print(int(calculate_average()))

# Default Argument Function

def default(a, b=2):
    prod  = a * b
    print(prod)
    return prod
default(2)

# Recursion

def recursion(n):
    if(n == 0):
        return
    print(n)
    recursion(n-1) # or n -= 1 then recursion(n)
    print("END")
recursion(8)

def fact(n):
    if(n == 1 or n == 0):
        return 1
    else:
        return n * fact(n-1) # recursive relationship (recurrence relation)
print(fact(5))    