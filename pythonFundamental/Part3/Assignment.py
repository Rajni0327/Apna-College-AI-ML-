# answer 1 -----------------------------------------

str = input("Enter a string: ")
    
if (str == str[::-1]): # string slicing to reverse the string and then compare with og string
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


# answer 2 -----------------------------------------
list= [1, 2, 3, 4, 5]
sum = 0
for val in list :
    sum += val

print(f"avg is {sum/len(list)}") # calculate average by dividing sum by length of list

# answer 3 -----------------------------------------

list1 = [1, 2, 7]
list2 = [2, 4, 5]

merge_list = list1 + list2 
print(merge_list) # [1, 2, 7, 2, 4, 5]

result = [1, 2, 3, 54, 5, 7] 
result.sort() 
print(result) 



# answer 4 -----------------------------------------

tup = (1,2,3,4,5,6,7,8,9,10)
even_tup = tuple() # create an empty tuple to store even numbers
odd_tup = tuple() # create an empty tuple to store odd numbers

for val in tup:
    if (val % 2 == 0):
        even_tup += (val,) # add even number to even_tup
    else:
        odd_tup += (val,) # add odd number to odd_tup

print(even_tup) 
print(odd_tup) 



# answer 5 -----------------------------------------

dict = {
    "Anita" : 85,
    "Suresh" : 92,
    "Ravi" : 78,
    "Priya" : 90,
    "Amit" : 88,
    "Samantha" : 95
}

def add_student():
    name = input("Enter student name : ")
    marks = int(input("Enter student marks : "))

    dict[name] = marks # add name and marks to the dictionary
    print(f"{name} added to the dictionary successfully.")

def update_marks():
    name = input("Enter student name : ")
    marks = int(input("Enter new marks : "))

    if (dict.get(name) != None): # check if the name exists in the dictionary
        dict[name] = marks # update marks for the name
        print(f"{name}'s marks updated successfully.")
    else:
        print("Student not found in the dictionary.")

def search_student():
    name = input("Enter student name : ")

    if (dict.get(name) != None): # check if the name exists in the dictionary
        print(f"{name} : {dict[name]}") # print name and marks
    else:
        print("Student not found in the dictionary.")

def display_students():
    for name, marks in dict.items(): # iterate through the dictionary items
        print(f"{name} : {marks}") # print name and marks

print(dict)

print("A to Add student")
print("B to Update marks")
print("C to Search student")
print("D to Display all students")

answer = input("Enter your choice : ")

if (answer == "A"):
    add_student()
elif (answer == "B"):
    update_marks()
elif (answer == "C"):
    search_student()
elif (answer == "D"):
    display_students()
else:
    print("Invalid choice.")


# answer 6 -----------------------------------------

word = ["apple", "banana", "kiwi", "cherry", "mango"]
dict = {}
for val in  word:
    dict[val] = len(val) # add word as key and its length as value to the dictionary

print(dict)


# answer 7 -----------------------------------------

str= input("Enter a string : ")
num = 0

for ch in str:
    if ch == " ":
        num += 1 

print(f"Number of words in the string is {num}")


# answer 8 -----------------------------------------

list1 = [1, 2, 3, 4]
list2 = [2, 6, 7, 8]

set1 = set(list1) # convert list1 to set
set2 = set(list2) # convert list2 to set
if (set1.intersection(set2) != set()): # check if the intersection of two sets is not empty
    print("share common elements")
else:
    print("share no common elements")


# answer 9 -----------------------------------------

list = [1, 2, 3, 4, 5, 5, 5, 3, 2]
seen = set()
duplicates = set()

for item in list:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)

print(f"Elements appearing more than once: {duplicates}")


# answer 10 -----------------------------------------

str = input("Enter a string : ")

unique_chars = set() 
count = set()

for ch in str:
    if ch in unique_chars:
        count.add(ch) # add character to count set if it is already in unique_chars set
    else:
        unique_chars.add(ch) # add character to unique_chars set if it is not already present

print(f"all unique characters are {unique_chars}")
print(f"the count of unique characters is {len(count)}")