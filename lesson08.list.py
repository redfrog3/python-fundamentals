# LISTS IN PYTHON
# Lists store multiple values in one variable.
# They are ordered, mutable (changeable), and allow duplicates.


#initialize a list with brackets:
empty_list = []
empty_list.append("Thing")
print(empty_list)

print()
print("--- Lists in Python ---")

animals = ["donkey", "pangolin", "blobfish"]
numbers = [2, 4, 6, 8, 10]
mixed = ["piffle", 42, True, 9.99]

print(animals)
print(numbers)
print(mixed)

print()
print()
print()
print("--- Indexing: how to access the elements of a list ---")
print("First Element:", animals[0])
print("Second element:", animals[1])
print("third element:", animals[-1])

print()
print()
print("--- Modifying Lists ---")
animals[0] = "babarusa"
print(animals)

animal_to_replace = animals.index("pangolin")
print(animal_to_replace)
animals[animal_to_replace] = "seamonkey"


# add elemnt at end: .append
animals.append("Glass Frog")
print(animals)

# insert element at specific index .insert---note:every list starts from 0 then 1: example: 0, 1, 2, 3, 4, 5,
animals.insert(2, "aye-aye")
print("Inserted one animal:", animals)
animals.insert(0, "camel")
print("Inserted another animal:", animals)

#remove animal .remove
#animals.remove("babirusa")
#print(animals)

last_animal = animals.pop()
print("Removed animal:", last_animal)
print("Remaining animals:", animals)




print()
print()
print()
print()
print()
print()

#len = length
nums = [3, 7, 1, 9, 4, 2, 5, 8, 6, 0]
print("Original Numbers:", nums)

print("Length of the list:", len(nums))
print("Min:", min(nums))
print("Max:", max(nums))
print("Sum:", sum(nums))

#organize = .sort
nums.sort()
print(nums)
animals.sort()
print(animals)

#reverse = .reverse
nums.reverse()
print(nums)


print()
print("--- Checking Membership ---")

if "cat" in animals:
    print("Cat is in the list!")
else:
    print("Cat is not in the list.")

print()
print("--- Copying Lists ---")

original_list = [1, 2, 3]
copied_list = original_list
copied_list = original_list.copy()
copied_list.append(4)
print(original_list)
print(copied_list)


print()
print()
print()
print("--- Nested Lists/The Matrix ---")

#list inside of list
matrix = [  
    [1,2,3], 
    [4,5,6], 
    [7,8,9]  
    ] 

print(matrix[2])
print(matrix[0][2]) #first number is list and second is number in list



#challanges

### **Challenge 1: Integer Swap**

# Store this list in a variable: [ 1, 2, 3, 4, 5, 6 ] 
# Ask the user to enter a new integer.
# Replace the **third integer** in the original list with the user’s input, and then print the updated list.
# *Hint: use indexing and assignment.*

list = [1, 2, 3, 4, 5, 6]
print(list)
user_number = int(input("Enter a number: "))
list[2] = user_number
print(list)


### **Challenge 2: Shopping List Manager**

# Initialize an empty list called `shopping`.
# Add three items of your choice using `.append()`.
# Then insert one extra item at the second position 
# Remove one item of your choice.
# Finally, print the final shopping list.

shopping = []
print(shopping)
shopping.append = ("ice cream")
shopping.append = ("soap")
shopping.append = ("green cheese boi")
print(shopping)