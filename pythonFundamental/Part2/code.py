# # Conditional Statements ----------------------------

# age = 21 
# if age >= 18:
#     print("You can Vote.")
#     print ("You can drive")
# else :
#     print("You cannot Vote.")


# color = input ("enter color :")

# if color == "red":
#     print("stop")
# elif color == "yellow":
#     print("get ready")
# elif color == "green":
#     print("go")
# else:
#     print("invalid color")


# age = int(input("Enter your age: "))

# if (age < 13):
#     print("child")
# elif (age >= 13 and age < 18):
#     print("teenager")
# else:
#     print("adult")


# username = input("Enter username: ")
# password = input("Enter password: ")

# if username == "admin" and password == "pass":
#     print("Login successful")
# elif username != "admin":
#     print("Invalid username")
# else :
#     print("Invalid password")


# num = int(input("Enter a number: "))

# if num % 5 == 0:
#     print("multiple of 5")
# else:
#     print("not a multiple of 5")

# #to check if a number is even or odd
# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print("even")
# else:
#     print("odd")


#nesting - condition inside another condition ----------------------

# username = input("Enter username: ")
# password = input("Enter password: ")

# if(username == "admin" and password == "pass"):
#     print("Login successful")
# else:
#     if (username != "admin"):
#         print("Invalid username")
#     else :
#         print("Invalid password")


##match case statement ----------------------------

# color = input("Enter color: ")

# match color:
#     case "Green":
#         print("Go")
#     case "Yellow":
#         print("Get Ready")
#     case "Red":
#         print("Stop")
#     case _:
#         print("Invalid Color")


##loops -----------------------------

##while

# counter = 1   #iterator
# while (counter <= 5):
#     print("Hello", counter)
#     counter += 1


# #reverse loop 
# count = 10 
# while (count >=1) :
#     print(count)
#     count -= 1




##print multiplication table of any number

# n = int(input("Enter a number: "))
# i = 1
# while (i <= 10):
#     print(n*i)
#     i += 1


##break and continue -----------------------------

# i = 1 
# while (i <= 10):
#     if (i % 6 == 0):
#         break
#     print(i)
#     i += 1

# print("outside loop now...")




# i = 1

# while (i <= 10):
#     if ( i % 3 ==0):
#         i += 1
#         continue
#     print(i)
#     i += 1

# print ("outside loop now...")


##print odd numbers 

# i = 1 

# while (i <= 10):
#     print (i)
#     i += 2
# print("outside loop now...")

# i = 0 
# while (i < 10):
#     i += 1
#     if (i % 2 == 0):
#         continue
#     print(i)


##for loop

# string = "Hello"
# #in = membership operator
# for var in string:
#     print(var)

# string = "Hello" #o
# if 'o' in string:
#     print("present")

# for i in range(5):
#     print(i)


# word = "artificial intelligence"

# # count the number of i in the word
# count = 0
# for char in word:
#     if (char == 'i'):
#         count += 1

# print("Number of i's :", count)


# print vowels count of the given string

# word = "artificial"
# count = 0
# for char in word:
#     if (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
#         count += 1

# print("Number of vowels :", count)


# range() -> used to generate a sequence of numbers
#  range(start, stop, step)


# for i in range(5):
#     print(i)

# for i in range(1,6):
#     print(i)

# for i in range(1, 11, 2):
#     print(i)



#print sum of first n natural numbers

# n = int(input("Enter a number: "))
# sum = 0
# for i in range(1, n+1):
#     sum += i

# print ("sum = " ,sum)


## functions -----------------------------
# -> block of code that performs a specific task
# -> reusable code

# def hello():
#     print("Hello World") #function definition

# hello() #function call


# # parameters 
# def sum(a, b):
#     s = a + b
#     return s

# ans = sum(2, 3) #function call with arguments
# print(ans)
# # or
# print(sum(2, 3)) 


# def avg(a, b, c):
#     s = a + b + c
#     return s/3

# print(avg(2, 3, 4))



# # default parameters
# def sum(a , b = 1):
#     return a + b

# print(sum(2)) #b will take default value 1



# types of functions
# 1. built-in functions -> pre-defined functions in python
# 2. user-defined functions -> functions defined by the user