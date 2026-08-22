# 🧪 Lab 01: Python Foundations, Syntax & Golden Rules

Welcome to **Lab 01** of the Python series! This lab covers the absolute foundational principles of Python programming, specifically tailored for **DevOps & MLOps automation**.

---

## 📌 Lab Objectives
By completing this lab, you will master:
1. The **Golden Rules of Python** (Indentation, No semicolons, Comments).
2. How Python handles **Variables & Dynamic Typing**.
3. Core primitive data types: `int`, `float`, `str`, `bool`, and `NoneType`.
4. **Type Casting** (Implicit vs. Explicit conversions and Truthy/Falsy evaluations).
5. Capturing input via `input()` and modern **F-String formatting**.

---

## 🌟 The 3 Golden Rules of Python

### 1. Indentation is Everything
Python does not use curly braces `{ }` to delimit code blocks. Instead, it relies on **indentation whitespace** (4 spaces per level by PEP 8 standard).

```python
# C / Java / PHP Style (Curly Braces):
# if (is_ready) {
#     do_something();
# }

# Python Style (Indentation):
if is_ready:
    do_something()
```

### 2. No Semicolons Required
In Python, statements end with a newline character. No trailing `;` is needed at the end of each line.

```python
# Clean and readable
server_ip = "10.0.0.1"
port = 8000
```

### 3. Comments Use `#`
- Single-line comments start with `#`.
- Multi-line docstrings use triple quotes `""" ... """` or `''' ... '''`.

```python
# This is a single-line comment
"""
This is a multi-line docstring used to document
modules, functions, and classes.
"""
```

---

## 📂 Lab Scripts & Exercises

| Script File | Purpose | Key Concepts |
| :--- | :--- | :--- |
| **`01_golden_rules.py`** | Demonstrates core syntax rules | Indentation blocks, clean line endings, inline & block comments |
| **`02_variables_and_datatypes.py`** | Variable assignments & primitive types | `int`, `float`, `str`, `bool`, `None`, `type()`, `isinstance()`, unpacking |
| **`03_type_casting.py`** | Type conversion mechanisms | Implicit widening, `int()`, `float()`, `str()`, Truthy/Falsy values, error catching |
| **`04_user_input_and_formatting.py`** | CLI input & F-string styling | `input()`, f-strings, alignment, precision (`:.2f`), thousand separators |
| **`05_mini_challenge.py`** | Self-assessment & practice tool | Review quiz, server capacity estimator |

---

## 🛠️ Data Types Cheatsheet

| Type | Name | Example Value | Description |
| :---: | :---: | :---: | :--- |
| `int` | Integer | `42`, `-7`, `1000` | Whole numbers (arbitrary precision) |
| `float` | Floating Point | `3.14`, `-0.001`, `2.0` | Decimal numbers (IEEE 754 double precision) |
| `str` | String | `"MLOps"`, `'prod'` | Immutable sequence of Unicode characters |
| `bool` | Boolean | `True`, `False` | Truth values (subclass of int: 1 and 0) |
| `NoneType`| None | `None` | Represents the null/absence of value |

---

## 🚀 Running the Lab Scripts

Execute any script using Python 3:

```bash
# 1. Run Golden Rules Demo
python 01_golden_rules.py

# 2. Run Variables & Data Types
python 02_variables_and_datatypes.py

# 3. Run Type Casting Demo
python 03_type_casting.py

# 4. Run Input & String Formatting
python 04_user_input_and_formatting.py

# 5. Run Mini Challenge & Quiz
python 05_mini_challenge.py
```

---

## 💡 Key Takeaways for DevOps & MLOps
- `input()` **always** returns a string. Remember to cast it with `int()` or `float()` when calculating CPU limits, ports, or memory thresholds.
- Empty lists `[]`, empty strings `""`, `0`, and `None` evaluate to `False` in conditional statements (truthy/falsy evaluation).
- Use **f-strings** (`f"{variable}"`) for clean log messages, configuration generator scripts, and dynamic file paths.
