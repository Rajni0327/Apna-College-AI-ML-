# Python Data Structures Tutorial

A comprehensive guide to Python's fundamental data structures including strings, lists, tuples, dictionaries, and sets. Master the essential tools for organizing and manipulating data in Python.

## 📚 Contents

- Strings (Creation, Indexing, Slicing, Formatting)
- Lists (Mutable Sequences, Methods, Operations)
- Tuples (Immutable Sequences, Methods)
- Dictionaries (Key-Value Pairs, Methods)
- Sets (Unique Values, Set Operations)

## 📖 Topics Covered

### 1. Strings

Strings are sequences of characters used to store text.

#### Creation
```python
word = "python"  # Double quotes
word = 'python'  # Single quotes
```

#### String Length
```python
len(word)  # Returns number of characters
```

#### String Concatenation
```python
word1 = "I Love"
word2 = "Python"
result = word1 + " " + word2  # "I Love Python"
```

#### String Indexing
- Each character has an index starting from 0
- **Important:** Strings are **immutable** (cannot be changed)

```python
word = "python"
print(word[0])   # 'p'
print(word[-1])  # 'n' (last character)
```

#### String Slicing
Create substrings using `string[start:end:step]`

```python
word = "I study from Apna College"
word[0:3]     # "I s"
word[2:8]     # "study "
word[2:]      # "study from Apna College"
word[:8]      # "I study "
word[-5:-1]   # "Colle"
```

#### String Formatting

**1. format() Method**
```python
a = 5
b = 10
sum = a + b

# Basic placeholder
print("sum is {}".format(sum))

# Multiple placeholders
print("sum of {} and {} is {}".format(a, b, sum))

# Index-based
print("sum of {1} and {0} is {2}".format(a, b, sum))

# Named parameters
print("values are {a} and {b}".format(a=5, b=10))
```

**2. f-strings (Modern & Recommended)**
```python
a = 5
b = 10
print(f"sum of {a} and {b} is {a + b}")
print(f"avg is {(a + b)/2}")
```

---

### 2. Lists

Mutable sequences that can store multiple values of any type.

#### Creation and Basic Operations
```python
marks = [85, 90, 78, 92, 100]
print(len(marks))  # Length of list
```

#### Indexing
```python
print(marks[0])   # 85
marks[2] = 80     # Lists are mutable - can modify elements
```

#### Slicing
Create sublists using `list[start:end:step]`

```python
marks = [85, 90, 78, 92, 65, "abc", 67.56]

marks[2:5]   # [78, 92, 65]
marks[:4]    # [85, 90, 78, 92]
marks[3:]    # [92, 65, 'abc', 67.56]
marks[-3:]   # [65, 'abc', 67.56]
```

#### List Methods

| Method | Description | Example |
|--------|-------------|---------|
| `append(value)` | Add element to end | `num.append(4)` |
| `insert(idx, value)` | Insert at specific index | `num.insert(2, 10)` |
| `sort()` | Sort in ascending order | `num.sort()` |
| `sort(reverse=True)` | Sort in descending order | `num.sort(reverse=True)` |
| `reverse()` | Reverse the list | `num.reverse()` |

#### Loops with Lists
```python
num = [1, 2, 3, 4, 5]

# Iterate through values
for val in num:
    print(val)

# Linear search example
x = 3
for idx, val in enumerate(num):
    if val == x:
        print(f"{x} found at index {idx}")
        break
```

---

### 3. Tuples

Immutable sequences of values. Once created, cannot be modified.

#### Creation
```python
tup = (1, 2, 3, 4, 5, "abc", 67.56)
print(type(tup))  # <class 'tuple'>

# Single element tuple (note the comma!)
single_tup = (5,)      # Tuple
single_tup2 = (5)      # Integer (not a tuple)
```

#### Immutability
```python
tup[2] = 10  # ❌ ERROR: Tuples are immutable
```

#### Indexing and Slicing
Same syntax as lists:
```python
tup = (1, 2, 3, 4, 5)
tup[0]       # 1
tup[2]       # 3
tup[1:4]     # (2, 3, 4)
tup[:3]      # (1, 2, 3)
tup[3:]      # (4, 5)
tup[-1]      # 5
```

#### Tuple Methods

| Method | Description | Example |
|--------|-------------|---------|
| `index(value)` | Find first occurrence index | `t.index(2)` |
| `count(value)` | Count occurrences | `t.count(2)` |

#### Loops with Tuples
```python
tup = (1, 2, 3, 4, 5)
sum = 0
for val in tup:
    sum += val
print(f"sum of values is {sum}")
```

---

### 4. Dictionaries

Mutable collections of key-value pairs. Unordered (order depends on keys).

#### Creation
```python
info = {
    "name": "Samantha",
    "cgpa": 9.2,
    "subjects": ["math", "science"],
    3.14: "pi"
}
```

#### Key Features
- Keys must be unique (values can be duplicate)
- Keys can be strings, numbers, or tuples
- Values can be any data type
- Unordered collection

#### Accessing Values
```python
print(info["name"])      # "Samantha"
print(info["cgpa"])      # 9.2
print(info[3.14])        # "pi"

# Modifying values
info["cgpa"] = 9.5
```

#### Dictionary Methods

| Method | Description | Example |
|--------|-------------|---------|
| `keys()` | Returns all keys | `info.keys()` |
| `values()` | Returns all values | `info.values()` |
| `items()` | Returns key-value pairs as tuples | `info.items()` |
| `get(key)` | Returns value (None if key doesn't exist) | `info.get("name")` |
| `update(dict)` | Add new items | `info.update({"city": "Delhi"})` |

#### Converting Dictionary Views to Lists
```python
keys_list = list(info.keys())
values_list = list(info.values())
items_list = list(info.items())
```

---

### 5. Sets

Unordered collections of unique values.

#### Creation
```python
set = {1, 2, 2, 2, 3}
print(set)  # {1, 2, 3} - duplicates removed

# Empty set (important!)
empty_dict = {}        # This is a dictionary, NOT a set
empty_set = set()      # This is an empty set
```

#### Set Characteristics
- Stores only unique values (duplicates automatically removed)
- Unordered collection
- Sets are mutable, but elements must be immutable
- Elements can be: strings, numbers, tuples
- Elements cannot be: lists, dictionaries

#### Set Methods

| Method | Description | Example |
|--------|-------------|---------|
| `add(value)` | Add element | `s.add(4)` |
| `remove(value)` | Remove element (error if not found) | `s.remove(1)` |
| `clear()` | Remove all elements | `s.clear()` |
| `pop()` | Remove and return random element | `s.pop()` |
| `union(set2)` | Return union of sets | `s1.union(s2)` |
| `intersection(set2)` | Return intersection of sets | `s1.intersection(s2)` |

#### Set Operations
```python
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 8, 9, 10}

# Union (all unique elements from both)
s1.union(s2)  # {1, 2, 3, 4, 5, 8, 9, 10}

# Intersection (common elements)
s1.intersection(s2)  # {4, 5}
```

---

## 🔍 Quick Comparison Table

| Feature | String | List | Tuple | Dictionary | Set |
|---------|--------|------|-------|------------|-----|
| Mutable | ❌ | ✅ | ❌ | ✅ | ✅ |
| Ordered | ✅ | ✅ | ✅ | ❌* | ❌ |
| Indexed | ✅ | ✅ | ✅ | ✅ (by key) | ❌ |
| Duplicates | ✅ | ✅ | ✅ | Keys: ❌, Values: ✅ | ❌ |
| Syntax | `"..."` or `'...'` | `[...]` | `(...)` | `{k:v}` | `{...}` or `set()` |

*Python 3.7+ maintains insertion order for dictionaries

---

## 💡 Key Concepts

### Mutability vs Immutability

**Mutable (Can be changed):**
- Lists
- Dictionaries
- Sets

**Immutable (Cannot be changed):**
- Strings
- Tuples
- Numbers

### When to Use Each Data Structure

**Strings:**
- Storing and manipulating text
- User input, file content, messages

**Lists:**
- Ordered collection that needs modification
- When you need to add/remove/sort items
- Dynamic data that changes over time

**Tuples:**
- Ordered collection that shouldn't change
- Function return multiple values
- Dictionary keys (lists can't be keys)
- Slightly faster and more memory-efficient than lists

**Dictionaries:**
- Key-value associations
- Fast lookups by key
- Storing structured data (like JSON)

**Sets:**
- Remove duplicates from a collection
- Mathematical set operations (union, intersection)
- Membership testing (faster than lists)

---

## 🎯 Practice Examples

### String Manipulation
```python
# Count specific character
word = "artificial intelligence"
count = word.count('i')
```

### Linear Search in List
```python
num = [1, 2, 3, 4, 5]
x = 3
for idx, val in enumerate(num):
    if val == x:
        print(f"{x} found at index {idx}")
```

### Tuple Sum
```python
tup = (1, 2, 3, 4, 5)
total = sum(tup)
```

### Dictionary Operations
```python
info = {"name": "Sam", "age": 25}
info.update({"city": "Delhi"})
print(list(info.keys()))
```

### Set Operations
```python
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
common = s1.intersection(s2)
all_elements = s1.union(s2)
```

---

## ⚠️ Common Mistakes to Avoid

1. **String Immutability**
   ```python
   word = "python"
   word[0] = 'j'  # ❌ ERROR: Strings are immutable
   ```

2. **Single Element Tuple**
   ```python
   tup = (5)    # ❌ This is an integer
   tup = (5,)   # ✅ This is a tuple
   ```

3. **Empty Set vs Dictionary**
   ```python
   empty = {}      # ❌ This is a dictionary
   empty = set()   # ✅ This is a set
   ```

4. **Modifying Tuple**
   ```python
   tup = (1, 2, 3)
   tup[0] = 10  # ❌ ERROR: Tuples are immutable
   ```

5. **List as Dictionary Key**
   ```python
   d = {[1, 2]: "value"}  # ❌ ERROR: Lists are mutable
   d = {(1, 2): "value"}  # ✅ Tuples can be keys
   ```



