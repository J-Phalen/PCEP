# ### Task 1.1: Create calculate_pay() function
# Write a function that calculates weekly pay with overtime rules.

# **Requirements:**
# - Function name: `calculate_pay(hours, rate)`
# - Parameters: `hours` (float), `rate` (float)
# - Return: total pay as float
# - Logic:
#   - Regular pay for hours ≤ 40
#   - Overtime at 1.5x rate for hours > 40
# - Raise `ValueError` if hours or rate is negative
# - Include a docstring describing the function


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
