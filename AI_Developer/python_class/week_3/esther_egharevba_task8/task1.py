# collecting users first number and second number

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# print(f"{num1}=={num2}: {num1 == num2}")
#  # output : false   if user enter two diiferent numbers the output will be false.


# print(f"{num1} != {num2}: {num1 != num2}")
# # output is true: because num1 is not equal to num2

# print(f"{num1} > {num2}: {num1 != num2}")
# # output is true  :num1 is not greater than num2 and num1 is not equal to num2 

# print(f"{num1} < {num2}: {num1 != num2}")
# output is true  :num1 is less than num2 and num1 is not equal to num2



# cenarios
# 1. admission Eligibility
# 2. student grading
# 3.  check people that are of age for retieredment age

# student grading
# collecting student  name and thrid term result
student_name = input("Eenter name: ")
student_score = int(input("enter your score: "))
Eligible_student = (student_score >= 60 )
print(f"student:{student_name}\nstudent scores:{student_score}\n{Eligible_student} ")
