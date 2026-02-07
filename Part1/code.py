print("hello world")


#calculate avg of two numbers 

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
avg = (a + b) / 2
print("Average of two numbers is:", avg)



#Variables------------------------------
name = "Rajni" 
age = 30 
PI = 3.14 
word = "arificial intelligence" 
print ("value of PI =", PI)



#Datatypes------------------------------
x = 10 
print(type(x)) # <class 'int'>

PI = 3.14 
print(type(PI)) # <class 'float'> 

name = "shradha" 
print(type(name)) # <class 'str'> 

isTeacher = True
print(type(isTeacher)) #<class'bool'>

empty_var=None
print(type(empty_var)) #<class'NoneType'>


#Type Conversion------------------------------

#Implicite Conversion
x = 10
y = 3.14
print(x + y) # 13.14    #int + float = float

#Explicite Conversion
x = 10
y = float(x)  #int to float
z = str(x)    #int to str

'''
int() , float() , str() , bool(), list() , tuple() common type conversion functions
'''

#Operators------------------------------


#Arithmetic Operators
a = 5
b = 10

print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a % b)  # Modulus
print(a ** b) # Exponentiation/power

#Reational/Comparison Operators
x = 10
y = 20
print(x == y)  # Equal to    (False)
print(x != y)  # Not equal to  (True)
print(x > y)   # Greater than  (False)
print(x < y)   # Less than   (True)
print(x >= y)  # Greater than or equal to  (True)
print(x <= y)  # Less than or equal to   (True)


#Assignment Operators
a = 5   #simple assignment
print("a =", a)  #5

x += 5  # x = x + 5
print("x += 5:", x)  #15

x *= 2  # x = x * 2
print("x *= 2:", x)  #30

x -= 10  # x = x - 10
print("x -= 10:", x)  #20

x /= 4  # x = x / 4
print("x /= 4:", x)  #5.0

x %= 3  # x = x % 3
print("x %= 3:", x)  #2.0

x**= 3  # x = x ** 3
print("x **= 3:", x)  #8.0


#Logical Operators
x = 10
y = 20
z = 5

#AND
print(x < y and x > z)  # True

#OR
print(x < y or x < z)   # True

#NOT
print(not(x < y))       # False
print(not(x > y))       # True


'''
Operator Precedence:
1. Parentheses ()
2. Exponentiation **
3. Multiplication *, Division /, floor // ,Modulus %
4. Addition +, Subtraction -
5. Comparison Operators (< , <= , > , >= , != , ==)
6. Logical Operators (not , and , or)
7. Assignment Operators (= , += , -= , *= , /= , %= , **= )
'''

#Input and Output------------------------------

name = input("Enter your name: ")
print("Hello,", name)
print(type(name))  # type is string

#program to add 2 numbers by taking input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(num1 + num2)


#calculate avg of two numbers 

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
avg = (a + b) / 2
print("Average of two numbers is:", avg)
