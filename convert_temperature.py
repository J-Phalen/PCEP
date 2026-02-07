# ### Task 1.2: Create convert_temperature() function
# Write a function using the math module.

# **Requirements:**
# - Import the `math` module
# - Function name: `convert_temperature(celsius)`
# - Convert Celsius to Fahrenheit using formula: `F = C * 9/5 + 32`
# - Use `math.floor()` to return integer result
# - Include docstring

# **Learn About:**
# - Importing modules: `import math`
# - Using module functions: `math.floor(value)`
# - The `dir(math)` function to see available functions
# - The `help(math.floor)` function for documentation

# ---

import math


def convert_temperature(celsius):
    """Convert Celsius to Fahrenheit and return a floored integer value.
    Args:
        celsius (float): Temperature in degrees Celsius
    Returns:
        int: Temperature in degrees Fahrenheit (floored by math)
    """

    try:
        celsius = float(celsius)
    except (TypeError, ValueError):
        raise ValueError("Temperature input must in digits")

    fahrenheit = (celsius * (9 / 5)) + 32  # Yes I know (()) not needed but it helps show ooo.
    return math.floor(fahrenheit)  # round down to nearest whole number aka drop the decimal place


try:
    print(convert_temperature(0))  # 32
    print(convert_temperature(25))  # 77
    print(convert_temperature(36.6))  # 97
except ValueError as e:
    print(f"ValueError: {e}")
