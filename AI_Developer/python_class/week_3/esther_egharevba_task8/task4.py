student= {}
user_name = input("enter your name: ")
user_age =int(input("enter your age: "))
student = dict(name = user_name, age = user_age) 

# using comparison operator to check if the student has pass
score =[70, 85, 90] 
average_scores = sum(score)/len(score)
student.update(name=user_name, age = user_age)
student_that_pass = average_scores >= 50
student.update({"name": "user_name", "age": "user_age", "score":"score"})
# student["passed"] = average_scores(True/False)
teenager = user_age >= 13 and user_age <= 18

print(f"student name:\n{student["user_name"]}\nage{student["user_age"]} \nscore:\n{student["score"]} passed {student['passed']}/n teenager:{student["teenager"]}")