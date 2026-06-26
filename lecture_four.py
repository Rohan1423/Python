# Dictionary
dict = {
    "name" : "Rohan",
    "age" : 20,
    "topic" : (1,2,3,4),
    "marks" : [85, 90, 78]
}
print(dict)
print(type(dict))
print(dict["name"])

dict["name"] = "Chauhan"
print(dict)
print(type(dict))
print(dict["name"])

null_dict = {}
null_dict["name"] = "rohan"

# Nested Dictionary

nested_dict = {
    "name" : "Rohan",
    "age" : 20,
    "topic" : (1,2,3,4),
    "score" : {
        "maths" : 90,
        "science" : 85
    }
}
print(nested_dict["score"])
print(nested_dict["score"]["maths"])

# Dictionary Methods

student = {
    "name" : "Rohan",
    "subject" : {
        "maths" : 90,
        "science" : 85,
        "chem" : 88
    }
}

print(student.keys())
print(list(student.keys()))
print(len(list(student.keys())))
print(student.values())
print(list(student.items()))
pairs = list(student.items())
print(pairs[0])
print(student["name"])  # Error if key not found code after error will not execute
print(student.get("name")) # No error if key not found will give None

student.update({"city" : "Delhi", "age" : "22", "country" : "India"}) # if key already exists it will update the value else it will add new key value pair
new_Dict = {"country" : "Australia", "state" : "New South Wales"}
student.update(new_Dict)
print(student)

# Set

collection = {1, 2, 2, 2, 4, 5, 6, 7, 8, 9}
print(collection)
print(type(collection))
print(len(collection))

collection1 = {} # this is not a empty set this is a empty dictionary

print(collection1)
print(type(collection1))

collection2 = set() # this is a empty set
collection2.add(1)
collection2.add(2)
collection2.add(3)
collection2.add((4,5,6))
# collection2.add([4,5,6])
print(collection2)
print(type(collection2))

collection2.clear() # removes all elements from the set
print(collection2)

collection2 = {1, 2, 2, 2, 4, 5, 6, 7, 8, 9}

collection2.pop() # removes a random element from the set
collection2.pop() # removes a random element from the set
print(collection2)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = set1.union(set2) # union of two sets
print(set3)

set4 = set1.intersection(set2) # intersection of two sets
print(set4)

# Store following word meaning in a python dictionary :
# table : a piece of furniture with a flat top and one or more legs, used for supporting objects at a convenient height
# chair : a separate seat for one person, typically with a back and four legs

word_meanings = {
    "table": ["a piece of furniture with a flat top and one or more legs","used for supporting objects at a convenient height"],
    "chair": "a separate seat for one person, typically with a back and four legs"
}
print(word_meanings)

# You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all the students.

subjects = {"python", "java", "c++", "html", "css", "javascript", "python", "java", "c++", "html", "css", "javascript"}
print(len(subjects)) # 6 classrooms are needed for all the students