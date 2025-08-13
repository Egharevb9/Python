#Operations in Python***List
#Python lists support a variety of operations for creating, modifying, and working with data.We will go through them step by step now.
# Concatenation (+)**
# Joins two lists into a new list.
# Joins two lists into a new list.

list1 = [1, 2, 3]
list2 = [4, 5]
result = list1 + list2
print(result)

#Repetition (*)
# Repeats elements in a list a given number of times.
nums = [1, 2]
repeated = nums * 3
print(repeated) 

#Indexing
# Access elements using their position (starting from 0)
fruits = ["apple", "banana", "cherry"]
print(fruits[0])
print(fruits[-1])

# licing
# Extract a portion of the list.

numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])
print(numbers[:3])
print(numbers[3:])
print(numbers[::2])

#Membership (in / not in)
#Checks if an element exists in a list.
colors = ["red", "green", "blue"]
print("green" in colors)
print("yellow" not in colors)

#Length (len())**
#Counts the number of elements in a list.
items = ["pen", "book", "laptop"]
print(len(items))

#Min and Max (min() / max())
#Returns the smallest or largest element.
nums = [5, 2, 9, 1]
print(min(nums))
print(max(nums))


# n Sum (sum())
# Adds all numerical elements ia list.
numbers3 = [1, 2, 3, 4 ,5]
print(sum(numbers3))

# List Comprehension**
# Creates a list in a single line.
#This should be familiar already, right?
squares = [x**2 for x in range(5)]
print(squares)

# Copying a List**
#Create a duplicate list.
a = [1, 2, 3]
b = a.copy() # or b = list(a)
print(b)
