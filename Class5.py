# Question Number 01:
import string


a = float(input("please tell the first number: "))
b= float(input("please tell the second number: "))
if a > b:
    print(f"The first number ({a}) is greater than the second number ({b})")
elif b>a:
    print(f"The first number ({b}) is greater than the second number ({a})")
else:
    print(f"The first number ({a}) is equal to the second number ({b})")
    
# Question Number 2:
gender = input("please tell your Gender in charcter (m,f):- ")
if gender == "m":
    print("Hello sir How are you?")
else:
    print("Hello madam How are you?")
 
 # Question Number 3:
gender = input("please tell your Gender in charcter (m,f):- ")
if gender == "m" or gender == "M":
    print("Hello sir How are you?")
elif gender == "f" or gender == "F":
    print("Hello madam How are you?")
else:
    print("Wrong input only provide m or f")
    
    # Question Number 4:
    integers = int(input("please tell the number: "))
    if integers % 2 == 0:
        print(f"The number {integers} is even")
    else:
        print(f"The number {integers} is odd") 
# Question Number 5:
# Voting Eligibility
name = input("please tell your name: ")
age = int(input("please tell you age:"))
if age >= 18:
    print(f"Hello {name}, you are eligible to vote")
else:
    print(f"Hello {name}, you are  eligible to vote after {18-age} years")
    
    # Question Number 6:
# Day_number to Day_name
day_number = int(input("please tell the day number (1-7): "))
if day_number == 1:
    print("Today is Monday")
elif day_number == 2:
    print("Today is Tuesday")
elif day_number == 3:
    print("Today is Wednesday")
elif day_number == 4:
    print("Today is Thursday")
elif day_number == 5:
    print("Today is Friday")
elif day_number == 6:
    print("Today is Saturday")
elif day_number == 7:
    print("Today is Sunday")
else:
    print("Invalid day number. Please enter a number between 1 and 7.")

# Question Number 7:
A = int(input("please tell the first number: "))
B = int(input("please tell the second number: "))
C = int(input("please tell the third number: "))
if A==B and A==C:
    print("All three numbers are equal.")
elif A==B or B==C or A==C:
    print(f"Any two numbers are equal.")
elif A > B and A > C:
    print(f"The first number ({A}) is the greatest among the three numbers.")
elif B > A and B > C:
    print(f"The second number ({B}) is the greatest among the three numbers.")
else:
    print(f"The third number ({C}) is the greatest among the three numbers.")

# Question number 8:
year = int(input("please tell the year:"))
if year %100 == 0 and year % 400 == 0:
    print("The year is a leap year.")
elif year % 100 != 0 and year % 4 == 0:
    print("The year is a leap year.")       
else:
    print("The year is not a leap year.")
    
    # Question number 9:
    Bill = int(input("please tell the Total amount: ")) 
    if Bill > 1000 and Bill <= 4999:
        discount = Bill * 0.10
        final_amount = Bill - discount
        print(f"Congratulations! You have received a 10% discount. Your final amount is: {final_amount}")
    elif Bill > 5000:
        discount = Bill * 0.20
        final_amount = Bill - discount
        print(f"Congratulations! You have received a 20% discount. Your final amount is: {final_amount}")
    else:
        print(f"Sorry, you are not eligible for any discount. Your total amount is: {Bill}")
        
        # Question number 10:
        Vowel = input("please tell the character: ")
        if Vowel in "aeiouAEIOU":
            print(f"The character '{Vowel}' is a vowel.")
        else:
            print(f"The character '{Vowel}' is a consonant.")
         
        