# control flow in python 
# control flows refers to the order in which statements are excuted in a program. instead of always running line by line control flow allows your program to :
# make decisions (choose one path or another, explore alternatives)
# repeat actions (loops)
# it is the foundation for logica and problem  solving in programming.PendingDeprecationWarning
# control flow is divided into 3 parts


# conditional statements
# if statement
# executes a block only when a condition is True

age = 20 
if age >= 18:
    print("you are eligible to vote")

    # some usecases
    # checking for eligibility
    # validating login attemps.
    # Ensuring a minimum purchase requiredment, etc
# if-else statement

# provides two alternative paths
wallet = 400
price = 500
if wallet >= price:
   print("purchase successful")
else:
    print("insufficient balance")

    # some  usee cases
# deciding success or failur of a payment
# grantig or denying access to a system.
# determinin pass/fail in an exam, etc.

# if_elif-else statement
#  used for multiple conditions.
score = 85
if score >= 70:
    print("Grade  A")
elif score >= 50:
    print("Grade  B") 
else:
    print("Grade C")

# some usecases 
# voting eligibility(age + citizenship)
# - Banking (account active + balance sufficient).
# - School admission (age + grade level).


# Loops
# for loop
# This is used for iterating over a sequence (strings, list, tuple, dictionary)
# iterates through each element in a List 
fruits = ["apple", "banana", "orange"]
for fruit in  fruits: 
    print(f"i like {fruit}")

    # Some usecases
# Iterating through shopping lists.

# Checking availability of products.

# Displaying student names, etc.

# Iterates through each element in a TUPLE.This Works like lists, but remember that tuples are immutable.

coordinates = (0.34654, -0.48585, 0.57477)
for point in coordinates:
    print(f"point: {point}")
    # some usecase
    # storing fixed sensor readings.
    # displaying fixed seating positions, etc

    # iterates through each element in a dictionary. remember that dictionaries have key-value pairs
student = {"name": "Tunde","age": 16,"grade": "A"}
for key, value in  student.items():
    print(f"{key}: {value}")

## Some usecases

# Reading database records.

# Showing user profile details.

# Checking configuration settings, etc.


# Iterates through each element in a STRING. Remember that strings are sequences of characters.
word = "PYTHON"
for char in word:
    print(char)


## Some usecases

# Counting vowels/consonants.

# Password validation (checking digits/special chars).

# Text analysis, etc.

# while loop 
# a while loop is used to repeatedly execute a block of code as long as a given condition is true . Unlike the for loop (which iterates over sequences like lists, tuples, etc.), the while loop is condition-based.

# while condition:
 # code block

# - The condition must evaluate to `True` for the loop to continue running.

# - When the condition becomes `False`, the loop stops.

# sing while loop

## Documenting my thoughts##
# Let the loop start with count = 1
# Let it keep printiUng until count is greater than 5
# Let the loop terminate when the condition is no longer true

## My code
count = 1 
while count <= 5:
    print("number:", count)
    count += 1

    # Incrementing with `while`
    num = 1
    while num <= 10:
        print(num, end=" ")
        num  += 1

# Decrementing with `while
timer = 10
while timer > 0:
    print("countdown:", timer)
    timer -= 1


    password = ""
    while password != "python123":
       password = input("Enter the password: ")
print("Access granted!")


# Understanding while True
# - The while True: loop is an infinite loop — it keeps running forever until you explicitly stop it with a break statement or by exiting the program.
# - It is commonly used when:
# - You don’t know in advance how many times you want the loop to run.
# - You want to keep asking the user for input until a valid condition is met.
# - You are building continuous programs like menus, login systems, or simulations.
# while True:
    # Code block
    # Must include a break statement to stop