# Operators 
# operarors are building blocks of programming languages. They are used to perform operations on variables and values. Python divides the operators in the following groups:
# Arithmetic Operators: Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, division,power,flow division,modulus. For example: +, -, *, /, **, //, %.
# Addition:
x = 5
y = 3
print(x + y) # it will print 8
# Subtraction:
x = 25
y = 10          
print(x - y) # it will print 15
# Multiplication:
x = 25
y = 3
print(x * y) # it will print 75
# Division:
x = 25
y = 5
print(x / y) # it will print 5.0
# // : it is used to perform floor division. It returns the largest integer less than or equal to the result of the division.
# For example:
print(5 // 2) # will return 2
print(7 // 3) # will return 2
# power: it is used to perform power operation. It returns the result of raising the first operand to the power of the second operand.
# For example:
print(2 ** 3) # will return 8 
# modulus: it is used to perform modulus operation.it Actually shows the remainder of the division.
# For example:
print(5 % 2) # will return 1
print(7 % 3) # will return 1
#Assignment Operators: Assignment operators are used to assign values to variables. like (=)
""" Shorthand operators: Shorthand operators are used to perform operations on variables and assign the result to the same variable. 
For example: +=, -=, *=, /=, **=, //=, %=."""
# For Example:
x = 5
x += 3 # it is equivalent to x = x + 3
print(x) # it will print 8 becauuse We assigned 5 to x and then we added 3 to x and assigned the result to x.
x = 8
x -= 3
print(x)
x = 9
x //=3
print(x)
# String also used some operators like + and *.
x = "Hello"
y = "Brother"
z = x + " " + y
print(z)
print("Hello"*3) # it will print HelloHelloHello