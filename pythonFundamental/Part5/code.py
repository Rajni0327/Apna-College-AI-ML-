# file i/o---------------------------------------------------

# Open 
# Operations 
# -read 
# -write    
# -append 
# Close
# delete




# to open 
f = open("sample.txt","r") #returns file object

data = f.read()
print(type(data))


data = f.readline()
print(data)

data = f.readline()
print(data) 

data = f.readline()
print(data) 


# to write 
f = open("sample.txt","w") 
f.write("Text to overwrite \nit changes the complete data.")



f.close()


# file operations ------------------------------------------
# modes

# r : reading [default]
# w : writing truncates file first , overwrite from the start
# x : creates new and open for writing 
# a : writing, appends at end
# b : binary mode 
# t : text mode [default]
# + : opens disk file for update (r and w)
# "rt" : Read text (default)
# "rb" : Read binary
# "wb" : Write binary
# "ab" : Append binary



# a :append

f = open("sample.txt","a") 
f.write("\nnew text being appended\nto the file")

# x :tp create and write 

f = open("sample2.txt","x")
f.write("Some random Text")

# r+
# the file must exist 
# does not delete old data 
#  writing starts from the current pointer(beginning by default)

f = open("sample.txt", "r+")
print(f.read())
f.write("\nAdded Text")
f.close() 


# w+
# deletes old content 
# creates file if not exists

f = open("sample.txt", "w+")
f.write("New Data")
print(f.read())
f.close()


# a+
# append and read 
# writing always at end 
# creates file if not exists 
# does not delete old data 

f = open("sample.txt", "a+")
f.write("\nAnother Line")
print(f.read())

f.close()





# with keyword-------------------------------------------
# automatically closes the file 

with open("sample.txt", "r") as f:
    # print(f.read())
    data = f.read()
    print(len(data))


# Delete files
import os 

os.remove("sample2.txt")




# word search --------------------------------------------------------

word = "Python"
data = True
line = 1

with open("sample.txt","r") as f:
    while data :
        data = f.readline()

        if (word in data):
            print(f"{word} word found at line {line}")
            break
        line += 1



# Exception Handling ------------------------------------------------------
# if error not handled , it stops the program


# try, except, else, finally 

try:   
    x = int(input("enter x : "))
    ans = 10/x

except ZeroDivisionError:
    print(f"Divide by 0 is not allowed")

except ValueError:
    print(f"Invalid input")

else:     #runs when no exception occurs
    print(f"answer : {ans}")

finally:   #always runs (whether theres an error or not)
    print("End of Program")


# List Comprehensions ----------------------------------------------------
# Output for item in iterable if condition

# normal way
sqr = []
for i in range(6):
    sqr.append(i*i)
print(sqr)

# in single line 
sqr = [i*i for i in range(6)]
print(sqr)

# if
# to print the sqr root of odd numbers 

sq = [i*i for i in range(6) if i%2 != 0]
print(sq)


# if-else
# expression_if_true if condition else expression_if_false for item in iterable
# to replace negative number to 0 

nums = [-2, -4, 3, 5, 6, 1]

nums = [0 if val < 0 else val for val in nums]
print(nums)


# strings

words = ["hello", "python", "apnacollege"]

words = [val.upper() for val in words]
print(words)


# JSON Module----------------------------------------------------------
# JSON (JavaScript Object Notation) is a format used to store and exchange data.
# Convert Python objects → JSON (Serialization)
# Convert JSON → Python objects (Deserialization)

# json.loads()  -loads doesnt mean plural ,here s stands for the string 
#  converts JSON strings to python

# import json 

json_str = '{"name": "Samay","isTeacher": true }'   # <class 'str'>

py_obj = json.loads(json_str)

print(type(py_obj))



# json.dumps()  -converts python to JSON string
import json

py_obj = {
    "name" : "Samay",
    "isTeacher" : True
}

json_str = json.dumps(py_obj)

print(type(json_str))



# json.load() -read JSON from file

import json 

with open("data.json", "r") as f:
    py_obj = json.load(f)
    print(py_obj)


# json.dump()- write from json file

import json 

data = {
    "name" : "Samay" ,
    "age" :27 ,
    "isTeacher" :True 
}

with open("data.json", "w") as f:
    json.dump(data, f, indent= 4, sort_keys= 4)

