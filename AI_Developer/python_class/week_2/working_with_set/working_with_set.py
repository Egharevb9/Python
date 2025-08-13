# In Python, a set is an unordered collection of unique elements. Sets are useful when you want to store multiple items but avoid duplicates.
# creating sets
# using curly braces
fruits = {"apple", "banana", "mango"} 
print(fruits)

# using the set() constractor
numbers = set ([1, 2, 3, 4])
print(numbers)

# creating an empty set (must use set(), not {})
empty_set = set()
print(empty_set)

# from a string (duplicates removed automatically)
letters = set("mississippi")
print(letters)


# characteristics of sets
# unordered: no defined indexing or sequence.
# unique elements: duplicates are automatically removed.
# mutable: ypu can add or remove items
# unindexed: you can't  access element using an index like my_set[0].
# supports mathematical set operations: Union , intersection, difference, symmetric difference

# set operations
# a. adding Elements

# colors = {"red", "blue","yellow"}
# colors.add("green")
# print(colors)


# # removing ELements
# colors.remove("blue") 
# colors. discard("yellow")
# print(colors)


# pop an element
colors = {"red", "blue", "green"}
removed = colors.pop()
print("Removed:" , removed)
print("Remaining:", colors)


# Clear a Set
colors.clear()
print(colors)

# Mathematical Set Operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}


# Union
print(set1 | set2)
print(set1.union(set2))


# Intersection
print(set1 & set2)
print(set1.intersection(set2))


# Difference
print(set1 - set2)
print(set1.difference(set2))

#  Symmetric Difference
print(set1 ^ set2)
print(set1.symmetric_difference(set2))


# Working with Sets
# Collecting unique visitors to an event
visitors = set()

# Adding visitors
visitors.add("Chinedu")
visitors.add("Aisha")
visitors.add("Chinedu") # Duplicate, ignored automatically
print("Visitors:", visitors)

# Checking if a visitor attended
# (Dont worry if you can't figure this part out yet. We will discuss it properly later in the course.)

name = "Aisha"
if name in visitors:
    print(f"{name} attended the event.")
else:
    print(f"{name} did not attend the event.")