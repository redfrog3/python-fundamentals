print("\n--- User Input Demonstration ---")

name = input("Enter your name: ")
print(name)

age = input("Enter your age: ",)
print("your age is: ", age)

age_number = int(age)
print("Next year, you will be: ", age_number + 1)

# Example with float input
height = float(input("Enter your height in meters: "))
print("You are", height, "meters tall.")

# Ask the user for their favorite color and print out a message using it.

Color = input("Enter you favorate color")
print("The color", Color, "is a fantastic color!")

# Challenge 2: Adding Two Numbers
# Ask the user for two numbers, add them together, and print the result.

import math
Numbers = input("enter a single number")
Number = input("enter another number")
print("Your numbers added: ", Numbers + Number)

# Challenge 3: Circle Area from User Input
# Ask the user for the diameter of a circle, then calculate and print the area.
# Refer to lesson 3 or 4.

import math

Rad = float(input("Enter the diameter of a circle to find the area"))
Area = 3.14 * ((Rad / 2) ** 2) 
print("The area of a circle with the diameter of", Rad ,"is",Area)

# Challenge: Custom Die Roll
# Ask the user to enter how many sides the die should have.
# Then simulate rolling the die once and print the result.
import random

Sides = int(input("How many sides would you like you die to have?"))
roll = random.radiant(1, sides)
print("your rolled" roll)

