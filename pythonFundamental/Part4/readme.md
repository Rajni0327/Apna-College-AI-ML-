# 🐍 Python Object-Oriented Programming (OOP) — Concepts Guide

A beginner-friendly Python script covering all core OOP concepts with practical examples.

---

## 📋 Table of Contents

- [Classes & Objects](#classes--objects)
- [Constructors](#constructors)
- [Attributes](#attributes)
- [Class Methods & Static Methods](#class-methods--static-methods)
- [OOP Pillars](#oop-pillars)
  - [Encapsulation](#encapsulation)
  - [Inheritance](#inheritance)
  - [Abstraction](#abstraction)
  - [Polymorphism](#polymorphism)

---

## Classes & Objects

A **class** is a blueprint for creating objects. An **object** is an instance of a class.

```python
class Student:
    subject = "python"
    college = "abc"

stu1 = Student()
print(stu1.subject)  # python
```

---

## Constructors

The `__init__` method is called automatically every time an object is created.

```python
class Student:
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa

stu1 = Student("Sanaya", 8.0)
```

**Types of constructors:**
- **Default** — only takes `self`
- **Parameterized** — takes `self` + additional arguments

> ⚠️ Python supports only **one constructor** per class. If multiple are defined, only the last one is used.

---

## Attributes

| Type | Belongs To | Description |
|---|---|---|
| Class Attribute | Class | Shared across all objects |
| Instance Attribute | Object | Unique to each object |

> Instance attributes have **higher priority** than class attributes when names conflict.

```python
class Student:
    college_name = "ABC College"   # class attribute

    def __init__(self, name):
        self.name = name           # instance attribute
```

---

## Class Methods & Static Methods

Demonstrated through a **Product Store** example:

```python
class Product:
    count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1

    def get_info(self):              # instance method
        ...

    @classmethod
    def get_count(cls):              # class method
        ...

    @staticmethod
    def calc_discount(price, disc):  # static method
        ...
```

---

## OOP Pillars

### Encapsulation

Wrapping data and functions into a single unit, with access control.

| Modifier | Syntax | Accessible From |
|---|---|---|
| Public | `self.name` | Anywhere |
| Protected | `self._name` | Class + subclasses (by convention) |
| Private | `self.__name` | Class only (name mangling) |

```python
acc1 = BankAccount("Samarth", 100_000)
acc1.set_balance(200_000)       # via setter
acc1.get_balance()              # via getter
```

---

### Inheritance

Reusing attributes and methods from a parent (base) class.

**Types covered:**

**Single Inheritance** — one child inherits from one parent.

**Multi-level Inheritance** — a chain of inheritance.
```python
Employee → AdminStaff → Accountant
```

**Multiple Inheritance** — a child inherits from more than one parent.
```python
class TA(Teacher, Student):
    ...
```

`super()` is used to call the parent class constructor.

---

### Abstraction

Hiding internal implementation details and exposing only essential features. Uses Python's `abc` module.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Lion(Animal):
    def make_sound(self):
        print("Roar!")
```

> Abstract classes **cannot be instantiated** directly — they serve as blueprints.

---

### Polymorphism

"Many forms" — the same interface behaves differently depending on context.

**Operator Overloading**
```python
1 + 2        # 3
"hello" + " world"  # "hello world"
```

**Method Overriding** — redefining a parent class method in a child class. Python always looks in the child class first.

**Duck Typing** — independent classes with the same method name can be used interchangeably.
```python
t1.get_designation()    # designation = Teacher
acc1.get_designation()  # designation = Accountant
```

---

## 🚀 How to Run

```bash
python oop_concepts.py
```

**Requirements:** Python 3.x — no external libraries needed.

---

## 📚 Concepts Summary

| Concept | Description |
|---|---|
| Class | Blueprint for objects |
| Object | Instance of a class |
| Constructor | Initializes object on creation |
| Encapsulation | Bundles data + methods, restricts access |
| Inheritance | Child class reuses parent class features |
| Abstraction | Hides implementation, shows interface |
| Polymorphism | Same interface, different behavior |