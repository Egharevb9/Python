# python operators

# operators are special symbols in python that perform  operations on variables and values. Here we will forcus on;
# . comparison operators
# . Assignment operators 
# . Logical operators

# comparison operators
# . comparison operators are used to compare two values . the result is always True or False.

# operators        example             meaning
# ==                5==5                equals To
# !=                5 != 3              not equal to
# >                 7 > 4               greater than
# <                 3 < 8               less than
# >=               6 >= 6              greater than or equal to 
# <=               2 <= 5              less than or equal to 



a = 10
b = 20
print(a==b)

print(a != b)

print(a > b)

print(a < b)


print(a >= 10)

print(a <= 25)

# using case example - student exam result
score = 75

print(score >= 50)
print(score < 50)
print(score == 100)

# assignment operators 
# assignment operators are used to assign values to  variables . they can also  combine  an operation with assignment so instead of writing x =  x + 5, we can write x += 5.
# operators            example           meaning 
# =                   x =  10            assign value 10 to x
# +=                  x +=  5           adds 5 to x (x = x 5)
# -=                  x -=  3          subtracts 3 from x
# *=                  x *=  2          multiply  x by 2
# /=                  x /=  4          divides x by 4
# %=                  x %=  3           stores remaindder after division
# **=                 x **=  2           Raises x to the  power of 2
# //=                 x //=  2          floor divides x by 2



x = 10 
print("initial value:",x )

x +=5
print(" Aftter x += 5:",x )

x -= 2
print("After x -= 2:",x )

x *=3
print("After x *= 3:",x )

x /= 4
print(" After x *= 4:",x )

x %= 3
print("After x %= 3:",x )

x = 4
x **= 2 
print("After **= 2:",x )

x //= 3 
print("After x //= 3:",x )
# use case example:
# define variable
balance = 1000
deposit = 200
withdraw = 150

balance += deposit
balance -= withdraw

print("updated balance:", balance)
# print("initial value:",x )
# print("initial value:",x )


# logical operators
# logical operators are used to combine conditional statements, they work with boolen values (True or False).
# operators         example                      meaning
# And              x  > 5 and x < 15             True if both  conditions are true
# or              x  < 5 or x < 20             True if at least  one conditions is true
# not              not(x ==10)             True if the conditions is false

x = 10
y = 20


# and operator
print(x > 5 and y > 15)

# or operator
print(x > 5 or y > 15)

# not operator
print(not (x==10))

# use  case exampel1 - scholarship Eligibility
# define variables
age = 17
score = 85

# must be younger than 18 and score above 80
eligible = (age < 18) and (score > 80)
print("scholarship Eligible:", eligible)


# use case example2 - event Access
age =  22
has_ticket = False

can_enter = (age >= 18) and (has_ticket or age < 25)
print("Access granted:", can_enter)
