# collecting users name and age
student= {}
user_name = input("enter your name: ")
user_age =int(input("enter your age: "))
student = dict(name = user_name, age = user_age) 

score =[70, 80, 90]
print(student)
average_score = sum(score)/len(score)
# print(average_score)
passed_student = average_score >= 50
result = passed_student
# print("passed:" ,passed_student)
teenager = (user_age >=13) and (user_age <=19)
print(f"Student Record:\nName{user_name}\nAge:{user_age}\nscore:{score}\npassed:{passed_student}")
# using comparison operator to check if the student has pass
<<<<<<< HEAD
 
# average_scores = sum(score)/len(score)
# student=dict()
=======
score =[70, 85, 90] 
average_scores = sum(score)/len(score)
student.update(name=user_name, age = user_age)
student_that_pass = average_scores >= 50
student.update({"name": "user_name", "age": "user_age", "score":"score"})
# student["passed"] = average_scores(True/False)
teenager = user_age >= 13 and user_age <= 18

print(f"student name:\n{student["user_name"]}\nage{student["user_age"]} \nscore:\n{student["score"]} passed {student['passed']}/n teenager:{student["teenager"]}")
>>>>>>> 3d97c32826e406e50b111679655473949135039d
