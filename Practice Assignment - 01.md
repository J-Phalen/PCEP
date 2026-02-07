# Day 2 - PCAP Preparation Assignment
## Functions, Exceptions & File I/O Operations

**Estimated Time:** 120-180 minutes  
**PCAP Exam Coverage:** Sections 1, 2, 5 (48% of exam)  
**Environment:** VSCode with Python 3.x

---

## 📚 Learning Objectives

By completing this assignment, you will master:
- User-defined functions with parameters and return values
- Exception handling using try-except-else-finally blocks
- The Python exception hierarchy (BaseException → Exception → specific types)
- Custom exception classes and raising exceptions
- Standard library modules (math, platform, datetime)
- File I/O operations in text and binary modes
- Context managers using the `with` statement
- File methods: read(), write(), readline(), readlines()

---

## 📖 Required Reading & Resources

### Before You Start:
1. **Python Documentation - Functions:**
   - https://docs.python.org/3/tutorial/controlflow.html#defining-functions
   - Focus on: parameters, return values, docstrings, default arguments

2. **Python Documentation - Exceptions:**
   - https://docs.python.org/3/tutorial/errors.html
   - Study: exception hierarchy, try-except-else-finally, raising exceptions

3. **Python Documentation - File I/O:**
   - https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
   - Learn: open() function, file modes, context managers (with statement)

4. **Standard Library Modules:**
   - math module: https://docs.python.org/3/library/math.html
   - platform module: https://docs.python.org/3/library/platform.html

### Key PCAP Concepts to Review:
- Function definition syntax: `def function_name(parameters):`
- Return statement and returning multiple values with tuples
- Exception handling flow: try → except → else → finally
- Built-in exceptions: ValueError, TypeError, ZeroDivisionError, FileNotFoundError
- File modes: 'r' (read), 'w' (write), 'a' (append), 'rb'/'wb' (binary)
- The difference between text and binary file modes
- Name mangling for custom exceptions

---

## 🎯 Assignment Structure

Create a Python project with the following files:
```
day2_assignment/
├── payroll.py          # Main payroll calculator (Part 1-4)
├── file_manager.py     # File I/O operations (Part 5-7)
├── test_functions.py   # Test your implementations
└── data/
    └── payroll_data.txt
```

---

## Part 1: User-Defined Functions

**File:** `payroll.py`

### Task 1.1: Create calculate_pay() function
Write a function that calculates weekly pay with overtime rules.

**Requirements:**
- Function name: `calculate_pay(hours, rate)`
- Parameters: `hours` (float), `rate` (float)
- Return: total pay as float
- Logic: 
  - Regular pay for hours ≤ 40
  - Overtime at 1.5x rate for hours > 40
- Raise `ValueError` if hours or rate is negative
- Include a docstring describing the function

**Hints:**
```python
def calculate_pay(hours, rate):
    """Calculate weekly pay with overtime (1.5x for hours > 40)
    
    Args:
        hours (float): Hours worked
        rate (float): Hourly pay rate
    
    Returns:
        float: Total weekly pay
        
    Raises:
        ValueError: If hours or rate is negative
    """
    # Your implementation here
```

**Test Cases:**
- `calculate_pay(35, 20)` should return `700.0`
- `calculate_pay(45, 20)` should return `950.0` (40*20 + 5*30)
- `calculate_pay(-5, 20)` should raise `ValueError`

---

### Task 1.2: Create convert_temperature() function
Write a function using the math module.

**Requirements:**
- Import the `math` module
- Function name: `convert_temperature(celsius)`
- Convert Celsius to Fahrenheit using formula: `F = C * 9/5 + 32`
- Use `math.floor()` to return integer result
- Include docstring

**Learn About:**
- Importing modules: `import math`
- Using module functions: `math.floor(value)`
- The `dir(math)` function to see available functions
- The `help(math.floor)` function for documentation

---

### Task 1.3: Create print_system_info() function
Use the platform module to display system information.

**Requirements:**
- Import the `platform` module
- Print: `platform.system()`, `platform.python_version()`, `platform.machine()`
- Format output nicely with labels

**Example Output:**
```
System: Windows
Python Version: 3.11.0
Machine: AMD64
```

---

## Part 2: Exception Handling Fundamentals

**File:** `payroll.py` (continue)

### Task 2.1: Implement safe_divide() function
Create a function with comprehensive exception handling.

**Requirements:**
- Function name: `safe_divide(a, b)`
- Use try-except-else-finally structure
- Handle `ZeroDivisionError` - print error message, return None
- Handle `TypeError` - print error message, return None
- Use `else` block to print success message when division succeeds
- Use `finally` block to print "Division attempt complete"
- Return result or None

**Key Learning Points:**
- The try block contains code that might raise exceptions
- Multiple except blocks catch different exception types
- The else block runs ONLY if no exception occurred
- The finally block ALWAYS runs (even if exception or return)

**Test Cases:**
```python
safe_divide(10, 2)    # Should succeed, print success, return 5.0
safe_divide(10, 0)    # Should catch ZeroDivisionError, return None
safe_divide(10, 'a')  # Should catch TypeError, return None
```

---

### Task 2.2: Understanding Exception Hierarchy
Study the built-in exception hierarchy:

```
BaseException
└── Exception
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   ├── OverflowError
    │   └── FloatingPointError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── TypeError
    ├── ValueError
    ├── OSError
    │   └── FileNotFoundError
    └── ... (many more)
```

**Important:** 
- Always catch specific exceptions, not broad `Exception`
- More specific exceptions should be caught before general ones
- You can catch multiple exceptions: `except (ValueError, TypeError):`

---

## Part 3: Custom Exceptions

**File:** `payroll.py` (continue)

### Task 3.1: Define custom exception class
Create a custom exception for negative values.

**Requirements:**
```python
class NegativeValueError(Exception):
    """Raised when a negative value is provided where positive is expected"""
    pass
```

**Key Concepts:**
- Custom exceptions inherit from `Exception`
- Use `pass` for simple exceptions that don't need additional logic
- Custom exceptions improve code readability and error handling

---

### Task 3.2: Create get_positive_number() function
Implement input validation with custom exceptions.

**Requirements:**
- Function name: `get_positive_number(prompt)`
- Get input from user with `input(prompt)`
- Convert to float
- Raise `NegativeValueError` if number < 0
- Raise `ValueError` if conversion fails
- Return the valid positive number

**Hints:**
```python
def get_positive_number(prompt):
    """Get a positive number from user input
    
    Args:
        prompt (str): Message to display to user
    
    Returns:
        float: Positive number from user
        
    Raises:
        NegativeValueError: If number is negative
        ValueError: If input is not a valid number
    """
    user_input = input(prompt)
    # Convert to float (may raise ValueError)
    # Check if negative (raise NegativeValueError if so)
    # Return valid number
```

---

### Task 3.3: Create main payroll function
Combine everything with proper exception handling.

**Requirements:**
- Function name: `run_payroll_calculator()`
- Use try-except to catch all exceptions
- Call `get_positive_number()` for hours and rate
- Call `calculate_pay()` with the values
- Print formatted result
- Handle `NegativeValueError` and `ValueError` separately

---

## Part 4: Working with Standard Library Modules

**File:** `payroll.py` (continue)

### Task 4.1: Add timestamp functionality
Import and use the datetime module.

**Requirements:**
- Import datetime: `from datetime import datetime`
- Create function `get_timestamp()` that returns current date/time as string
- Format: "YYYY-MM-DD HH:MM:SS"
- Use `datetime.now().strftime("%Y-%m-%d %H:%M:%S")`

**Learn About:**
- The datetime module and datetime class
- The `.now()` method to get current time
- The `.strftime()` method for formatting dates
- Date format codes: %Y (year), %m (month), %d (day), %H (hour), %M (minute), %S (second)

---

## Part 5: Text File Operations

**File:** `file_manager.py`

### Task 5.1: Write data to file with context manager
Create a function that saves payroll data to a text file.

**Requirements:**
- Function name: `save_payroll_data(name, hours, rate, total_pay, filename)`
- Use `with open(filename, 'w') as file:` to open file in write mode
- Write multiple lines with employee information
- Include timestamp using `get_timestamp()` from Part 4
- File closes automatically when with block ends

**Key Concepts:**
- Context manager (`with` statement) ensures file is properly closed
- Write mode 'w' creates new file or overwrites existing
- Use `file.write(string)` to write text
- Remember to add newline characters `\n`

**Example File Content:**
```
Employee: John Doe
Hours: 45.0
Rate: $25.50
Total Pay: $1168.75
Generated: 2024-02-07 14:30:00
```

**Hints:**
```python
def save_payroll_data(name, hours, rate, total_pay, filename):
    """Save payroll information to text file
    
    Args:
        name (str): Employee name
        hours (float): Hours worked
        rate (float): Hourly rate
        total_pay (float): Total calculated pay
        filename (str): Output filename
    """
    with open(filename, 'w') as file:
        # Write each line of information
        # Use f-strings for formatting: f"Employee: {name}\n"
```

---

### Task 5.2: Append data to existing file
Create function that adds new entries without overwriting.

**Requirements:**
- Function name: `append_payroll_entry(name, hours, rate, total_pay, filename)`
- Use append mode: `'a'`
- Add a separator line between entries: `"\n" + "="*50 + "\n"`
- Include timestamp

**File Modes Summary:**
- `'r'` - Read (default) - file must exist
- `'w'` - Write - creates new or overwrites existing
- `'a'` - Append - creates new or adds to end of existing
- `'r+'` - Read and write
- `'rb'`, `'wb'`, `'ab'` - Binary modes

---

### Task 5.3: Read entire file
Create function to read and display file contents.

**Requirements:**
- Function name: `read_payroll_file(filename)`
- Use context manager with read mode `'r'`
- Use `.read()` method to get entire file as string
- Print the contents
- Handle `FileNotFoundError` exception

**Hints:**
```python
def read_payroll_file(filename):
    """Read and display entire payroll file"""
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
```

---

### Task 5.4: Read file line by line
Create function to process file lines individually.

**Requirements:**
- Function name: `process_payroll_lines(filename)`
- Use `.readlines()` to get list of lines
- Iterate through lines with enumerate to show line numbers
- Strip whitespace from each line using `.strip()`
- Handle `FileNotFoundError`

**Learn About:**
- `.readlines()` returns list of lines (includes \n)
- `.readline()` reads one line at a time
- Iterating directly over file object: `for line in file:`
- String method `.strip()` removes leading/trailing whitespace

---

## Part 6: Binary File Operations

**File:** `file_manager.py` (continue)

### Task 6.1: Write binary data
Create function to save data in binary format.

**Requirements:**
- Function name: `save_binary_data(data_list, filename)`
- Parameter `data_list` is a list of integers (0-255)
- Convert list to bytearray: `bytearray(data_list)`
- Open file in binary write mode: `'wb'`
- Write bytearray to file

**Key Concepts:**
- Binary mode works with bytes, not strings
- bytearray is a mutable sequence of bytes
- Each byte represents a number from 0-255
- Binary files don't have line endings or encoding

**Hints:**
```python
def save_binary_data(data_list, filename):
    """Save integer list as binary data
    
    Args:
        data_list (list): List of integers (0-255)
        filename (str): Output filename
    """
    with open(filename, 'wb') as file:
        data = bytearray(data_list)
        file.write(data)
```

---

### Task 6.2: Read binary data
Create function to read binary file.

**Requirements:**
- Function name: `read_binary_data(filename)`
- Open in binary read mode: `'rb'`
- Read all bytes using `.read()`
- Return as bytearray
- Print both the bytes and decoded text

**Test Example:**
```python
# ASCII codes for "Hello"
test_data = [72, 101, 108, 108, 111]
save_binary_data(test_data, 'test.bin')
result = read_binary_data('test.bin')
print(f"Binary: {list(result)}")
print(f"Text: {result.decode('utf-8')}")
```

---

## Part 7: Complete Integration

**File:** `test_functions.py`

### Task 7.1: Create comprehensive test program
Build a complete application using all concepts.

**Requirements:**
1. Import all your functions from payroll.py and file_manager.py
2. Create a menu system with options:
   - Calculate new payroll
   - View payroll history
   - Exit
3. Use exception handling throughout
4. Save all calculations to files
5. Display results formatted nicely

**Program Flow:**
```
=== Payroll Management System ===
1. Calculate Employee Pay
2. View Payroll History
3. Exit

Enter choice: 1

Enter employee name: Alice Smith
Enter hours worked: 45
Enter hourly rate: 28.50

Calculating pay...
Regular hours: 40 @ $28.50 = $1140.00
Overtime hours: 5 @ $42.75 = $213.75
Total pay: $1353.75

Data saved to payroll_data.txt
```

---

## 🧪 Testing Your Code

Create test cases for each function:

```python
def test_calculate_pay():
    """Test the calculate_pay function"""
    assert calculate_pay(40, 20) == 800.0
    assert calculate_pay(45, 20) == 950.0
    try:
        calculate_pay(-5, 20)
        assert False, "Should raise ValueError"
    except ValueError:
        pass
    print("✓ calculate_pay tests passed")

def test_safe_divide():
    """Test the safe_divide function"""
    assert safe_divide(10, 2) == 5.0
    assert safe_divide(10, 0) is None
    assert safe_divide(10, 'a') is None
    print("✓ safe_divide tests passed")

# Add more test functions for other features
```

---

## 📊 Grading Criteria

| Component | Points | Description |
|-----------|--------|-------------|
| Functions (Part 1) | 15 | Correct implementation with proper parameters and return values |
| Exception Handling (Part 2-3) | 20 | Proper use of try-except-else-finally and custom exceptions |
| Standard Library (Part 4) | 10 | Correct use of math, platform, datetime modules |
| Text File I/O (Part 5) | 20 | Context managers, read/write operations, file modes |
| Binary Files (Part 6) | 15 | Binary mode operations with bytearray |
| Integration (Part 7) | 15 | Complete working program with all features |
| Code Quality | 5 | Docstrings, comments, PEP 8 style, testing |
| **Total** | **100** | |

---

## 💡 Tips for Success

1. **Read the documentation** - The official Python docs are your best resource
2. **Test frequently** - Run your code after each function to catch errors early
3. **Use print statements** - Debug by printing variable values
4. **Handle exceptions properly** - Don't use bare `except:` clauses
5. **Follow PEP 8** - Use consistent naming and formatting
6. **Write docstrings** - Document what each function does
7. **Use type hints** - Optional but helpful: `def calculate_pay(hours: float, rate: float) -> float:`

---

## 🎓 PCAP Exam Connection

This assignment covers these PCAP exam sections:

**Section 1: Modules and Packages (12%)**
- Importing modules
- Using standard library modules
- The `dir()` and `help()` functions

**Section 2: Exceptions (14%)**
- Exception hierarchy
- try-except-else-finally blocks
- Raising exceptions
- Custom exception classes

**Section 5: File I/O Operations (22%)**
- open() function and file modes
- Reading and writing files
- Context managers (with statement)
- Text vs binary modes
- File methods

**Total Coverage: 48% of PCAP exam**

---

## 📚 Additional Resources

- Python Tutorial: https://docs.python.org/3/tutorial/
- Real Python - File I/O: https://realpython.com/read-write-files-python/
- Real Python - Exceptions: https://realpython.com/python-exceptions/
- PEP 8 Style Guide: https://pep8.org/
- Python Module Index: https://docs.python.org/3/py-modindex.html

---

## ✅ Submission Checklist

- [ ] All Python files are properly formatted and commented
- [ ] All functions have docstrings
- [ ] All test cases pass
- [ ] Exception handling is implemented correctly
- [ ] File I/O operations use context managers
- [ ] Code follows PEP 8 style guidelines
- [ ] Test file demonstrates all functionality
- [ ] No syntax errors or runtime crashes

---

**Good luck! Remember: The PCAP exam tests practical programming skills, so focus on understanding WHY things work, not just memorizing syntax.**
