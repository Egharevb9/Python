#Tuples
# A tuple is an ordered,immutable (unchangeable) collection of items in python.
#creating tuples

#using parentheses()
#example 1: tuple with multiple items
fruits = ("apple", "banana", "cherry")
print(fruits)

# without parentheses(tuple packing)
numbers = 1, 2, 3
print(numbers)

# single_item tuple (must include a comma)
single_item = ("apple",)
print(single_item)
print(type(single_item))


# using the tuple() constructor
fruit_list = ["apple" , "banana", "cherry"]
fruit_tuple = tuple(fruit_list)
print(fruit_tuple)

# Characteristics of Tuples
# 1. Ordered – Items have a fixed position.
# 2. Immutable – Cannot change after creation.
# 3. Allow duplicates – Same value can appear multiple times.
# 4. Can contain mixed data types – Strings, integers, lists, etc.
# 5. Can be nested – Tuples inside tuples.
# ordered
colors= ("red", "green","blue")
print(colors[0])

# Immutable ( uncomment and run. This will cause an error)
# colors[1] = "yellow"  #  TypeError

# Allow duplicates
numbers = (1, 2, 2, 3)
print(numbers)  # (1, 2, 2, 3)

# mixed data types
mixed = ("apple", 3, True, 5.6)
print(mixed)


# Nested tuples
Nested = (("a", "b"), (1, 2))
print(Nested)

# Tuple Operations
# Even though tuples are immutable, you can still perform several operations

# Indexing

fruits = ("apple", "banana", "cherry")
print(fruits[1])   # banana
print(fruits[-1])  # cherry

# Slicing
print(fruits[0:2])   # ('apple', 'banana')
print(fruits[::-1])  # ('cherry', 'banana', 'apple')

# Concatenation
tuple1 = (1, 2)
tuple2 = (3, 4)
result = tuple1 + tuple2
print(result)

#  Repetition
nums = (1, 2)
print(nums * 3)

# Membership

fruits = ("apple", "banana", "cherry")
print("banana" in fruits)  # True
print("grape" not in fruits)  # True


# Iteration
for fruit in fruits:
    print(fruit)


# working with tuples

