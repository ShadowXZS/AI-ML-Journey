
---

# 🐍 Python Basics Notes

## Printing Output

```python
print("Output")
```

- Displays the string placed between `""`.
- `""` marks the beginning and end of a string.
- Syntax errors are highlighted by the interpreter.

---

## String Manipulation

- `\n` → Creates a line break (no space after `n` for no gap).
- `+` → Concatenates (joins) strings.
- **Indentation matters** → Spaces and tabs are critical.  
    ⚠️ Beware of **IndentationError**.

---

## Input

```python
input("Displayed to User ?")
```

- Prompts the user for input.
- The text inside `""` is shown to the user.

💡 Use **Thonny IDE** for detailed debugging.

---

## Errors & Tracebacks

- **Traceback**: Shows the error message when an exception isn’t handled.
- Read tracebacks **from bottom upward** to locate the source of the error.
- Example: Concatenating a string (`str`) with an integer (`int`) using `+` causes an error.  
    ✅ Solution: Convert one type to match the other.

---

## Type Conversion

- `len()` → Finds the length of a string.
- `str()` → Converts numbers into strings.
- `int()` → Converts input/output into integers.

---

## Variable Naming Rules

- Must be **readable**.
- Written as **one single unit**.
- Use `_` (underscore) to separate words.
- ❌ Do not use reserved words like `print` or `input`.
- Variables must be spelled correctly and case-sensitive.

### Example

```python
name = "Gourav"
```

- `name` → variable
- `"Gourav"` → value assigned to the variable

---

Day 2 

---

# 🐍 Python Notes – Expressions, Data Types & Operations

## ⚠️ `eval()`

- `eval()` → Evaluates expressions inside a string.
- **Avoid using `eval()` unless absolutely necessary**.  
    It can execute arbitrary code → **security risk**.
- Use only with **controlled, safe inputs**.

### Example

```python
print(eval("5+2*3**2"))  # Output: 23
```

---

## 📑 Data Types

### String

- Sequence of characters.
- Access characters using **square brackets**:

```python
print("Hello"[0])   # Output: H
print("Hello"[-1])  # Output: o (last character)
```

### Integer

- Whole numbers (no decimal).

```python
print(123 + 345)       # Output: 468
print(363_456_789)     # Large integer with underscores for readability
```

### Float

- Numbers with decimal points.

```python
print(3.14159)
```

### Boolean

- Logical values: `True` or `False` (uppercase T/F).

```python
print(True)
print(False)
```

---

## ⚠️ Errors

- **TypeError** → Occurs when a function doesn’t work with the given data type.  
    Example: `len(123)` ❌ (cannot find length of an integer).
- `type()` → Check the data type.

```python
print(type("Hello"))   # Output: <class 'str'>
```

---

## ➗ Mathematical Operations

```python
print(300 + 63)   # Addition
print(400 - 27)   # Subtraction
print(23 * 56)    # Multiplication
print(9 / 3)      # Division → always float
print(12 // 3)    # Floor division → removes decimal
```

### Notes

- Division `/` → always returns float (implicit typecasting).
- Use `//` → integer division (floor).
- **PEMDAS** order of operations:
    - Parentheses → Exponents → Multiplication/Division → Addition/Subtraction.
    - Multiplication & Division have equal priority → evaluated **left to right**.

---

## 🔢 Number Manipulation

- `round(number, 2)` → Round to 2 decimal places.
- `int()` → Floors (truncates) the number.

---

## 📝 Assignment Operators

```python
score = 0
score += 1   # Increment
score -= 1   # Decrement
score *= 1   # Multiply
score /= 1   # Divide
print(score)
```

---

## 🎯 F-Strings

- Allow mixing of different data types inside strings.
- Syntax: `print(f"Text {variable}")`

### Example

```python
score = 0
height = 1.8
is_winning = True

print(f"Your Score is : {score} \nYour Height is : {height} \nAre You Winning? : {is_winning}")
```

---

---

# 🐍 Python Notes – Control Flow & Logical Operators

## 🔀 Control Flow with `if/else`

- Control flow decides **what code runs depending on conditions**.
- Syntax:

```python
if condition:
    # do this
else:
    # do this
```

⚠️ Rules:

- `if` and `else` must be paired.
- Indentation is critical → misaligned blocks cause **IndentationError**.
- Always include a colon `:` after `if`, `elif`, and `else`.

### Example

```python
print("Welcome to the Roller-Coaster :")
height = int(input("Please Enter Your Height in Cms :"))

if height >= 120:
    print("Here is your ticket, Enjoy the Ride ")
else:
    print("Sorry you have to grow taller before you can ride")
```

---

## 🔎 Comparison Operators

- `>` Greater than
- `<` Less than
- `>=` Greater than or equal to
- `<=` Less than or equal to
- `==` Equal to
- `!=` Not equal to

⚠️ **Note**:

- `=` → assignment
- `==` → equality check
- Using `=` in place of `==` causes **Invalid Syntax error**.

---

## ➗ Modulo Operator

- `%` → Finds the remainder of division.

```python
expression = 10 % 3
print(expression)   # Output: 1
```

### Odd/Even Check

```python
OE_Number = int(input("Enter the Number: "))
if OE_Number % 2 == 0:
    print("You have entered an Even Number.")
else:
    print("You have entered an Odd Number.")
```

---

## 🧩 Nested `if` Statements

```python
print("Welcome to the Roller-Coaster :")
height = int(input("Please Enter Your Height in Cms :"))
age = int(input("Please Enter Your Age In Years:"))

if height >= 120:
    print("Here is your ticket, Enjoy the Ride ")
    if age >= 18:
        print("Please Pay ₹800")
    else:
        print("Please Pay ₹350")
else:
    print("Sorry you have to grow taller before you can ride")
```

---

## 🔄 `elif` Statements

- Used for **multiple conditions**.

```python
if condition1:
    # do A
elif condition2:
    # do B
else:
    # do this
```

### Example

```python
height = int(input("Please Enter Your Height in Cms :"))
age = int(input("Please Enter Your Age In Years:"))

if height >= 120:
    print("Here is your ticket, Enjoy the Ride ")
    if age >= 18:
        print("Please Pay ₹950")
    elif age < 18 and age >= 12:   # using AND operator
        print("Please Pay ₹550")
    else:
        print("Please Pay ₹350")
else:
    print("Sorry you have to grow taller before you can ride")
```

---

## 📚 Multiple `if` Statements in Succession

```python
bill = 0
if height >= 120:
    print("Here is your ticket, Enjoy the Ride ")
    if age >= 18:
        bill = 950
        print("Adult Tickets are ₹950")
    elif age < 18 and age >= 12:
        bill = 550
        print("Youth Tickets are ₹550")
    else:
        bill = 350
        print("Child Tickets are ₹350")

    wants_photo = input("Do you want a Photo? Type Y/N: ")
    if wants_photo == "Y":
        bill += 120   # short form of bill = bill + 120

    print(f"Please Pay: ₹{bill}")
else:
    print("Sorry you have to grow taller before you can ride")
```

---

## ⚙️ Logical Operators

- `A and B` → **AND** operator → Both must be True.
- `C or D` → **OR** operator → At least one must be True.
- `not E` → **NOT** operator → Inverts the truth value.

💡 Use the Python console to quickly test logical expressions.

---


---

# 🐍 Python Notes – Randomisation & Lists

## 🎲 Random Module

- Python uses the **Mersenne Twister** algorithm for random number generation.
- Must **import `random`** before use.

### Examples

```python
import random

# Random integer between 1 and 10
random_integer = random.randint(1, 10)
print(random_integer)

# Random float between 0 and 1, scaled up
random_float = random.random() * 10
print(random_float)

# Random float between 1 and 10
random_floatone = random.uniform(1, 10)
print(random_floatone)
```

💡 Recommended: use `random.random()` for simplicity.

---

## 🧱 Modules

- Modules are like **bricks in a house** → reusable building blocks.
- To create your own module:
    - Save Python code in a file (e.g., `my_module.py`).
    - Import it with:

```python
import my_module
my_module.function_name()
```

---

## 📑 Python Lists

- Lists are **ordered collections** of items.

```python
states_of_india = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa"]
print(states_of_india[0])   # Output: Andhra Pradesh
```

### Indexing

- Positive index → starts from 0.
- Negative index → counts from the end (`-1` is last item).

```python
print(states_of_india[-1])   # Output: Goa
```

### Modifying Lists

```python
states_of_india[0] = "Andhra Pradesh (AP)"   # Modify item
```

### Adding Items

```python
states_of_india.append("Karnataka")          # Add single item
states_of_india.extend(["Kerala", "Tamil Nadu"])  # Add multiple items
```

### Length of List

```python
print(len(states_of_india))  # Number of items in list
print(len(states_of_india) - 1) # When indexing list with len  
```

---

## 🎲 Random Item from List

```python
random_choice = random.choice(states_of_india)
print(random_choice)
```

---

## ⚠️ Index Errors

- **IndexError** occurs when trying to access an index outside the list range.

```python
print(states_of_india[100])   # ❌ IndexError
```

---

## 🗂️ Nested Lists

- Lists can contain other lists.

```python
nested_list = [states_of_india, ["Delhi", "Mumbai", "Chennai"]]
print(nested_list[1][0])   # Output: Delhi
```

---

# 🐍 Python Notes – Loops

## 🔁 For Loop with Lists

```python
fruits = ["Apple", "Peach", "Orange", "Pear"]
for fruit in fruits:
    print(fruit)
```

- Executes the same line of code multiple times.
- Iterates through each item in the list.

---

## 📊 Summing Values

```python
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

# Using built-in sum()
total_exam_score = sum(student_scores)
print(total_exam_score)

# Manual accumulation
sum_scores = 0
for score in student_scores:
    sum_scores += score
print(sum_scores)
```

---

## 🔢 For Loops with `range()`

```python
total = 0
for number in range(1, 101):
    total += number
print(total)

# Alternative
print(sum(range(1, 101)))
```

- `+=` → accumulator operator.
- `range()` generates numbers.

---

## 🧭 Two Types of Loops

### Type A: The **Inspector** (Iterate Source)

- Use when you want to check every item in a list.

```python
for fruit in fruits:
    print(fruit)
```

- Runs once for every item.
- **Analogy**: Security guard checking every bag.

### Type B: The **Counter** (Iterate Count)

- Use when you want to perform an action X times.

```python
for _ in range(10):
    print("Pushup")
```

- Runs exactly 10 times.
- **Analogy**: Doing 10 pushups.

---

## 🔢 The `range()` Function

- Think of `range()` as a **number generator**.
- Rule: **Start is IN, Stop is OUT**.

Examples:

```python
range(4)        # 0, 1, 2, 3
range(1, 5)     # 1, 2, 3, 4
range(0, 10, 2) # 0, 2, 4, 6, 8
```

---

## 🏷️ Loop Variable

- Temporary "nametag" for the current item/number.
- Reassigned at each iteration.

```python
for i in range(3):
    print(i)
# Step 1: i = 0
# Step 2: i = 1
# Step 3: i = 2
```

- Does not remember the past → only knows the **current step**.

---

## ⚠️ The Scope Trap

- **Error**: Defining a list inside the loop.

```python
for i in range(5):
    my_list = []   # ❌ new list created each time
    my_list.append(i)
```

- Result: Old list discarded each iteration.

✅ **Fix**: Define list outside the loop.

```python
my_list = []
for i in range(5):
    my_list.append(i)
print(my_list)   # [0, 1, 2, 3, 4]
```

---
