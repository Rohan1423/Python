# List 

marks = [94.4,"hello",95,66.4]
print(marks)
print(marks[0])
print(len(marks))
marks[1] = "Okay"
print(marks)
print(marks[0])
print(len(marks))

# List Slicing

markss = [87,64,33,95,76]
print(markss[1:4])
print(markss[:4])
print(markss[1:])
print(markss[-3:-1])

# List Methods

list = [2,1,3]
print(list)
list.append(4)
print(list)
list = [2,1,3]
list.sort()
print(list)
list = [2,1,3]
list.sort(reverse=True)
print(list)
list = [2,1,3]
list.reverse()
print(list)
list = [2,1,3]
list.insert(1,5)
print(list)
list = [2,1,3]
list.insert(4,6)
print(list)
list.append(1)
print(list)
list.remove(1)
print(list)
list.pop(2)
print(list)

# Tuples

tup = (1,3,2,4,5)
print(tup[1])

tuple = () # Empty tuple
print(tuple)
print(type(tuple))

tuplee = (1,) # single value tuple
print(tuplee)
print(type(tuplee))

tuplee = (1) # this is wrong declaration for single value tuple as it will read it as integer value 
print(tuplee)
print(type(tuplee))

tuplee = (1.0) # this is wrong declaration for single value tuple as it will read it as float value 
print(tuplee)
print(type(tuplee))

tuplee = ("hello") # this is wrong declaration for single value tuple as it will read it as sting value 
print(tuplee)
print(type(tuplee))

tuplee = (1,2,3,4,5,6) # no need fopr comma in the end when not single value
print(tuplee)
print(type(tuplee))

# Tuple Slicing

print(tuplee[:4])

# Tuple Methods

tupp = (1,2,1,3)

print(tupp.index(1))
print(tupp.count(1))

# WAP to ask user to enter three names of their 3 favorite movies & store them in a list
listOfMovies = []
a = input("Enter the first movie name :") # we can also do like this listOfMovies.append(input("Enter the first movie name :"))
b = input("Enter the second movie name :")
c = input("Enter the third movie name :")
listOfMovies.append(a)
listOfMovies.append(b)
listOfMovies.append(c)
print(listOfMovies)

# WAP to check if a list contains a palindrome of elements
listPalindrome=["m","a","a","m"]

copy_Of_List = listPalindrome.copy()
copy_Of_List.reverse()
if(listPalindrome == copy_Of_List):
    print("Is Palindrome")
else:
    print("Not Palindrome") 