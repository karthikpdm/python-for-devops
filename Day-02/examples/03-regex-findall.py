import re

text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")


# ==================== REGEX (REGULAR EXPRESSIONS) EXAMPLES ====================

import re

# Checks if a pattern matches at the beginning of a string
# Returns a Match object if found, None if not found
text = "Python is awesome"
pattern = r"^Python"
match = re.match(pattern, text)
print("match() =", match)

# Searches for a pattern anywhere in the string
# Returns a Match object for the first occurrence found
text = "Python is awesome and Python is fun"
pattern = r"Python"
search = re.search(pattern, text)
print("search() =", search)

# Finds all occurrences of a pattern in the string
# Returns a list of all matches found
text = "Python is awesome and Python is fun Python rocks"
pattern = r"Python"
findall = re.findall(pattern, text)
print("findall() =", findall)

# Finds all occurrences with their positions (start, end indices)
# Returns an iterator of Match objects with location information
text = "Python is awesome and Python is fun"
pattern = r"Python"
finditer = re.finditer(pattern, text)
print("finditer() =", list(finditer))

# Replaces all occurrences of a pattern with a replacement string
# Returns the new string with replacements made
text = "Python is awesome and Python is fun"
pattern = r"Python"
replaced = re.sub(pattern, "Java", text)
print("sub() =", replaced)

# Replaces only the first N occurrences of a pattern
# count parameter specifies how many replacements to make
text = "Python is awesome and Python is fun and Python rocks"
pattern = r"Python"
replaced = re.sub(pattern, "Java", text, count=2)
print("sub() with count =", replaced)

# Splits a string by a pattern delimiter
# Returns a list of substrings split at pattern matches
text = "Python,Java,C++,JavaScript,Ruby"
pattern = r","
split = re.split(pattern, text)
print("split() =", split)

# Extracts groups from a pattern using parentheses
# Returns the matched groups as a tuple
text = "My email is karthik@gmail.com"
pattern = r"(\w+)@(\w+)"
match = re.search(pattern, text)
print("groups() =", match.groups())

# Extracts a specific group from a pattern match
# Returns the text of the specified group number
text = "My email is karthik@gmail.com"
pattern = r"(\w+)@(\w+\.\w+)"
match = re.search(pattern, text)
print("group(1) =", match.group(1))
print("group(2) =", match.group(2))

# Matches any single digit (0-9)
# Character class [0-9] or shorthand \d
text = "I have 5 apples and 10 oranges"
pattern = r"\d"
digits = re.findall(pattern, text)
print("Digits (\d) =", digits)

# Matches any non-digit character
# Opposite of \d
text = "I have 5 apples and 10 oranges"
pattern = r"\D"
non_digits = re.findall(pattern, text)
print("Non-digits (\D) =", non_digits)

# Matches any word character (letters, digits, underscore)
# Equivalent to [a-zA-Z0-9_]
text = "Hello_World123 @#$%"
pattern = r"\w"
word_chars = re.findall(pattern, text)
print("Word characters (\w) =", word_chars)

# Matches any non-word character
# Opposite of \w
text = "Hello_World123 @#$%"
pattern = r"\W"
non_word = re.findall(pattern, text)
print("Non-word characters (\W) =", non_word)

# Matches any whitespace character (space, tab, newline)
# Includes spaces, tabs, and line breaks
text = "Hello World\tPython\nJava"
pattern = r"\s"
whitespace = re.findall(pattern, text)
print("Whitespace characters (\s) =", whitespace)

# Matches any non-whitespace character
# Opposite of \s
text = "Hello World Python Java"
pattern = r"\S"
non_whitespace = re.findall(pattern, text)
print("Non-whitespace characters (\S) =", non_whitespace)

# Matches one or more occurrences of the pattern
# + means 1 or more repetitions
text = "I have 123 apples and 45 oranges"
pattern = r"\d+"
numbers = re.findall(pattern, text)
print("One or more digits (+) =", numbers)

# Matches zero or more occurrences of the pattern
# * means 0 or more repetitions
text = "color, colour, colr, col"
pattern = r"colou*r"
matches = re.findall(pattern, text)
print("Zero or more matches (*) =", matches)

# Matches exactly N occurrences of the pattern
# {N} means exactly N repetitions
text = "I have 123 apples and 45 oranges"
pattern = r"\d{3}"
matches = re.findall(pattern, text)
print("Exactly 3 digits ({3}) =", matches)

# Matches between N and M occurrences of the pattern
# {N,M} means N to M repetitions
text = "I have 123 apples and 45 oranges and 6 pears"
pattern = r"\d{2,3}"
matches = re.findall(pattern, text)
print("2 to 3 digits ({2,3}) =", matches)

# Matches zero or one occurrence of the pattern
# ? means 0 or 1 repetitions (optional)
text = "color, colour"
pattern = r"colou?r"
matches = re.findall(pattern, text)
print("Zero or one match (?) =", matches)

# Matches any single character except newline
# . matches any character
text = "cat, bat, rat, mat"
pattern = r".at"
matches = re.findall(pattern, text)
print("Any single character (.) =", matches)

# Matches any character inside the brackets
# Character class [abc] matches a, b, or c
text = "cat bat rat dog"
pattern = r"[cbr]at"
matches = re.findall(pattern, text)
print("Character class [cbr] =", matches)

# Matches any character NOT inside the brackets
# Negated character class [^abc]
text = "cat bat rat dog"
pattern = r"[^bc]at"
matches = re.findall(pattern, text)
print("Negated character class [^bc] =", matches)

# Matches any character in the range
# Range [a-z] matches lowercase letters a to z
text = "apple Apple APPLE 123"
pattern = r"[a-z]+"
matches = re.findall(pattern, text)
print("Lowercase range [a-z] =", matches)

# Matches any uppercase letter
# Range [A-Z]
text = "apple Apple APPLE 123"
pattern = r"[A-Z]+"
matches = re.findall(pattern, text)
print("Uppercase range [A-Z] =", matches)

# Alternation - matches one of several patterns
# | means OR
text = "I like cat, dog, and bird"
pattern = r"cat|dog|bird"
matches = re.findall(pattern, text)
print("Alternation (|) =", matches)

# Validates an email format
# Checks for standard email pattern
email = "karthik@gmail.com"
pattern = r"^[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
is_valid = bool(re.match(pattern, email))
print("Is valid email? =", is_valid)

# Extracts all phone numbers from text
# Matches pattern like (123) 456-7890
text = "Call me at (123) 456-7890 or (987) 654-3210"
pattern = r"\(\d{3}\) \d{3}-\d{4}"
phones = re.findall(pattern, text)
print("Phone numbers =", phones)

# Removes all special characters from a string
# Keeps only alphanumeric and spaces
text = "Hello@World#123$%^"
cleaned = re.sub(r"[^a-zA-Z0-9 ]", "", text)
print("Cleaned text =", cleaned)

# Extracts all words from a string
# \b is word boundary
text = "Hello World! Python is awesome."
pattern = r"\b\w+\b"
words = re.findall(pattern, text)
print("All words =", words)
