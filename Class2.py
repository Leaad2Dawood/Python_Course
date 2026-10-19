# String 
a = "Nature"
print(a)
# Indexing: Indexing is a way to access individual characters in a string. In Python, strings are indexed starting from 0. For example, the first character of the string "Nature" is at index 0, the second character is at index 1, and so on.
# and we can use negative indexing to access characters from the end of the string. For example, the last character of the string "Nature" is at index -1, the second last character is at index -2, and so on.  
print(a[0])
print(a[-1], a[5])
a = "Beautiful Nature"
print(a)
print(a[9])
print(a[11])
# All words that came in a string have will be counted and accessed as index and even the space also have index like in Beautiful and Nature it has space which will acccessed on a[10].
# String slicing: In string slicing we only slice specific words from the string like:
a = "Sheryians Coding" 
print(a) 
# here we follow three steps: Start,End(stop), and Steps. 
# Start: it is the start of index from where we wan to start.
# Stop: it is the end of index to where we want to end.
# steps: it means how much step itwill go further like 1 or 2?
print(a[0:9:1]) 
print(a[0:9:2]) 
# There are default values as well like if we dont add anything just :: for slicing than python will consider first : as 0 index and last as : . so it will pront out all.
print(a[::])
a = "Hello i am Data Scientist"
print(a) 
print(a[0:5]) 
print(a[11:15]) 
print(a[16:25]) 
# immutable nature: we can't change the string
# print Statement ways
"""using Normal variable in print statement(using+): like print(any data type), print(12),print"("HELLO"), print(a)"""
# What is formatted string:formatted string is a way to format strings in Python. 
# It allows you to embed expressions inside string literals, using curly braces {}.
# The expressions are evaluated at runtime and then formatted using the format() method or f-strings (available in Python 3.6 and later). For example: 
Name = "Muhammad Dawood"
age = 25
Des =   "Data Scientist"
print(f"My name is {Name} and i am {age} years old and i am a {Des}.")
# Escape Sequence: Escape sequences are special characters that are used to represent certain characters in a string. 
# They are preceded by a backslash (\).
# For example, \n is used to represent a new line, \t is used to represent a tab, and \\ is used to represent a backslash. For example:
print("Hello\nWorld!") # it will print Hello in first line and World in second line.
print("Hello\tWorld!") # it will print Hello and World with a tab space in between.
print("Hello\\World!") # it will print Hello\World! with a backslash in between.
# raw String: raw strings are strings that are prefixed with an 'r' or 'R'. They are used to treat backslashes as literal characters, rather than escape characters. For example:
print(r"Hello\nWorld!") # it will print Hello\nWorld! with a backslash in between.

# Type Conversion: Type conversion is the process of converting one data type to another. In Python, we can use the following functions to convert data types:
# int(): converts a value to an integer: means if we have a float value or a string value and want to convert it into integer than we can use int() function. 
# For example: int(3.14) will return 3, int("10") will return 10.
# float(): converts a value to a float: means if we have an integer value or a string value and want to convert it into float than we can use float() function.
# For example: float(3) will return 3.0, float("10.5") will return 10.5.
# str(): converts a value to a string: means if we have an integer value or a float value and want to convert it into string than we can use str() function.
# For example: str(3) will return "3", str(3.14) will return "3.14".
# Bolean(): converts a value to a boolean: means if we have an integer value or a float value or a string value and want to convert it into boolean than we can use bool() function.
# For example: bool(0) will return False, bool(1) will return True, bool("") will return False, bool("Hello") will return True.
# Truthy and Falsy values: In Python, some values are considered "truthy" and some are considered "falsy".
# Truthy values are values that evaluate to True in a boolean context.
# For example, non-zero numbers, non-empty strings, and non-empty lists are all considered truthy values.
# Falsy values are values that evaluate to False in a boolean context. 
# For example, 0,0.0, None, empty strings"", and empty lists[],{}, and () are all considered falsy values.
""" input(): The input() function is used to take input from the user. 
It takes a string as an argument, which is displayed as a prompt to the user. 
 The function then waits for the user to enter a value and press Enter. The value entered by the user is returned as a string. For example:
     name = input("What is your name? ")"""
name = input("What is your name? ")
print(f"My Name is {name}")
age = int(input("What is your age? "))
print(f"Your age is {age}")
