# PCAP Practice Exam Questions
## Based on Day 2 & Day 3 Assignments

**Format:** Single-choice and multiple-choice questions  
**Time Limit:** 30 minutes (similar to 40 questions in 65 minutes on real exam)  
**Passing Score:** 14/20 (70%)  
**Instructions:** Select the best answer for each question. Some questions may have multiple correct answers.

---

## Section 1: Functions and Modules (Questions 1-4)

### Question 1
What will be the output of the following code?

```python
def calculate(x, y=10):
    return x + y

print(calculate(5))
```

A) `5`  
B) `10`  
C) `15`  
D) `TypeError` (missing required argument)

<details>
<summary>Click to reveal answer</summary>

**Answer: C) `15`**

**Explanation:** The function has a default parameter `y=10`. When called with only one argument `calculate(5)`, `x` becomes `5` and `y` uses the default value `10`. The result is `5 + 10 = 15`. This tests understanding of default parameter values, which is a key PCAP concept.
</details>

---

### Question 2
Which statement about the `math` module is TRUE?

A) `math.floor(5.9)` returns `6`  
B) `math.ceil(5.1)` returns `6`  
C) You must use `from math import *` to access `math.floor()`  
D) `math.floor()` and `int()` always produce the same result

<details>
<summary>Click to reveal answer</summary>

**Answer: B) `math.ceil(5.1)` returns `6`**

**Explanation:** 
- `math.floor(5.9)` returns `5` (rounds down), not `6` - so A is FALSE
- `math.ceil(5.1)` returns `6` (rounds up) - B is TRUE ✓
- You can use `import math` and access with `math.floor()` - C is FALSE
- They differ for negative numbers: `int(-5.5)` = `-5`, but `math.floor(-5.5)` = `-6` - so D is FALSE

This tests knowledge of standard library modules and their functions.
</details>

---

### Question 3
What is the result of the following code?

```python
def func(a, b, c):
    return a, b, c

result = func(1, 2, 3)
print(type(result))
```

A) `<class 'list'>`  
B) `<class 'tuple'>`  
C) `<class 'dict'>`  
D) `<class 'set'>`

<details>
<summary>Click to reveal answer</summary>

**Answer: B) `<class 'tuple'>`**

**Explanation:** When a function returns multiple values separated by commas (`return a, b, c`), Python automatically packs them into a tuple. This is called "tuple packing" and is a fundamental concept for PCAP. The result is `(1, 2, 3)` which is a tuple type.
</details>

---

### Question 4
Which code correctly imports and uses the `platform` module to get the Python version?

A) `import platform; print(platform.version())`  
B) `from platform import *; print(python_version())`  
C) `import platform; print(platform.python_version())`  
D) `from platform import version; print(version())`

<details>
<summary>Click to reveal answer</summary>

**Answer: C) `import platform; print(platform.python_version())`**

**Explanation:** The correct function in the platform module is `python_version()`, not `version()`. Option C properly imports the module and calls the function. Options A and D use the wrong function name, and while option B would work, using `import *` is discouraged as it pollutes the namespace. This tests module import syntax and standard library knowledge.
</details>

---

## Section 2: Exception Handling (Questions 5-8)

### Question 5
What is the correct order of execution for exception handling blocks?

A) `try` → `except` → `finally` → `else`  
B) `try` → `except` → `else` → `finally`  
C) `try` → `else` → `except` → `finally`  
D) `try` → `finally` → `except` → `else`

<details>
<summary>Click to reveal answer</summary>

**Answer: B) `try` → `except` → `else` → `finally`**

**Explanation:** The correct execution order is:
1. `try` block executes first
2. If exception occurs, `except` block runs
3. If NO exception occurs, `else` block runs (optional)
4. `finally` block ALWAYS runs last, regardless of exceptions

This is a critical PCAP concept about exception handling flow control.
</details>

---

### Question 6
Given the exception hierarchy, which `except` clause should come FIRST?

```python
try:
    # some code
except ________:  # Which should be first?
```

A) `Exception`  
B) `ZeroDivisionError`  
C) `ArithmeticError`  
D) Order doesn't matter

<details>
<summary>Click to reveal answer</summary>

**Answer: B) `ZeroDivisionError`**

**Explanation:** In exception handling, more specific exceptions should be caught BEFORE more general ones. The hierarchy is:
- `Exception` (most general)
- `ArithmeticError` (more specific)  
- `ZeroDivisionError` (most specific)

If you put `Exception` first, it would catch everything and the more specific handlers would never execute. This tests understanding of exception hierarchy, a key PCAP topic.
</details>

---

### Question 7
What happens when you `raise ValueError("Invalid input")` inside a `try` block?

A) The program crashes immediately  
B) The `except ValueError` block executes if present  
C) The `else` block executes  
D) The exception is ignored if no `except` clause exists

<details>
<summary>Click to reveal answer</summary>

**Answer: B) The `except ValueError` block executes if present**

**Explanation:** When you raise an exception inside a `try` block, Python looks for a matching `except` clause. If found, that block executes. If not found, the exception propagates up the call stack. The `else` block only runs when NO exception occurs. This tests the mechanics of raising and catching exceptions.
</details>

---

### Question 8
Which statement about custom exceptions is TRUE?

```python
class NegativeValueError(Exception):
    pass
```

A) Custom exceptions must inherit from `BaseException`  
B) Custom exceptions should inherit from `Exception`  
C) You cannot raise custom exceptions  
D) The `pass` keyword is not allowed in exception classes

<details>
<summary>Click to reveal answer</summary>

**Answer: B) Custom exceptions should inherit from `Exception`**

**Explanation:** While custom exceptions CAN inherit from `BaseException`, they SHOULD inherit from `Exception` (which itself inherits from `BaseException`). This is best practice because `BaseException` is meant for system-exiting exceptions like `KeyboardInterrupt`. The `pass` statement is perfectly valid for empty class bodies. This tests understanding of exception hierarchy and custom exception creation.
</details>

---

## Section 3: File I/O Operations (Questions 9-11)

### Question 9
What is the advantage of using the `with` statement when working with files?

```python
with open('file.txt', 'r') as f:
    data = f.read()
```

A) Files are automatically closed even if an error occurs  
B) Files can be read faster  
C) Multiple files cannot be opened at the same time  
D) The `with` statement is required for all file operations

<details>
<summary>Click to reveal answer</summary>

**Answer: A) Files are automatically closed even if an error occurs**

**Explanation:** The `with` statement implements context management, which guarantees that the file will be properly closed when the block exits, even if an exception occurs. This prevents resource leaks. The `with` statement doesn't make files read faster (B), allows multiple files to be opened (C is false), and is not required but is best practice (D is false). This tests understanding of context managers, a critical PCAP concept.
</details>

---

### Question 10
Which file mode should you use to add data to the END of an existing file without erasing its contents?

A) `'r'` (read)  
B) `'w'` (write)  
C) `'a'` (append)  
D) `'r+'` (read and write)

<details>
<summary>Click to reveal answer</summary>

**Answer: C) `'a'` (append)**

**Explanation:** 
- `'r'` opens for reading only (cannot write)
- `'w'` opens for writing but ERASES existing content
- `'a'` opens for writing and appends to the END without erasing ✓
- `'r+'` opens for both reading and writing but doesn't automatically move to end

This tests knowledge of file modes, which is frequently tested on PCAP.
</details>

---

### Question 11
What is the difference between these two file operations?

```python
# Option 1
with open('data.bin', 'wb') as f:
    f.write(b'Hello')

# Option 2
with open('data.txt', 'w') as f:
    f.write('Hello')
```

A) There is no difference  
B) Option 1 writes in binary mode, Option 2 writes in text mode  
C) Option 1 will cause an error  
D) Option 2 will cause an error

<details>
<summary>Click to reveal answer</summary>

**Answer: B) Option 1 writes in binary mode, Option 2 writes in text mode**

**Explanation:** 
- `'wb'` opens file in binary write mode, requires bytes object (hence `b'Hello'`)
- `'w'` opens file in text write mode, requires string object
- Binary mode writes raw bytes; text mode handles encoding/decoding automatically
- Both options are syntactically correct for their respective modes

This tests understanding of binary vs text file modes, a key PCAP topic.
</details>

---

## Section 4: Object-Oriented Programming (Questions 12-17)

### Question 12
What is the output of this code?

```python
class Counter:
    count = 0
    
    def __init__(self):
        Counter.count += 1

c1 = Counter()
c2 = Counter()
print(Counter.count)
```

A) `0`  
B) `1`  
C) `2`  
D) `AttributeError`

<details>
<summary>Click to reveal answer</summary>

**Answer: C) `2`**

**Explanation:** `count` is a class variable (defined in class body, not in `__init__`). It is shared by ALL instances of the class. Each time a new Counter object is created, `__init__` increments the class variable. After creating `c1` and `c2`, the count is `2`. This tests understanding of class vs instance variables, which is crucial for PCAP (34% of exam is OOP).
</details>

---

### Question 13
Which statement about the `self` parameter is TRUE?

A) `self` is a Python keyword  
B) You can name it anything, but `self` is conventional  
C) `self` is automatically passed when calling instance methods  
D) Both B and C are correct

<details>
<summary>Click to reveal answer</summary>

**Answer: D) Both B and C are correct**

**Explanation:** 
- `self` is NOT a keyword in Python (you could use `this` or `me`), but `self` is the strong convention
- When you call `obj.method()`, Python automatically passes `obj` as the first argument
- Both B and C are true statements

This tests fundamental understanding of Python's object system.
</details>

---

### Question 14
What does "name mangling" do in Python?

```python
class Example:
    def __init__(self):
        self.__private = 42
```

A) Makes the attribute completely inaccessible  
B) Renames it to `_Example__private`  
C) Raises an error if you try to access it  
D) Converts it to a class variable

<details>
<summary>Click to reveal answer</summary>

**Answer: B) Renames it to `_Example__private`**

**Explanation:** Name mangling occurs when an attribute starts with double underscore (but doesn't end with it). Python renames it by prepending `_ClassName` to prevent accidental overriding in subclasses. The attribute is still accessible as `obj._Example__private`, but this is discouraged. It's NOT truly private (A is false), doesn't raise errors (C is false), and remains an instance variable (D is false). This tests understanding of encapsulation in Python.
</details>

---

### Question 15
What is the output?

```python
class Parent:
    def greet(self):
        return "Hello from Parent"

class Child(Parent):
    def greet(self):
        return "Hello from Child"

obj = Child()
print(obj.greet())
```

A) `Hello from Parent`  
B) `Hello from Child`  
C) `TypeError`  
D) Both greetings are printed

<details>
<summary>Click to reveal answer</summary>

**Answer: B) `Hello from Child`**

**Explanation:** This demonstrates method overriding. The `Child` class overrides the `greet()` method from the `Parent` class. When calling `obj.greet()`, Python looks for the method in the most specific class first (Child), finds it, and executes it. To call the parent's method, you would need to use `super().greet()`. This tests inheritance and method overriding, core OOP concepts.
</details>

---

### Question 16
What does the `super()` function do?

```python
class Child(Parent):
    def __init__(self, name):
        super().__init__(name)
```

A) Creates a new parent object  
B) Calls the parent class's method  
C) Returns the parent class  
D) Prevents method overriding

<details>
<summary>Click to reveal answer</summary>

**Answer: B) Calls the parent class's method**

**Explanation:** `super()` returns a proxy object that allows you to call methods from the parent class. In this example, `super().__init__(name)` calls the parent's `__init__` method. This is essential when you override a method but still want to execute the parent's version. It doesn't create a new object (A), doesn't return the class itself (C), and has nothing to do with preventing overriding (D). This tests understanding of inheritance mechanics.
</details>

---

### Question 17
Which statement about the `__str__` method is TRUE?

```python
class Student:
    def __str__(self):
        return "Student object"
```

A) `__str__` is called by `print()` and `str()`  
B) `__str__` must always return a string  
C) `__str__` is a special method (magic method)  
D) All of the above

<details>
<summary>Click to reveal answer</summary>

**Answer: D) All of the above**

**Explanation:** 
- `__str__` is called automatically when you use `print(obj)` or `str(obj)` ✓
- `__str__` MUST return a string object (raises TypeError otherwise) ✓
- Methods with double underscores are called "special methods" or "magic methods" ✓

All three statements are correct. This tests knowledge of special methods, which are important in PCAP OOP section.
</details>

---

## Section 5: Strings, Comprehensions, and Lambda (Questions 18-20)

### Question 18
What is the result?

```python
text = "  Python Programming  "
result = text.strip().upper().split()
print(len(result))
```

A) `1`  
B) `2`  
C) `3`  
D) `19`

<details>
<summary>Click to reveal answer</summary>

**Answer: B) `2`**

**Explanation:** Method chaining occurs left to right:
1. `text.strip()` → `"Python Programming"` (removes whitespace)
2. `.upper()` → `"PYTHON PROGRAMMING"`
3. `.split()` → `["PYTHON", "PROGRAMMING"]` (splits on whitespace)
4. `len(result)` → `2` (two items in list)

This tests understanding of string immutability and method chaining.
</details>

---

### Question 19
Which list comprehension correctly filters even numbers from a list?

```python
numbers = [1, 2, 3, 4, 5, 6]
```

A) `[n for n in numbers where n % 2 == 0]`  
B) `[n for n in numbers if n % 2 == 0]`  
C) `[n if n % 2 == 0 for n in numbers]`  
D) `[n in numbers for n if n % 2 == 0]`

<details>
<summary>Click to reveal answer</summary>

**Answer: B) `[n for n in numbers if n % 2 == 0]`**

**Explanation:** 
- Python uses `if` for filtering in comprehensions, not `where` (A is wrong)
- The syntax is: `[expression for item in iterable if condition]`
- Option B follows this correct syntax
- Option C has `if` in the wrong position (would need `else` to work)
- Option D has invalid syntax

This tests list comprehension syntax, a key PCAP concept.
</details>

---

### Question 20
What is the output?

```python
numbers = [1, 2, 3, 4]
result = list(map(lambda x: x * 2, numbers))
print(result)
```

A) `[1, 2, 3, 4]`  
B) `[2, 4, 6, 8]`  
C) `8`  
D) `<map object at 0x...>`

<details>
<summary>Click to reveal answer</summary>

**Answer: B) `[2, 4, 6, 8]`**

**Explanation:** 
- `map(function, iterable)` applies the function to every element
- `lambda x: x * 2` is an anonymous function that doubles its input
- `map()` returns a map object, which we convert to a list with `list()`
- Each number is doubled: `[1*2, 2*2, 3*2, 4*2]` = `[2, 4, 6, 8]`

This tests lambda functions and the map() function, both important for PCAP.
</details>

---

## Answer Key

1. C
2. B
3. B
4. C
5. B
6. B
7. B
8. B
9. A
10. C
11. B
12. C
13. D
14. B
15. B
16. B
17. D
18. B
19. B
20. B

---

## Scoring Guide

- **18-20 correct (90-100%):** Excellent! You're well-prepared for PCAP
- **14-17 correct (70-85%):** Good! Review areas you missed
- **10-13 correct (50-65%):** Fair. Need more study time
- **Below 10 (< 50%):** Review all concepts thoroughly

---

## Topics to Review Based on Your Score

### If you missed Questions 1-4:
- Review function definitions and default parameters
- Study standard library modules (math, platform)
- Practice module import syntax
- Understand function return values and tuple packing

### If you missed Questions 5-8:
- Review exception handling flow (try-except-else-finally)
- Study exception hierarchy thoroughly
- Practice creating and raising custom exceptions
- Understand when to catch specific vs general exceptions

### If you missed Questions 9-11:
- Review file modes ('r', 'w', 'a', 'rb', 'wb')
- Practice using context managers (with statement)
- Understand binary vs text file operations
- Study file methods (read, write, readline, readlines)

### If you missed Questions 12-17:
- **OOP is 34% of PCAP - spend extra time here!**
- Review class vs instance variables
- Practice inheritance and super()
- Study encapsulation and name mangling
- Understand method overriding and polymorphism
- Learn special methods (__init__, __str__, etc.)

### If you missed Questions 18-20:
- Review string methods and immutability
- Practice list comprehension syntax
- Study lambda functions
- Understand map(), filter(), and sorted()

---

## PCAP Exam Format Reminder

**Real PCAP Exam:**
- 40 questions (single and multiple choice)
- 65 minutes (plus 10 minutes for NDA/tutorial)
- 70% passing score (28/40 questions)
- Covers Python 3.x
- No access to Python interpreter during exam
- Questions test both knowledge and code prediction

**Exam Sections:**
1. Modules and Packages (12%)
2. Exceptions (14%)
3. Strings (18%)
4. Object-Oriented Programming (34%)
5. Miscellaneous (File I/O, Comprehensions, Lambdas) (22%)

---

## Study Tips for PCAP Success

1. **Practice predicting code output** - Don't just run code, think through what will happen
2. **Understand the "why"** - Know why certain approaches are better than others
3. **Master OOP concepts** - 34% of the exam focuses on this
4. **Review exception hierarchy** - Know which exceptions inherit from which
5. **Practice without an IDE** - The exam doesn't let you run code
6. **Time management** - You have about 1.5 minutes per question
7. **Read questions carefully** - Some ask what will happen, others ask what's wrong
8. **Know string immutability** - Strings cannot be modified in place
9. **Understand file modes** - Know the difference between 'r', 'w', 'a', 'rb', 'wb'
10. **Practice with official Python docs** - Get comfortable reading documentation

---

**Ready to take the real PCAP exam? Review any topics where you scored poorly, then try these questions again. Good luck!**
