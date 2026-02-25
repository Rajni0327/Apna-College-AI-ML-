# Python File I/O, Exception Handling, List Comprehensions & JSON

A beginner-friendly reference covering core Python concepts including file handling, error management, list comprehensions, and JSON processing.

---

## Table of Contents

- [File I/O](#file-io)
- [File Modes](#file-modes)
- [The `with` Keyword](#the-with-keyword)
- [Deleting Files](#deleting-files)
- [Word Search in a File](#word-search-in-a-file)
- [Exception Handling](#exception-handling)
- [List Comprehensions](#list-comprehensions)
- [JSON Module](#json-module)
- The additional files are generated for the assignment

---

## File I/O

Python uses the built-in `open()` function to work with files. The basic operations are **read**, **write**, **append**, and **close**.

```python
# Open and read
f = open("sample.txt", "r")  # returns a file object
data = f.read()               # reads entire file
data = f.readline()           # reads one line at a time
f.close()

# Write (overwrites existing content)
f = open("sample.txt", "w")
f.write("Text to overwrite\nit changes the complete data.")
f.close()
```

---

## File Modes

| Mode | Description |
|------|-------------|
| `r`  | Read (default) |
| `w`  | Write — truncates file first |
| `x`  | Create new file and open for writing |
| `a`  | Append — writes at end of file |
| `b`  | Binary mode |
| `t`  | Text mode (default) |
| `+`  | Open for update (read and write) |
| `r+` | Read & write — file must exist, preserves old data |
| `w+` | Write & read — deletes old content, creates if not exists |
| `a+` | Append & read — preserves old data, creates if not exists |

```python
# Append
f = open("sample.txt", "a")
f.write("\nnew text being appended")

# Create new file
f = open("sample2.txt", "x")
f.write("Some random Text")

# r+ — read then write (pointer at beginning)
f = open("sample.txt", "r+")
print(f.read())
f.write("\nAdded Text")
f.close()
```

---

## The `with` Keyword

Using `with` automatically closes the file after the block finishes — no need to call `f.close()`.

```python
with open("sample.txt", "r") as f:
    data = f.read()
    print(len(data))
```

---

## Deleting Files

Use the `os` module to delete files.

```python
import os
os.remove("sample2.txt")
```

---

## Word Search in a File

Read through a file line by line and search for a specific word.

```python
word = "Python"
data = True
line = 1

with open("sample.txt", "r") as f:
    while data:
        data = f.readline()
        if word in data:
            print(f"{word} found at line {line}")
            break
        line += 1
```

---

## Exception Handling

Prevent your program from crashing by catching errors with `try`, `except`, `else`, and `finally`.

```python
try:
    x = int(input("Enter x: "))
    ans = 10 / x

except ZeroDivisionError:
    print("Divide by 0 is not allowed")

except ValueError:
    print("Invalid input")

else:           # runs only when no exception occurs
    print(f"Answer: {ans}")

finally:        # always runs regardless of errors
    print("End of Program")
```

---

## List Comprehensions

A concise way to create lists using a single line of code.

**Syntax:** `[expression for item in iterable if condition]`

```python
# Squares of 0–5
sqr = [i * i for i in range(6)]

# Squares of odd numbers only
sq = [i * i for i in range(6) if i % 2 != 0]

# Replace negative numbers with 0
nums = [-2, -4, 3, 5, 6, 1]
nums = [0 if val < 0 else val for val in nums]

# Convert strings to uppercase
words = ["hello", "python", "apnacollege"]
words = [val.upper() for val in words]
```

---

## JSON Module

JSON (JavaScript Object Notation) is used to store and exchange data. Python's `json` module handles conversion between Python objects and JSON.

| Function | Description |
|----------|-------------|
| `json.loads()` | JSON string → Python object |
| `json.dumps()` | Python object → JSON string |
| `json.load()`  | Read JSON from a file |
| `json.dump()`  | Write Python object to a JSON file |

```python
import json

# JSON string → Python dict
json_str = '{"name": "Samay", "isTeacher": true}'
py_obj = json.loads(json_str)

# Python dict → JSON string
py_obj = {"name": "Samay", "isTeacher": True}
json_str = json.dumps(py_obj)

# Read from JSON file
with open("data.json", "r") as f:
    py_obj = json.load(f)

# Write to JSON file
data = {"name": "Samay", "age": 27, "isTeacher": True}
with open("data.json", "w") as f:
    json.dump(data, f, indent=4, sort_keys=True)
```

---

## Notes

- Always close files after use, or better yet use the `with` statement.
- The `s` in `json.loads()` and `json.dumps()` stands for **string**.
- `sort_keys` in `json.dump()` should be a boolean (`True`/`False`), not an integer.
