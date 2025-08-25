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

