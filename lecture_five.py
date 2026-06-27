# while loop 

count = 1
while count <=5:
    print("hello")
    count += 1

    i = 5
    while i >=1 :
        print(i)
        i -= 1
    print ("Loop Ended")

n = int(input("Enter a number: "))
i = 1
while (i<=10):
    print((n*i))
    i += 1

list = [1,4,9,16,25,36,49,64,81,100]
i = 0
while (i<len(list)): # Stopping condition
    print(list[i])
    i +=1     

nums = (1,4,9,16,25,36,49,64,81,100,36)
x = 36
i = 0
while(i<len(nums)):
    if(nums[i] == x):
        print("Found at index: ", i)
    else:
        print("Finding...")
    i += 1

# Break

i = 0
while(i<10):
    if(i == 5):
        break
    print(i)
    i += 1

# Continue

i = 0
while(i<10):
    i += 1
    if(i == 5):
        continue
    print(i)

i = 0
while(i<10):
    if(i == 5):
        i += 1
        continue # skip
    print(i)
    i += 1

i = 1
while(i<10):
    if(i%2 != 0):
        i += 1
        continue # skip
    print(i)
    i += 1

# For loop

veggies = ["potato", "tomato", "onion", "carrot"]
for veggie in veggies:
    print(veggie)

string = "Hello World"
for char in string:
    if(char == 'o'):
        print("Found o")
        break # it will break the loop after first iteration and will not execute the else block
    print(char)    # it will print each character in the string
else:
    print("LOOP ENDED")

x = 36
list = [1,4,9,16,25,36,49,64,81,100,36]
idx = 0
for i in list:
    if(i == x):
        print ("Found at index:",idx)
        break
    else:
        print("Finding...")
    idx += 1    
else:        
    print("Not Found")        

# range () # range(start, stop, step) # start is inclusive and stop is exclusive and both start and step are optional and default value of start is 0 and step is 1

for i in range(5): # stop
    print(i)

for i in range(1, 5):   # start, stop
    print(i)

for i in range(1, 5, 2): # start, stop, step    
    print(i)

# Pass Statement

for i in range(5):
    pass # it will do nothing and will not give any error
print("some work is done")

# wap to find the sum of first n natural numbers using while loop
n = int(input("Enter the value of n:"))
m = n
sum = 0
while(n>=1):
    sum += n
    n -= 1
print("Sum of first", m ,"values is:",sum)

# wap to find the factorial of first n natural numbers using for loop ->(n!)
n = int(input("Enter the value of n:"))
m = n
fact= n
for n in range (n,1,-1):
    fact *= n-1
    n -= 1
print ("Factorial of first", m ,"values is:",fact)    

