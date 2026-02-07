"""
Student enrolments 
given a list of tuples(name,subjects)
# 1. list all unique course 
# 2. list students enrolled in a English
# 3. create dictionary (student,set of courses)
"""

info = [
    ("Alice","Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie","English"),
]

# 1
courses_set = set() # to store unique courses
for tup in info:
    courses_set.add(tup[1]) # add course to set

print(courses_set) 


# 2
for name, course in info:
    if (course == "English"):
        print(name) 


# 3
dict = {}

for name, course in info:
    if (dict.get(name) == None): 
        dict.update({name : set()}) # add name as key and empty set as value to dict
        dict[name].add(course) # add course to the set corresponding to the name key
    else:
        dict[name].add(course) # add course to the name that already exists in the dict

print(dict)