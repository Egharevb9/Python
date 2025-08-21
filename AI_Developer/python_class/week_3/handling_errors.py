# Handling Errors in Python
# Errors in Python are classified into three main categories:

#  Syntax Errors

#  Runtime Errors

#  Semantic Errors

#  Each category has its own characteristics, subtypes, and ways to handle them.



# Syntax Errors
# It occur when the Python interpreter cannot understand your code because it breaks Python grammar rules.

#  Please note that Program will not run until the error is fixed.

# Common Subtypes of Syntax Errors
#  IndentationError – Incorrect spacing

# for i in range(3):
#     print(i)

# Missing Colon/Parenthesis Error
# if 5 > 3 :
#     print("hello")

#    Invalid Syntax – General grammar mi**c. stakes.
# print (" hello")


# Invalid Syntax – General grammar mi**c. stakes.


# Runtime Errors


# The program is syntactically correct, but an error occurs while it is running.

# These are also called exceptions.

#  They can be handled with try, except, and finally.


# Common Subtypes of Runtime Errors
#  ZeroDivisionError – Dividing by zero.

# x = 10 / 0

# NameError – Using a variable before defining it
# print(age)


#  TypeError – Wrong data type in an operation.
# result = "10" + 5

#  ValueError – Invalid value for a function.
# number = int("abc")

# IndexError – Accessing list index out of range
# fruits = ["apple", "banana"]
# print(fruits[3])

# KeyError – Accessing a dictionary with a missing key
data = {"name": "Ada"}
print(data["age"])

#  FileNotFoundError – File does not exist.
# f = open("missing.txt")


# Handling Runtime Errors
#  Python provides exception handling to prevent programs from crashing when unexpected errors occur.

# The keywords used are;

#   a.try – block of code to test for errors.

#   b. except – block of code that runs if an error occurs.

#   c . finally – block of code that always runs (whether error occurs or not).

# The try Block

#  It is used to wrap code that might raise an error.

#  If no error occurs Python skips the except block.

# # try: 
#   x = 10/2
#   print("Result:",x)


#  The except Block**

# It defines what to do if an error occurs inside try.

# It can catch specific errors or all errors.


# this is a specific Exception

# try: 
#    x = 10 / 0
# except ZeroDivisionError:
#    print("cannot divide by zero.")


# #    this is a case of multiple exception
# try:
#    number = int("abc")
#    result = 10 / 0
# except ValueError:
#    print("invalid conversion to integer. ")
# except ZeroDivisionError:
#    print("cannot divide by zero. ")


# # The `finally` Block**

# # Always runs, whether an error occurred or not.

# # Useful for cleanup tasks (e.g., closing files, releasing resources).

# # IF you don't understand this line of code now, It's Ok. But make sure you come back to it once we are done the *File Handling**.
# try:
   
#    f = open("sample.txt", "r")
#    content = f.read
# except FileNotFoundError:
#    print("file not found.")
# finally:
#    print("closing filee if it was open.")


# #    lets  have example on the application of try-except-finally, but try to read in betwwen the line for better understanding

balance = 5000


print("welcome to the ATM")
amount = input("Eenter amount  to withdraw: ")

try:
    amount = float(amount)

    if amount >  balance:
        raise ValueError("insufficient funds. ")
    
    balance -= amount
    print("withdraw successful. new balance: ₦", balance)
except ValueError as e:
    print("error:",e)

    
except Exception as e:
    print("unexpected error:",e)

finally:
    print("transaction session closed")


# If user enters 2000
# Withdrawal successful. New balance: ₦ 3000.0
# Transaction session closed.

# if user enters 6000

# - Error: Insufficient funds.
# - Transaction session closed.

#  if user enters abc
#  Error: could not convert string to float: 'abc'
#  Transaction session closed.


#  Semantic Errors

# The code runs without crashing, but the output is logically wrong.

# - Hardest to detect because the interpreter sees no error.
# - Semantic errors are mostly logic mistakes, so subtypes are based on how the logic is wrong.
# - Note that semantic errors are not officially exceptions in Python, but they are real mistakes programmers make when the logic is wrong.

# Common Subtypes of Semantic Errors

# wrong condition in logic
age =  18
if age > 18:
    print("Eligible to vote")
else: 
    print("not eligible")



    # wrong formula /computation
    length = 10
    width = 5
    area = length + width
    print("Area", area)

# wrong variable usage
marks = [70 , 80, 90]
total = marks[0] * marks[1] * marks[2]
print("total:", total)