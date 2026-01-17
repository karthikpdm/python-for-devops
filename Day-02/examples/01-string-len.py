# Returns the total number of characters in a string
# Counts spaces, letters, and all other characters
text = "Python is awesome"
length = len(text)
print("Length of the string:", length)

# Converts all characters in a string to uppercase letters
# Useful for case-insensitive comparisons or formatting
karthik = "my name is karthik bm so what about you"
alpehebet = karthik.upper()
print("length of the string is =", alpehebet)

# Converts all uppercase letters to lowercase
# Opposite of upper() method
karthik = "MY NAME IS KARTHIK BM SO WHAT ABOUT YOU"
alpehebet = karthik.lower()
print("length of the string is =", alpehebet)

# Removes leading and trailing whitespace (spaces, tabs, newlines)
# Does not remove spaces between words
karthik = "                  my name is karthik bm so what about you     "
strip = karthik.strip()
print("length of the string is =", strip)

# Splits string into a list of words using spaces as delimiter
# Returns a list of individual words
karthik = "my name is karthik bm so what about you"
split = karthik.split()
print("length of the string is =", split)

# Replaces all occurrences of a substring with another substring
# Returns a new string with replacements made
karthik = "my name is karthik bm so what about you"
replace = karthik.replace("karthik", "gowda")
print("length of the string is =", replace)

# Returns the index (position) of the first occurrence of a substring
# Returns -1 if the substring is not found
karthik = "my name is karthik bm so what about you"
find = karthik.find("karthik")
print("find =", find)

# Returns the index of the first occurrence of a substring
# Raises ValueError if the substring is not found (unlike find)
karthik = "my name is karthik bm so what about you"
index = karthik.index("karthik")
print("index =", index)

# Counts how many times a substring appears in the string
# Returns an integer count
karthik = "my name is karthik bm so what about you karthik"
count = karthik.count("karthik")
print("count =", count)

# Checks if the string starts with a specific substring
# Returns True or False (boolean)
karthik = "my name is karthik bm so what about you"
startswith = karthik.startswith("my")
print("startswith =", startswith)

# Checks if the string ends with a specific substring
# Returns True or False (boolean)
karthik = "my name is karthik bm so what about you"
endswith = karthik.endswith("my")
print("endswith =", endswith)

# Checks if all characters are alphanumeric (letters and numbers only)
# Returns False if spaces or special characters exist
karthik = "mynameiskarthikbmsowhataboutyou"
isalnum = karthik.isalnum()
print("isalnum =", isalnum)

# Checks if all characters are alphabetic letters only
# Returns False if numbers or spaces are present
karthik = "my name is karthik bm so what about you"
isalpha = karthik.isalpha()
print("isalpha =", isalpha)

# Checks if all characters are digits (numbers 0-9 only)
# Returns False if any letters or spaces are present
karthik = "my name is karthik bm so what about you"
isdigit = karthik.isdigit()
print("isdigit =", isdigit)

# Checks if the string contains only whitespace characters
# Returns False if any non-space characters exist
karthik = "my name is karthik bm so what about you"
isspace = karthik.isspace()
print("isspace =", isspace)

# Checks if string follows title case (first letter of each word capitalized)
# Returns False if not in proper title case format
karthik = "my name is karthik bm so what about you"
istitle = karthik.istitle()
print("istitle =", istitle)