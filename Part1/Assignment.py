#Answer 1------------------------------------------
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello, " + name + "! You are " + age + " years old.")

#Answer 2 ------------------------------------------
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2

print("Sum:", sum)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)

#Answer 3 ------------------------------------------
int1 = int(input("Enter first integer: "))
int2 = int(input("Enter second integer: "))
float1 = float(input("Enter first float: "))

num1 = float(int1)
num2 = float(int2)

avg = (num1 + num2 + float1) / 3
print("Average:", avg)


#Answer 4 ------------------------------------------

num_str = input("Enter a number as a string: ")

num_int = int(num_str)  #string to integer
num_float = float(num_str) #string to float
num_str_converted = str(num_float)   #float to string

print("Integer:", num_int)
print("Float:", num_float)
print("String:", num_str_converted)

#Answer 5 ------------------------------------------

x = 10 + 3 * 2 ** 2 
print("Value of x:", x)  #22
# Because:
# According to operator precedence:
# 1. Exponentiation: 2 ** 2 = 4
# 2. Multiplication: 3 * 4 = 12
# 3. Addition: 10 + 12 = 22


#Answer 6 ------------------------------------------
#  to swap values of two numbers
a = input("Enter the first number: ")
b = input("Enter the second number: ")

print("Before swapping: a =", a, " b =", b)

a, b = b, a

print("After swapping: a =", a, " b =", b)

#Answer 7 ------------------------------------------
temp_celsius = input("Enter temperature in Celsius: ")
temp_celsius = float(temp_celsius)
temp_fahrenheit = (temp_celsius * 9/5) + 32

print("Temperature in Fahrenheit:", temp_fahrenheit)


#Answer 8 ------------------------------------------

pi = 3.14
radius = float(input("Enter the radius of the circle: "))
area = pi * radius ** 2

print("Area of the circle:", area)

#ANswer 9 ------------------------------------------

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest:", simple_interest)

#Answer 10 ------------------------------------------

num = float(input("Enter a decimal number: "))

# Extract integer part
integer_part = int(num)

# Extract fractional part
fractional_part = num - integer_part

print("Integer part:", integer_part)
print("Fractional part:", fractional_part)