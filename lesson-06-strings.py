greeting = "Hello"
name = "Ada"
print(greeting, name)

# 0 1 2 3 4 
# H e l l o

# 0 1 2
# A d a

message = greeting + " " + name + "!!!"
print("concentrated message: ", message)
print(greeting[1])
second_letter = greeting[1] 
print(second_letter)

word = "super-cali-fragil-istic-expi-ali-docius"
print("First letter: ", word[0])
print("last letter: ", word[1])
print("Range of lettters (non-inclusive):",word[0: 5], word[18:23])
print("reversed, Steping through every every letter:", word[::-3])


phrase = input("Enter a phrase")
print("Here is every third letter of your phrase: ",  phrase [::-3])

## Built-in string functions

last_name = "Lovelace"
length = len(last_name)
print("Length of name:", length)

## Built in functions

country = "Finland"
length_of_word = len(country)
print(length_of_word)   
statement = "PaTrIcK"
print("\nUppercase:", statement.upper())
print("\nLowercase:  ", statement.lower())


sentace = "your a goofy goober"
new_sentace = sentace.replace("your", "I'm")

#Find and replace text
sentence = "I'm a goofy goober"
new_sentence = sentence.replace("I'm", "You're")
next_replacement = sentence.replace("goofy", "goober")
print(sentence)
print(new_sentence)
print(next_replacement)


# FORMATTED STRINGS IN PYTHON
# f-strings allow variables and expressions inside strings

print("\n--- Formatted Strings ---")

name = "Big dawg da absalut G"
age = 5
city = "dubai"

print(f"Hello, my name is {name}.\nI am {age} years old \nand I live in {city}.")


# f-strings can do math and function calls inside {}

print(f"Next year, i,ll be {age + 1}. My name in uppercase is {name.upper()}")