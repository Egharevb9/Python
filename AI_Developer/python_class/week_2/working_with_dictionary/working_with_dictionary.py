# python Dictionaries
# . A dictionary in python is a collection of key_value pairs.
# KEYS are unique and used to store and retrieve values
# values can be any data type (string, interger, list, tuple, even another diction).

# SYNAX
# dictionary_name = {key1: value1, key2: value2}

# characteristics of Dictionaries

# key-value structure: Each items is stored as a key: value pair.
# mutable: you can add , change, or remove items.
# unordered  (before python3.7): from python 3.7+, they maintain insertion order.
# unique keys : no duplcate keys allowed ; a new assigment to an existing key overwrites the old values

# keys must be immutable: string, numbers, tuples (containing only immutable items can be keys)


# creating dictionaries
# using curly braces
student = {
    "name": "ADa",
    "Age": 20,
    "course": "computer science"
}
print(student)

# using the dict() constructor
student_info = dict(name="John", Age=25, course="maths")
print(student_info)

# Empty Dictionary
empty_dict = {}
print(empty_dict)


# Dictionary comprehension
# syntax:
# {key_expression: value_expresssion for item in iterable if condition}
# create a dictionary of number and their squares
squares = {x: x**2 for x in range(1, 6)}
print(squares)


# with condition

# dictionary of even numbers and thier cubes
even_cube = {x: x**3 for x in range(1, 10) if x % 2 == 0}  # x  represent key
print(even_cube)
#if x % 2 == 0 
for x in range(1, 10):#  for x in range(1, 10) is used to print numbers between 1- 10
    if x % 2 ==0: #is used to print out numbers that can be divided by 2withoutreminders
        print(x)


# from excisting dictionary
students = {"ADa": 85, "john":40, "musa":65}
# filter students who  passed (score >= 50)
passed_students = {name: score for name, score in students.items() if score >= 50}
print(passed_students)


#using string keys
names = ["Ada", "john", "musa"]
lengths = {name: len(name) for name in names}
print(lengths)

# Accessing dictionary items

# define a dictionary
student = {"name": "Ada", "age":20, "course":"computer science"}


# using key 
print(student["name"])

# using get() method (avoids error if key is missing)
print(student.get("age"))
print(student.get("grade", "not found"))


# modifying dictionaries
student["age"] = 21 #change value 
student["grade"] = "A" # add new key-value pair
student["sure_name"] = "thomas"
print(student)

# Removing items from Dictionaries
# using pop()
student.pop("grade")
print(student)

# using popitem() - removes last inserted key-value
student.popitem()

# using del kyword
del student["course"]
print(student)

# using clear()- removes all items
student.clear()
print(student)

# Dictionary methods
# dot keys(), dot values(), dot items(), dot update()
person = {"name": "Emeka", "age": 30}
# key()
print(person.keys())

# values()
print(person.values())

# items()
print(person.items())

# update()
person.update({"age": 31, "city": "lagos", "mother":"abigail"})
print(person)


