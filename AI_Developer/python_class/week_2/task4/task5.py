# created empty list for student names and empty list for student_score
student_names = []
student_score = []

# asking user for student name
name1 = input(" enter your name: ")
name2 = input(" enter your name: ")
name3 = input(" enter your name: ")


# collecting student scores
scores1 = int(input("please enter your scores: "))
scores2 = int(input("please enter your scores: "))
scores3 = int(input("please enter your scores: "))

# adding users input into te empty list called student_names
student_names.append(name1)
student_names.append(name2)
student_names.append(name3)

# adding users input into te empty list called student_names
student_score.append(scores1)
student_score.append(scores2)
student_score.append(scores3)


print(name1,   scores1 )
print(name2,   scores2 )
print(name3,   scores3 )
