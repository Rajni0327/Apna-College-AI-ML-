# Python Basics Tutorial

A comprehensive beginner's guide to Python fundamentals, covering essential concepts from basic syntax to operators and input/output operations.

## 📚 Contents

This tutorial covers the following Python fundamentals:

- Variables and Constants
- Data Types
- Type Conversion
- Operators (Arithmetic, Relational, Assignment, Logical)
- Input and Output Operations
- Operator Precedence

## 📖 Topics Covered

### 1. Variables

Variables store data values. Python is dynamically typed, so you don't need to declare variable types explicitly.

```python
name = "Rajni" 
age = 30 
PI = 3.14
```

### 2. Data Types

Python supports several built-in data types:

- `int` - Integer numbers
- `float` - Decimal numbers
- `str` - String/Text
- `bool` - Boolean (True/False)
- `NoneType` - Represents absence of value

### 3. Type Conversion

**Implicit Conversion**: Python automatically converts data types
```python
x = 10      # int
y = 3.14    # float
print(x + y)  # Result: 13.14 (automatically converted to float)
```

**Explicit Conversion**: Manual type conversion using functions
```python
x = 10
y = float(x)  # Convert int to float
z = str(x)    # Convert int to string
```

Common conversion functions: `int()`, `float()`, `str()`, `bool()`, `list()`, `tuple()`

### 4. Operators

#### Arithmetic Operators
- `+` Addition
- `-` Subtraction
- `*` Multiplication
- `/` Division
- `%` Modulus (remainder)
- `**` Exponentiation (power)

#### Relational/Comparison Operators
- `==` Equal to
- `!=` Not equal to
- `>` Greater than
- `<` Less than
- `>=` Greater than or equal to
- `<=` Less than or equal to

#### Assignment Operators
- `=` Simple assignment
- `+=` Add and assign
- `-=` Subtract and assign
- `*=` Multiply and assign
- `/=` Divide and assign
- `%=` Modulus and assign
- `**=` Power and assign

#### Logical Operators
- `and` - Returns True if both conditions are true
- `or` - Returns True if at least one condition is true
- `not` - Reverses the boolean value

### 5. Operator Precedence

Understanding the order of operations:

1. Parentheses `()`
2. Exponentiation `**`
3. Multiplication `*`, Division `/`, Floor Division `//`, Modulus `%`
4. Addition `+`, Subtraction `-`
5. Comparison Operators `<`, `<=`, `>`, `>=`, `!=`, `==`
6. Logical Operators `not`, `and`, `or`
7. Assignment Operators `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `**=`

### 6. Input and Output

**Output**: Use `print()` to display information
```python
print("Hello, World!")
```

**Input**: Use `input()` to get user input (always returns a string)
```python
name = input("Enter your name: ")
```

**Type Conversion with Input**: Convert input to required data type
```python
age = int(input("Enter your age: "))
price = float(input("Enter price: "))
```

## 💡 Practice Examples

The code includes practical examples:

1. **Hello World** - Basic output
2. **Average Calculator** - Calculate average of two numbers
3. **Data Type Checker** - Check types of different variables
4. **Calculator Operations** - Perform various arithmetic operations
5. **Logical Comparisons** - Boolean logic examples

