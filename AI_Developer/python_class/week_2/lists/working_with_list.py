#method 1: using Square brackets
Empty_list = []
print(Empty_list) #output

# #method 2: using the list() constructor
Empty_list2 = list()
print(Empty_list2) # output: []


#creating a list with initial Elements.
# lists can store multiple items separated by commas inside square brackets
# list of integers
numbers = [1, 2, 3, 4, 5]
print(numbers)


# list of strings
fruits = ["Apple", "banana", "cherry"]
print(fruits)


# # mixed data types
mixed_list = ["Alice", 25, 5.8, 'Esther',  True]
print(mixed_list)


# creating a list from another sequence. you can convert strings, tuples or other iterables into a list
# from a string (each character becomes an  element)
chars = list ("Hello")
print(chars)


# from a tuple
my_tuple = (10, 20, 30) 
list_from_tuple = list(my_tuple) 
print(list_from_tuple)# output:[10, 20, 30]

# from a range
numbers_range = list(range(5)) 
print(numbers_range) # output[1, 2, 3, 4]
# creating a list using list comprehesion. list comprehensions are a concise way to create a lists using a loop in one lines . we  will come back to this later 


# #squares of numbers 0-4
squares = [x**2 for x in range(5)]
print(squares)

# even numbers between 0-10
odds = [x for x in range(12) if x % 2 == 0]
print(odds)

# creating a Nested list. A list can contain other lists it is useful for matrices or grouped data
# Matrix-like list
matrix =[[1, 2], [3, 4], [5, 6], ["Esther","blessing","joy"],['book']]
print(matrix)

# #Accessing Elements in a nested list
print(matrix[0])
print(matrix[0][1])


# Characteristics of a list
# Ordered Collection
# The elements in a list maintain the order in which they are inserted.
#  The first element has index 0, the second has index 1, and so on.
fruits = ["mango", "orange", "banana"]
print(fruits)
print(fruits[0])
print(fruits[2])


#  Allows Duplicates
# - Lists can store the same value multiple times.
items = ["rice", "beans", "yam", "rice" , "peanut", "bread"]
print(items)

# #  Mutable (Can Be Changed)
# # You can modify a list after it’s created—change elements, add new ones, or remove existing ones.
numbers = [1, 2, 3]
numbers[1] = 20 
print(numbers)

# Can Contain Different Data Types
#  A list can hold integers, strings, floats, booleans, and even other lists.
mixed = [10, "Nigeria", 3.14, True]
print(mixed)

# # Can Be Nested
# #  A list can contain other lists (2D or multi-dimensional lists).
nested_list =[[1, 2], ["a", "b"]]
print(nested_list)
print(nested_list[0][1])


#  Dynamic Size
# You don’t need to declare the size of a list beforehand; it can grow or shrink as needed.
name = ["Ada"]
name.append("Bola")
name.append("chidi")
print(name)