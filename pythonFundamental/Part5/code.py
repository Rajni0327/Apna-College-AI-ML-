# file i/o

# Open 
# Operations 
# -read 
# -write    
# -append 
# Close
# delete




# to open 
# f = open("sample.txt","r") #returns file object

# data = f.read()
# print(type(data))


# data = f.readline()
# print(data)

# data = f.readline()
# print(data) 

# data = f.readline()
# print(data) 


# to write 
# f = open("sample.txt","w") 
# f.write("Text to overwrite \nit changes the complete data.")



# f.close()


# file operations 
# modes

# r : reading [default]
# w : writing truncates file first , overwrite from the start
# x : creates new and open for writing 
# a : writing, appends at end
# b : binary mode 
# t : text mode [default]
# + : opens disk file for update (r and w)



# a :append

# f = open("sample.txt","a") 
# f.write("\nnew text being appended\nto the file")

# x :tp create and write 

# f = open("sample2.txt","x")
# f.write("Some random Text")

# r+
# the file must exist 
# does not delete old data 
#  writing starts from the current pointer(beginning by default)

f = open("data.txt", "r+")
print(f.read())
f.write("\nAdded Text")
f.close() 