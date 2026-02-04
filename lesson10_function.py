# python functions are simply blocks of code that can be reused
# to tun a function, you "call" the function by writing its name followed by parenthesis, and any arguments that it needs.

print("functions (procedures)")
print("\nExample 1")
def say_hi():
    print("Hi")

def say_bye():
    print("Bye")

say_hi()
say_bye()
say_bye()

print("\nExample 2")
def express_this(e): # e is called a PARAMETER, which is a placeholder for an ARGUMENT 
    return e

expression1 = express_this(1+2)  # the mathmatical expression here is the ARGUMENT, the actual value that will be used by a functions PARAMETER
print(expression1)

expression2 = express_this(2 * 6)
print(expression2)

print("\nExpression3")

def greeter(n):   # n is the parameter
    return f"Hi {n}!"

first = greeter("mr. meows")
second = greeter("Gwoodalert")
third = greeter("Lebron James")

print(first, second, third)

print("\nExample 4")
def remainder(a,b):
    return a % b 

result = remainder(3,2)
print("remainder:", result)

print("\nExample 5")

def is_far(distance):
    # INSERT BASE CASE
    if distance < 1:
        return "Error"

    if distance >= 100:
        return "That's far"
    elif distance < 100 or distance >= 20:
        return "That's not too far"
    elif distance < 20:
        return "That's nearby!"
    
print(is_far(30))
print(is_far(-55))
print(is_far(200))
print(is_far(0))

# I want to create a function that takes in a number and doubles it, then adds it to a list.
# The function should also take in a number of times that we should double the number

def double_sequencer(number, times):
    value = number
    sequence = []
    
    for i in range(times):
        value = value * 2
        sequence.append(value)
        return sequence
    
    return sequence

result = double_sequencer(1, 5000)
print(result)



#1

# PROCEDURE add(a, b)
# display(a + b)
# PROCEDURE subtract(a, b)
# display(a - b)
# PROCEDURE divide(a, b)
# display(a / b)
# PROCEDURE multiply(a, b)
# display(a * b)

def express_this(e)
    return(e)
add = express_this(a + b)
print(add)
subtract = express_this(a - b)
print(subtract)
divide = express_this(a / b)
print(divide)
multply = express_this(a * b)
print(multply)

# 2
# def avergage(n1, n2, n3)
# average(n1 +n2 + n3) /3
# display(average)

def average(num1, num2, num3):
    average = (num1 + num2 + num3) / 3
    return average


# 3
#
#
#

def is_even(num):
    is_odd = ""
    if num % 2 == 0:
        return(is_even)
    else:
        return(is_odd)




# 4
def analyze_word(word): 

    vowelCount = 0

    consonantCount = 0

vowels = ["a""e""i""o""u""A""E""I""O""U"]
    for i in word
        if i == vowels:
            return( += 1)
        else:
            return( -=)