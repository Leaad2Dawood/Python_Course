# For Loop: when we know how many times we want to repeat a task, we can use a for loop.
# The for loop is used to iterate over a sequence (like a list, tuple, dictionary, set, or string) and execute a block of code for each item in the sequence. 
# Understading the for loop:
# To understand the for loop we will first know the syntax of the for loop. The syntax of the for loop is as follows:
# Range function: The range() function is used to generate a sequence of numbers. 
# It takes three arguments: start, stop, and step.
#Start: The start argument is the starting number of the sequence, 
#Stop: The Stop argument is the ending number of the sequence (exclusive), 
# and the Step argument is the difference between each number in the sequence. 
# If the start argument is not provided, it defaults to 0. If the step argument is not provided, it defaults to 1.
print(list(range(0,50,5)))
ran = range(0,50,5)
for i in ran:
    print(i)
# Second
ran = range(1,10,1)
for i in ran:
    print("Hello how are you")
ran = range(1,10000,1)
for i in ran:
    print("Hello how are you")
print(len(ran))
# We can also write directly as:
for i in range(1,11,1):
    print("Hello World")
for i in range(10,41,1):
    print(i)   
for i in range(-10,21,1):
    print(i) 
for i in range(34,4,-1):
    print(i) 
for i in range(5,51,5):
    print(i)
for i in range(7,71,7):
    print(i)
# For Input
n = int(input("please tell what table you want"))
for i in range(n,(n*10)+1,n):
    print(i)
# for String
s = "Hello how are you"
for i in s:
    print(i) 
    
s = "Hello how are you"
for i in range(0,len(s),1):
    print(s[i])