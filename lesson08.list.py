# LISTS IN PYTHON
# Lists store multiple values in one variable.
# They are ordered, mutable (changeable), and allow duplicates.

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

# add elemnt at end:
animals.append("Glass Frog")
print(animals)

# insert element at specific index note: every list starts from 0 then 1: example: 0, 1, 2, 3, 4, 5,
animals.insert(2, "aye-aye")
print("Inserted one animal:", animals)
animals.insert(0, "camel")
print("Inserted another animal:", animals)

#remove animal
animals.remove("babirusa")
print(animals)

last_animal = animals.pop()
print("Removed animal:", last_animal)
print("Remaining animals:", animals)




print()
print()
print()
print()
print()
print()


