# collecting  users name ,age and score
name = input(" enter your name: ")
age = int(input("enter your age: "))
score = int(input("enter your test score"))


# seting setting the eligibility
eligibility =  (age < 18 ) and (score > 70)

# printing out the user name ,age and score to check if or she is legible
print(f"candidates: {name}\nage:{age}\nscores:{score}\nEligible: {eligibility} ")


# Fedral government scholarship key ELIGIBILITY
print("\nScholaship enrollment") 
name = input("Enter your name: ")
age = int(input("Enter your age: "))
citizenship = input("Enter your country: ")
Enrollment = input("Are you a full time  undergraduate student in a recongnized nigerian university?\nEnter (yes or no): ").lower()
other_scholarship = input(" Are you currently recieving any others scholarship from an entity in oil and Gas industry, whether national or international? \nEnter (yes or no): ").lower()
academic_qualification = int(input("enter five distinctions (As and Bs) in relevant subjects in your WAEC/WASSCE(MAY/june) exams including English  and mathematics"))
legible =((citizenship =="Nigeria")and (Enrollment =="yes")and(other_scholarship =="no")and(academic_qualification >= 5))
print(f"\nname: {name}\nage:{age}\ncountry:{citizenship}\nundergraduate:{Enrollment}\nother schorlaship:{other_scholarship}\nacademic qualification:{academic_qualification}\neligibility{legible}")