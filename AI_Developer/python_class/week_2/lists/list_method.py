#Python provides many built-in methods for working with lists.
#Here is each method, what it does, and an example.
#dot append() method**
#Adds an element to the end of the list.
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  
# Output: ['apple', 'banana', 'cherry']

#dot insert() method**
#Inserts an element at a specific position.
fruits = ["apple", "banana", "pawpaw"]
fruits.insert(2, "orange")
print(fruits)  
# Output: ['apple', 'orange', 'banana']



#dot extend() method
#Adds elements from another list (or iterable) to the end.
fruits = ["apple", "banana"]
tropical = ["mango", "pineapple", "watermelon"]
fruits.extend(tropical)
print(fruits)  
# Output: ['apple', 'banana', 'mango', 'pineapple']


#dot remove() method**
#Removes the first occurrence of a specified value.
fruits = ["apple", "banana", "cherry", "banana"]
fruits.remove("banana")
print(fruits)  
# Output: ['apple', 'cherry', 'banana']

#dot pop() method
#Removes and returns the element at a given index (default: last).
fruits = ["apple", "banana", "cherry"]
last_fruit = fruits.pop()
print(last_fruit)
print(fruits)

# dot clear() method
# Removes all elements from the list
fruits = ["apple", "banana", "cherry"]
fruits.clear()