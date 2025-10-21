# 1

palidrome = input("enter a palidrome: ") 
newpalidrome = palidrome[::-1]
if newpalidrome == palidrome:
    print("True")
else:
    print("False") 


# 2

user_mail = input("enter an email address: ")
mail = user_mail.index("@")
New = user_mail[mail::]
print(New)

# 3

list = ["orange", "blueberry", "cherry"]
userinput = input("enter a fruit from the list: ")
if userinput == list[2]:
    print("True")
else:
    print("False")

# 4

string = input("enter a word")
if string >= 3 and string != "ing":
    print(string)
elif string>= 3 and string == "ing":
    print(string)
else:
    print(string)