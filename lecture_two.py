# String
str1 = "hello"
str2 = 'hi'
str3 = """okay"""

# "this is rohan's mac"
# 'this is rohan"s mac'

str4 = "this is a string.we are creating it in python"
print(str4)

str5 = "okayyy"
print(str4 + " " + str5)
print(len(str4))

# Indexing
string = "APNA COLLEGE"
ch = string[4]
print(ch)

# Slicing
strr = "rohan chauhan"
print(strr[1:4])
print(strr[:5]) #[0:5]
print(strr[6:]) #[6:len(strr)]

# Negative Indexing
print(strr[-5:-1]) #ending_idx not included

print(strr.endswith("a"))
print(strr.capitalize())
print(strr.replace("ro","ni"))
print(strr.find("rohan"))
print(strr.count("han"))

# Conditional Statements
light = "green"
if(light=="red"):
    print("cross...")
# elif(light=="green"):
#     print("stopp!")
else:
    print("waitt!")

marks = int(input("Enter Marks : "))
if(marks>=90):
    grade = "A"
elif(marks>=80 and marks <90):
    grade = "B"
else:
    grade = "C"
print(grade)

# Nesting
if(marks>=90):
    grade = "A"
    if(marks<90):
        print("If Nested")
    else:
        print("Else Nested")    
elif(marks>=80 and marks <90):
    grade = "B"
else:
    grade = "C"