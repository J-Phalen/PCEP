# ### Task 2.1: Implement safe_divide() function
# Create a function with comprehensive exception handling.

# **Requirements:**
# - Function name: `safe_divide(a, b)`
# - Use try-except-else-finally structure
# - Handle `ZeroDivisionError` - print error message, return None
# - Handle `TypeError` - print error message, return None
# - Use `else` block to print success message when division succeeds
# - Use `finally` block to print "Division attempt complete"
# - Return result or None

# **Key Learning Points:**
# - The try block contains code that might raise exceptions
# - Multiple except blocks catch different exception types
# - The else block runs ONLY if no exception occurred
# - The finally block ALWAYS runs (even if exception or return)

# **Test Cases:**
# ```python
# safe_divide(10, 2)    # Should succeed, print success, return 5.0
# safe_divide(10, 0)    # Should catch ZeroDivisionError, return None
# safe_divide(10, 'a')  # Should catch TypeError, return None
# ```


def safe_divide(a, b):
    """Safely divide two values with comprehensive exception handling.
    Args:
        a: Numerator
        b: Denominator
    Returns:
        float or None: Result of division, or None if an error occurs
    """
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except TypeError:
        print("Error: Invalid input type. Both values must be numbers.")
        return None
    else:
        print("Division successful.")
        return result
    finally:
        print("Division attempt complete.")


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

    # First we validate the input
    try:
        hours = float(hours)
        rate = float(rate)
    except TypeError, ValueError:
        raise ValueError("The input provided was not found to be a valid floating point.")

    # Next we check for negative values of the correct input type that will still break the function
    if hours < 0 or rate < 0:
        raise ValueError("Hours and Rate values cannot be negative")

    # Calculate straight pay
    straightPay = hours * rate
    if hours <= 40:
        return straightPay
    else:
        otRate = rate * 1.5
        otHours = hours - 40
        return straightPay + (otRate * otHours)


# Program Execution starts here.
try:
    pay = calculate_pay(35, 20)  # should return 700.00
    print(f"Weekly pay: {pay:.2f}")
    pay = calculate_pay(45, 20)  # should return 950.00 (40*20 + 5*30)
    print(f"Weekly pay: {pay:.2f}")
    calculate_pay(-5, 20)  # should raise ValueError
    print(f"Weekly pay: {pay:.2f}")
except ValueError as e:
    print(f"ValueError: {e}")

print("\n=== Safe Divide Tests ===")
result = safe_divide(10, 2)  # Should succeed, print success, return 5.0
print(f"Result: {result}\n")
result = safe_divide(10, 0)  # Should catch ZeroDivisionError, return None
print(f"Result: {result}\n")
result = safe_divide(10, "a")  # Should catch TypeError, return None
print(f"Result: {result}\n")  # But I would have rathered a try except and show the error, not just return None.
