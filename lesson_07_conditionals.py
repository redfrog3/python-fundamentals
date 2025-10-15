# CONDITIONALS IN PYTHON
# comparison operators: ==, !=, <, >, <=, >=
# logical operators: and, or, not
# control flow: if, elif, else

print()
print("--- Conditionals in Python ---")
# Boolean refresher:
print( 3 == 2 )
print("Hello" == "Hi there")
print( 7 != 4)
print(4 > 5)

print()
print()
print()
print()
print()
print()



# if
num1 = 10 
if num1 == 10: 
    print("Your number is equal to 10")

# else
num2 = 11
print(num2 <= 12)
if num2 <= 12:
    print("Your number is less than or equal to 12")
else: 
    print("Your number is greater than 12")

# elif
temp = 65
if temp >= 80:
    print("Its hot!!!")
elif 60 <= temp < 80:
    print("It's nice out!!!")
else:
    print("Its cold!!!")



print()
print()
print()
print()
print()
print()



x = 20
y = 1

if x == y:
    print("x is equal to y")
elif x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("error")

print()
print()
print()
print()
print()
print()


age = 17
has_permission  = True

if age >= 17 and has_permission:
    print("you can drive")
else:
    print("you can't drive")


print()
print()
print()
print()
print()
print()


day = input("Enter any day of the week: ")

if day =="saturday" or day == "sunday":
    print("It's the weekend!")
else: 
    print("its the week")




# Using 'or' and 'not'
print("--- Using 'or' --- ")
day = "Monday"

if day == "Saturday" or  day == "Sunday":
    print("It's the weekend!")
elif day is "Monday" or day is "Tuesday":
    print("It's Monday or Tuesday")
else:
    print("It's Wed,Thur, or Fri")

if day is not "Monday":
    print("It's not Monday")

print()
print()
print()
print()
print()
print()



    # Challenge 1: Even or Odd
# Ask the user for a number, and tell them if it’s even or odd.
# Example output:
# Enter a number: 7
# 7 is odd.
# Hint: use modulus operator

import math

number = int(input("input an odd or even number: "))
eoon = number % 2
if eoon == 1:
    print("is odd")
else:
    print("is even")

print()
print()
print()
print()
print()
print()


# Challenge 2: Password Check
# Create a variable with a stored password
# Ask the user to enter a password. 
# If it matches the stored password, print "Access granted." Otherwise, "Access denied."
# Example output:
# Enter password: dolphin
# Access granted. Access denied.
# Enter password: swordfish
# Access granted.




user_pass_input = input("Enter your password")
password = ("qwerty")
if password == user_pass_input:
    print("access granted")
else:
    print("access denied")


print()
print()
print()
print()
print()
print()




    # Challenge 3: Grading System
# Ask the user for a numeric grade (0-100) and print a letter grade.
# Example output:
# Enter your grade: 94
# You earned an A.

grade_number = int(input("enter your numeral grade"))
if grade_number is 90 or 91 or 92 or 93 or 94 or 95 or 96 or 97 or 98 or 99 or 100:
    print("you have earned an A!")
elif grade_number is 80 or 81 or 82 or 83 or 84 or 85 or 86 or 87 or 88 or 89:
    print("you have earned a B!")
elif grade_number is 70 or 71 or 72 or 73 or 74 or 75 or 76 or 77 or 78 or 79:
    print("you have earned a C")
elif grade_number is 60 or 61 or 62 or 63 or 64 or 65 or 66 or 67 or 68 or 69:
    print("you have earned a D!")
else:
    print("you have failed!") 