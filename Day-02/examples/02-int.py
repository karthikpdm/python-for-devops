# Integer variables
num1 = 10
num2 = 5

# Integer Division
result1 = num1 // num2
print("Integer Division:", result1)

# Modulus (Remainder)
result2 = num1 % num2
print("Modulus (Remainder):", result2)

# Absolute Value
result3 = abs(-7)
print("Absolute Value:", result3)



# ==================== INT DATATYPE EXAMPLES ====================

# Converts a string to an integer
# Raises ValueError if string contains non-numeric characters
string_num = "42"
converted = int(string_num)
print("String to int:", converted)

# Converts a float to an integer by removing decimal part
# Truncates towards zero
num = 42.9
converted = int(num)
print("Float to int (truncated):", converted)

# Returns the absolute value (removes negative sign)
# Works for both positive and negative integers
num = -42
absolute = abs(num)
print("Absolute value:", absolute)

# Checks if an integer is even or odd
# Uses modulo operator (%)
num = 42
is_even = (num % 2 == 0)
print("Is 42 even?:", is_even)

# Performs floor division (divides and rounds down)
# Returns an integer result
num1 = 42
num2 = 5
result = num1 // num2
print("Floor division 42 // 5:", result)

# Calculates remainder after division (modulo operation)
# Returns the remainder as an integer
num1 = 42
num2 = 5
remainder = num1 % num2
print("Remainder 42 % 5:", remainder)

# Raises an integer to a power (exponent)
# base ** exponent
num = 2
power = num ** 3
print("2 raised to power 3:", power)

# Converts an integer to a string representation
# Useful for concatenation or formatting
num = 42
string_num = str(num)
print("Int as string:", string_num)

# Checks if a value is an integer type
# Returns True if it's an int type
num = 42
is_int = isinstance(num, int)
print("Is int?:", is_int)

# Formats an integer with leading zeros
# Returns a string with specified width
num = 42
formatted = f"{num:05d}"
print("Int formatted with leading zeros:", formatted)

# Returns the minimum value from a list of integers
# Compares all values and returns smallest
numbers = [42, 15, 78, 3, 99]
minimum = min(numbers)
print("Minimum value:", minimum)

# Returns the maximum value from a list of integers
# Compares all values and returns largest
numbers = [42, 15, 78, 3, 99]
maximum = max(numbers)
print("Maximum value:", maximum)

# Calculates the sum of all integers in a list
# Returns the total as an integer
numbers = [42, 15, 78, 3, 99]
total = sum(numbers)
print("Sum of integers:", total)
