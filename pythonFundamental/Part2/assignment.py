# #answer 1 ------------------------------------

# salary =int(input("Enter your salary: "))

# if (salary < 30000):
#     tax = 0.05
# elif (salary >= 30000 and salary < 70000):
#     tax = 0.15
# else:
#     tax = 0.25

# tax_amount = salary * tax
# print("Tax amount: ", tax_amount)

# # answer 2 ------------------------------------

# def even(a,b):
#     even_numbers = []   
#     for i in range(a,b+1):
#         if (i % 2 == 0):
#             even_numbers.append(i)
#     return even_numbers


# print(even(1,10))

# # answer 3 ------------------------------------

# def print_digits(n):
#     digits = []
#     while (n > 0):
#         digits.append(n % 10)
#         n = n // 10   #floor division to remove the decimal part

#     # print in reverse to get correct order
#     for d in reversed(digits):
#         print(d)

# print_digits(645)



# # answer 4 ------------------------------------

# def digit_count(n):
#     count = 0
#     while (n > 0):
#         count += 1
#         n = n // 10
#     return count

# print(digit_count(6))


# # answer 5 ------------------------------------

# def sum_of_digits(n):
#     sum = 0
#     while (n > 0):
#         sum += n % 10
#         n = n // 10
#     return sum

# print(sum_of_digits(1234))


# # answer 6 ------------------------------------

# for i in range(1,100):
#     if (i % 3 == 0 and i % 5 == 0):
#         print(i)                  


# # answer 7 ------------------------------------

# while True:
#     user_input = input("Enter a number (or type 'Quit' to stop): ")

#     if user_input == "Quit":
#         print("Program ended...")
#         break
#     else:
#         number = float(user_input)  # float allows both integers and decimals
#         if number > 0:
#             print("The number is Positive.")
#         elif number < 0:
#             print("The number is Negative.")
#         else:
#             print("The number is Zero.")


# #answer 8 ------------------------------------

# def calculate(a,b,operation):
#     if operation == "+":
#         return a + b
#     elif operation == "-":
#         return a - b
#     elif operation == "*":
#         return a * b
#     elif operation == "/":
#         if b != 0:
#             return a / b
#         else:
#             return "Error: Division by zero is not allowed."
#     else:
#         return "Error: Invalid operation."
    

# print(calculate(10,5,"*"))


# # answer 9 ------------------------------------

# def is_prime(n):
#     for i in range(2, n-1):
#         if n % i == 0:
#             return False
#     return True

# print(is_prime(25))


# # answer 10 ------------------------------------

# secret_num = 7 

# while True:
#     guess = int(input("Guess the number between 1 and 10: "))
#     if guess == secret_num:
#         print("Congratulations! You guessed the number.")
#         break
#     elif guess < secret_num :
#         print("Too low. Try again.")
#     else :
#         print("Too high. Try again.")

