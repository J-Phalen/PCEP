class NegativeValueError(Exception):
    """Raised when a negative value is provided where positive is expected"""

    pass


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
    except TypeError:
        raise TypeError("The input provided was not found to be a valid floating point.")
    except ValueError:
        raise ValueError("The input provided was not found to be a valid floating point.")
    except NegativeValueError:
        raise NegativeValueError("The input provided can not be negative.")

    # Next we check for negative values of the correct input type that will still break the function
    if hours < 0 or rate < 0:
        raise NegativeValueError("Hours and Rate values cannot be negative")

    # Calculate straight pay
    pay = hours * rate
    if hours <= 40:
        return pay
    else:
        otRate = rate * 0.5
        otHours = hours - 40
        straightPay = pay + (otRate * otHours)
        return straightPay


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
    try:
        # Convert to float (may raise ValueError)
        user_input = float(user_input)
    except ValueError:
        print("The input must be numeric")
        raise

    while user_input:
        # Check if negative (raise NegativeValueError if so)
        if user_input < 0:
            raise NegativeValueError("Some text maybe prints here saying were negative.")
        else:
            # Return valid number
            return user_input


# Program Execution starts here.
try:
    pay = calculate_pay(35, 20)  # should return 700.00
    print(f"Weekly pay: {pay:.2f}")
    pay = calculate_pay(45, 20)  # should return 950.00 (40*20 + 5*30)
    print(f"Weekly pay: {pay:.2f}")
    # calculate_pay(-5, 20)  # should raise ValueError
    # print(f"Weekly pay: {pay:.2f}")
except ValueError as e:
    print(f"ValueError: {e}")

print("\n=== Safe Divide Tests ===")
result = safe_divide(10, 2)  # Should succeed, print success, return 5.0
print(f"Result: {result}\n")
result = safe_divide(10, 0)  # Should catch ZeroDivisionError, return None
print(f"Result: {result}\n")
result = safe_divide(10, "a")  # Should catch TypeError, return None
print(f"Result: {result}\n")  # But I would have rathered a try except and show the error, not just return None.


posNumber = get_positive_number(prompt="Please input a number that should be positive:\n")
