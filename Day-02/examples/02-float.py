# Float variables
num1 = 5.0
num2 = 2.5

# Basic Arithmetic
result1 = num1 + num2
print("Addition:", result1)

result2 = num1 - num2
print("Subtraction:", result2)

result3 = num1 * num2
print("Multiplication:", result3)

result4 = num1 / num2
print("Division:", result4)

# Rounding
result5 = round(3.14159265359, 2)  # Rounds to 2 decimal places
print("Rounded:", result5)



# ==================== FLOAT DATATYPE EXAMPLES ====================

# Converts a float to an integer by removing decimal part
# Truncates towards zero (doesn't round)
num = 3.14159
converted = int(num)
print("Convert float to int:", converted)

# Rounds a float to a specified number of decimal places
# Default is 0 decimal places (returns integer)
num = 3.14159
rounded = round(num, 2)
print("Rounded to 2 decimals:", rounded)

# Returns the absolute value (removes negative sign)
# Works for both positive and negative floats
num = -3.14159
absolute = abs(num)
print("Absolute value:", absolute)

# Returns the smallest integer greater than or equal to the float
# Rounds upward (ceiling function)
import math
num = 3.14159
ceiling = math.ceil(num)
print("Ceiling value:", ceiling)

# Returns the largest integer less than or equal to the float
# Rounds downward (floor function)
num = 3.14159
floored = math.floor(num)
print("Floor value:", floored)

# Converts a float to a string representation
# Useful for concatenation or formatting
num = 3.14159
string_num = str(num)
print("Float as string:", string_num)

# Calculates the square root of a float
# Requires math module
num = 25.0
sqrt = math.sqrt(num)
print("Square root:", sqrt)

# Raises a float to a power (exponent)
# base ** exponent
num = 2.5
power = num ** 2
print("2.5 raised to power 2:", power)

# Checks if a value is a float or int
# Returns True if it's a float type
num = 3.14159
is_float = isinstance(num, float)
print("Is float?:", is_float)

# Formats a float with specific decimal places
# Returns a string with formatted value
num = 3.14159
formatted = f"{num:.2f}"
print("Formatted to 2 decimals:", formatted)



