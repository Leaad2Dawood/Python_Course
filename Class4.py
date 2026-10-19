# Comparison Operators: they are used to compare two values. 
# They return True or False based on the comparison. For example: ==, !=, >, <, >=, <=.
a = 12
b = 45
print(b > a)  # This will return True
print(a < b)  # This will return True
print(a == b) # This will return False
print(a != b) # This will return True
print(a >= b) # This will return False
print(a <= b) # This will return True
# Logical Operators: they are used to combine conditional statements.
# and: returns True if both statements are true.
# or: returns True if one of the statements is true.
# not: returns True if the statement is not true.
x = 5
y = 10
z = 15
print(x < y and y < z)  # This will return True
print(x < y or y > z)   # This will return True
print(not(x < y))       # This will return False
# Conditionnal Statements: they are used to perform different actions based on different conditions.
# if statement: it is used to test a specific condition.  
# If the condition is true, the code block inside the if statement will be executed.
# Else Statement: it is used to execute a block of code if the condition in the if statement is false.
# We Can not write any condition in else statement.
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.") 
# Ternary operator: it is a shorthand way of writing an if-else statement. It takes three operands: a condition, a result for true, and a result for false.
# For example: result = value_if_true if condition else value_if_false
print("You are eligible to vote." if age >= 18 else "You are not eligible to vote.")
# Elseif Statement: it is used to test multiple conditions. If the condition in the if statement is false, the code block inside the elseif statement will be executed.
money = int(input("please give me 10,20,30 or above"))
if money == 10:
    print("i will have a choco bar")
elif money == 20:
    print("i will have a mango dolly")
elif money == 30:
    print("i will have a cone ice cream")
else:
    print("i will have a full Course meal")
a = 10
b = 40
c = 30
if a > b and a > c:
    print("a is the Largest")
elif b > a and b > c:
    print("b is the Largest")
else:
    print("c is the Largest")
