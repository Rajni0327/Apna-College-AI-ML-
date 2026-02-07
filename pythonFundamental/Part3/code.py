#Strings --------------------------------------
#means of storing text in python or sequence of characters
#can be created using single or double quotes

word = "python" 
print(len(word)) #length of the string

# concatination of strings ----------------
word1 = "I Love"
word2 = "Python"
print(word1 + " " + word2)


# String indexing
# each character in a string has an index starting from 0
word = "python"
print(word[0]) #p

word[2] = 'k' #strings are immutable, we cannot change individual characters

# Slicing--------------------------
# creates substrings

str = "Python"
# syntax: string[start:end:step]

word = "I study from Apna College"
print(word[0:3]) #I st

print(word[2:8]) #study f

print(word[2:]) #study from Apna College

print(word[:8]) #I study

print(word[-1]) #e

print(word[-5:-1]) #Colle


# string Formatting--------
# 1 format() method
a = 5
b = 10
sum = a + b
print("sum is {}".format(sum))

print("language is {}".format("Python")) 

print("sum of {} and {} is {}".format(a, b, sum)) #multiple placeholders can be used

# index based formatting ---------
print("sum of {1} and {0} is {2}".format(a, b, sum))

# value based formatting --------
print("values of variables are {a} and {b}".format(a=5, b=10))



# 2 f-strings (literal string interpolation)(modern method)
a = 5
b = 10
print(f"sum of {a} and {b} is {a + b}")
print(f"avg is {(a + b)/2}")

# Lists ---------------------------------------------
# mutable sequence of values

marks = [85, 90, 78, 92, 100]
print(marks)
print(len(marks)) #length of the list

# indexing ------------------
print(marks[0]) #85

marks [2] = 80 #lists are mutable, we can change individual elements
print(marks) 


# slicing --------------------
# creates sublists
# syntax: list[start:end:step]

marks = [85, 90, 78, 92, 65, "abc", 67.56]

print(marks[2:5]) #[78, 92, 65]
print(marks[:4]) #[85, 90, 78, 92]
print(marks[3:]) #[92, 65, 'abc', 67.56]
print(marks[-3:]) #['abc', 67.56]


# Lists methods----------------------
# functions that perform specific operations on lists

# l.append() #adds an element to the end of the list
num = [1, 2, 3]
num.append(4)
print(num) #[1, 2, 3, 4]

# l.insert(idx, value) #inserts an element at a specific index
num.insert(2, 10)
print(num) #[1, 2, 10, 3, 4]

# l.sort() #sorts the list in ascending order
num.sort()
print(num) #[1, 2, 3, 4, 10]

num.sort(reverse=True) #sorts the list in descending order
print(num) #[10, 4, 3, 2, 1]

# l.reverse() #reverses the order of the list
num.reverse()
print(num) #[10, 4, 3, 2, 1]


# loops--------------------------------------
# for loop

num = [1, 2, 3, 4, 5]
for val in num:
    print(val)

# to finds the x in the list

x = 3
idx = 0

for val in num:
    if (val == x):
        print(f"{x} found at index {idx}")
        break 
    idx += 1
# this is also called linear search 


# tuples-----------------------------------------------------------
# immutable sequence of values
# can be created using parentheses

tup = (1, 2, 3, 4, 5, "abc", 67.56)
print(tup)
print(type(tup)) #<class 'tuple'>

tup[2]= 10 #tuples are immutable, we cannot change individual elements

single_tup = (5,) #to create a single element tuple, we need to add a comma after the element
print(single_tup) #(5,)
print(type(single_tup)) #<class 'tuple'>

single_tup2 = (5) #this is not a tuple, it's just an integer
print(single_tup2) #5
print(type(single_tup2)) #<class 'int'>


# indexing and slicing ----------------
tup = (1, 2, 3, 4, 5)
print(tup[0]) #1
print(tup[2]) #3
print(tup[1:4]) #(2, 3, 4)  
print(tup[:3]) #(1, 2, 3)
print(tup[3:]) #(4, 5)
print(tup[-1]) #5
print(tup[-3:-1]) #(3, 4)

# loops --------------------

tup = (1, 2, 3, 4, 5)
sum = 0
for val in tup:
    sum += val
    
print(f"sum of values is {sum}") #sum of values is 15


# tuple methods----------------------
# t.index(value) #returns the index of the first occurrence of the value
t = (1, 2, 3, 4, 5, 2)
print(t.index(2)) #1

# t.count(value) #returns the number of occurrences of the value
print(t.count(2)) #2


# Dictionaries--------------------------------------
# mutable collection of key-value pairs
# can be created using curly braces
# unordered collection of key-value pairs, meaning the order of items depends on the keys and not on the order of insertion.
# keys cannot be duplicate, but values can be duplicate

info = {
    "name" : "Samantha",
    "cgpa" : 9.2,
    "subjects" : ["math","science"],
    3.14 : "pi"
}

print(info)
print(type(info)) #<class 'dict'>


# indexing 
# keys are used to access values in a dictionary

print(info["name"]) #Samantha
print(info["cgpa"]) #9.2
print(info["subjects"]) #['math', 'science']
print(info[3.14]) #pi

info["cgpa"] = 9.5 #dictionaries are mutable, we can change values
print(info) # {'name': 'Samantha', 'cgpa': 9.5, 'subjects': ['math', 'science'], 3.14: 'pi'}


# dictionary methods----------------------
# d.keys() #returns all keys
print(info.keys()) 

dict_keys = info.keys()
print(dict_keys) 

# we can convert dict_keys to a list to access individual keys
keys_list = list(info.keys())
print(keys_list) 

# d.values() #returns all values
print(info.values()) 

dict_values = list(info.values())
print(dict_values) 

# d.items() #returns all key-value pairs as tuples in a list
print(info.items()) 

# d.get(key) #returns val according to key , if key is not present it returns None
print(info.get("name")) #Samantha

# d.update(new_item) # adds new item to dict
info.update ({
    "city" : "Delhi"
})

print(info)



# Sets -------------------------------------------------
# unordered collection of unique values 
# sets are mutable but elements in a set are immutable i.e strings, numbers, tuples can be elements of a set but lists and dictionaries cannot be elements of a set
# created using curly braces or set() function


set = {1, 2, 2, 2, 3}
print(set) #{1, 2, 3} duplicate values are not stored in a set
print(type(set))


empty_set = {} # this is not an empty set, it's an empty dictionary
print(type(empty_set)) #<class 'dict'>

empty_set2 = set() # this is an empty set
print(type(empty_set2)) #<class 'set'>


# set methods----------------------

# s.add(value) #adds an element to the set
set.add(4)
print(set) #{1, 2, 3, 4}

# s.remove(value) #removes an element from the set, if the element is not present it raises an error
set.remove(1)
print(set) #{2, 3, 4}

# s.clear() #removes all elements from the set

# s.pop() #removes and returns a random element from the set
set.pop()
print(set) 

# s.union(set2) #returns a new set that is the union of two sets
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 8, 9, 10}

print(s1.union(s2)) #{1, 2, 3, 4, 5, 8, 9, 10}

#  s.intersection(set2) #returns a new set that is the intersection of two sets
print(s1.intersection(s2)) #{4, 5}