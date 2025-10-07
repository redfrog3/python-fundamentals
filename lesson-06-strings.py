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


## Built in functions

country = "Finland"
length_of_word = len(country)
print(length_of_word)   
statement = "PaTrIcK"
print("\nUppercase:", statement.upper())
print("\nLowercase:  ", statement.lower())