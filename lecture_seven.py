# Read
f = open("demo.txt","r") # If not in same folder then type file's complete path
data = f.read(5) # we can also specify the no. of chars we only want to read
data = f.readline() # reads one line at a time
data = f.readline() # reads one line at a time
print(data)
print(type(data))
f.close() # always close once work is done

# Write

f = open("demo.txt","w")
data = f.write("new data")
f.close() # always close once work is done

# Append

f = open("demo.txt","a")
data = f.write("add in existing")
data = f.write("\nin next line add")
f.close() # always close once work is done

# Whenever we open a file in "w" or "a" mode then if that file does not exists then it will auto create that file
f = open("sample.txt","a") 
data = f.write("add in existing")
data = f.write("\nin next line add")
f.close() # always close once work is 

# with Syntax

with open("sample.txt","r") as f:
    data = f.read()
    print(data)

with open("sample.txt","w") as f:
    f.write("okkkk")    

# Delete a file
import os
os.remove("sample.txt")    

# Practice questions

with open("sample.txt","r") as f:
    data = f.read()
new_data = data.replace("Java","Python") # as data is a string only so we can use string methods
print(new_data)

with open("sample.txt","w") as f:
    f.write(new_data)

def check_word(word):
    with open("sample.txt","r") as f:
        data = f.read()
        if (data.find(word) != -1): # or we can also write it as if(word in data)
            print("Found")
        else:
            print("Not Found")

check_word("300")                          

def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("sample.txt","r") as f:
        while data: # data will become False when there no data in file
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1            

print(check_for_line())

# To print the count of even numbers from a file containing numbers like this 1, 2, 3, 4 ,5
count = 0
with open("sample.txt","r") as f:
    data = f.read()
    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1
print(count)

# without split()
with open("sample.txt","r") as f:
    data = f.read()
    nums = " "
    count = 0
    for i in range(len(data)):
        if (data[i] == ","):
            if(int(nums) % 2 == 0):
                count += 1
            nums = " "
        else:
            nums += data[i]    
print(count)