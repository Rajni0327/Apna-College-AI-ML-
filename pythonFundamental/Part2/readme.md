# Python Control Flow & Functions Tutorial

A comprehensive guide to Python control flow statements, loops, and functions. This tutorial builds upon Python basics and covers conditional statements, iteration, and function creation.

## 📚 Contents

- Conditional Statements (if/elif/else)
- Nested Conditions
- Match-Case Statements
- While Loops
- For Loops
- Break and Continue Statements
- Range Function
- Functions (Definition, Parameters, Return Values)
- Lambda Functions
- Higher-Order Functions

## 🚀 Getting Started

### Prerequisites

- Python 3.10+ (for match-case statements)
- Completion of Python basics (variables, operators, data types)

### Running the Code

```bash
python control_flow.py
```

## 📖 Topics Covered

### 1. Conditional Statements

Execute different code blocks based on conditions.

#### Basic If-Else
```python
if condition:
    # code if condition is True
else:
    # code if condition is False
```

#### If-Elif-Else
```python
if condition1:
    # code
elif condition2:
    # code
else:
    # code
```

**Practice Examples:**
- Age verification for voting
- Traffic light system
- Age categorization (child/teenager/adult)
- Login authentication
- Even/odd number checker
- Multiple of 5 checker

### 2. Nested Conditions

Conditions inside other conditions for complex logic.

```python
if condition1:
    if condition2:
        # nested code
    else:
        # nested else
else:
    # outer else
```

### 3. Match-Case Statement

Python 3.10+ feature for pattern matching (similar to switch-case in other languages).

```python
match variable:
    case "value1":
        # code
    case "value2":
        # code
    case _:
        # default case
```

**Example:** Traffic light system using match-case

### 4. While Loops

Repeat code while a condition is True.

```python
while condition:
    # code to repeat
    # update condition to avoid infinite loop
```

**Practice Examples:**
- Counter loop (1 to 5)
- Reverse countdown (10 to 1)
- Multiplication table generator

### 5. Break and Continue

**Break:** Exit the loop immediately
```python
while condition:
    if break_condition:
        break
    # code
```

**Continue:** Skip current iteration and move to next
```python
while condition:
    if skip_condition:
        continue
    # code
```

**Practice Examples:**
- Break when number is divisible by 6
- Skip multiples of 3 using continue
- Print odd numbers (two methods)

### 6. For Loops

Iterate over sequences (strings, lists, ranges).

```python
for variable in sequence:
    # code to repeat
```

**Membership Operator:** `in` checks if element exists in sequence

**Practice Examples:**
- Iterate through string characters
- Count specific characters in a string
- Count vowels in a word
- Sum of first n natural numbers

### 7. Range Function

Generate sequences of numbers for iteration.

```python
range(stop)              # 0 to stop-1
range(start, stop)       # start to stop-1
range(start, stop, step) # start to stop-1 with step
```

**Examples:**
```python
range(5)        # 0, 1, 2, 3, 4
range(1, 6)     # 1, 2, 3, 4, 5
range(1, 11, 2) # 1, 3, 5, 7, 9
```

### 8. Functions

Reusable blocks of code that perform specific tasks.

#### Function Definition
```python
def function_name(parameters):
    # code
    return value
```

#### Function Call
```python
result = function_name(arguments)
```

#### Default Parameters
```python
def function_name(a, b=default_value):
    return a + b
```

**Practice Examples:**
- Hello World function
- Sum of two numbers
- Average of three numbers
- Factorial calculator

### 9. Types of Functions

1. **Built-in Functions:** Pre-defined in Python
   - `print()`, `input()`, `len()`, `type()`, `range()`, etc.

2. **User-Defined Functions:** Created by programmers
   - Custom functions for specific tasks

3. **Lambda Functions:** Anonymous functions
   ```python
   lambda arguments: expression
   # Example: lambda a, b: a + b
   ```

4. **Higher-Order Functions:** Functions that take other functions as arguments or return functions

## 💡 Key Concepts

### Loop Control
- **Break:** Exits the loop completely
- **Continue:** Skips to next iteration
- **Iterator:** Variable that controls loop execution

### Function Components
- **Definition:** Creating the function with `def`
- **Parameters:** Variables in function definition
- **Arguments:** Values passed when calling function
- **Return:** Send result back to caller

### Best Practices
- Use meaningful variable names
- Add comments for complex logic
- Avoid infinite loops (always update loop condition)
- Use functions to avoid code repetition
- Keep functions focused on single tasks

## 🎯 Practice Problems Included

1. **Voting Age Checker:** Verify if user can vote
2. **Traffic Light System:** Simulate traffic signals
3. **Age Categorizer:** Classify as child/teenager/adult
4. **Login System:** Authenticate username and password
5. **Even/Odd Checker:** Determine number parity
6. **Multiplication Table:** Generate table for any number
7. **Character Counter:** Count specific characters in strings
8. **Vowel Counter:** Count vowels in words
9. **Natural Numbers Sum:** Calculate sum of first n numbers
10. **Factorial Calculator:** Compute factorial using function

## 📝 Code Examples

### Traffic Light System
```python
color = input("Enter color: ")

if color == "red":
    print("stop")
elif color == "yellow":
    print("get ready")
elif color == "green":
    print("go")
else:
    print("invalid color")
```

### Multiplication Table
```python
n = int(input("Enter a number: "))
i = 1
while (i <= 10):
    print(n * i)
    i += 1
```

### Vowel Counter
```python
word = "artificial"
count = 0
for char in word:
    if char in 'aeiou':
        count += 1
print("Number of vowels:", count)
```

### Factorial Function
```python
def calc_factorial(n):
    fact = 1   
    for i in range(1, n+1):
        fact *= i
    return fact

n = int(input("Enter a number: "))
print(calc_factorial(n))
```

## ⚠️ Common Mistakes to Avoid

1. **Infinite Loops:** Always update loop variables
   ```python
   # Wrong
   i = 1
   while i <= 10:
       print(i)
   # i is never updated!
   ```

2. **Indentation Errors:** Python uses indentation for code blocks
   ```python
   # Wrong
   if condition:
   print("Hello")  # IndentationError
   
   # Correct
   if condition:
       print("Hello")
   ```

3. **Missing Return Statement:** Functions without return give `None`
4. **Off-by-One Errors:** Remember `range(5)` gives 0-4, not 1-5
5. **Modifying Loop Variable Incorrectly:** Can cause skipped iterations


