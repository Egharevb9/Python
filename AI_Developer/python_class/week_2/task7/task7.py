# collecting users detail
student ={}
name_name = input("Please enter your name: ").title().strip()
age = int(input("Please enter your age: "))
gender = input("Please enter your gender: ").strip()
course = input("Please enter your course \"seperated by space\": ")
# response = dict (name_name, age, gender, course)
student["name"] = name_name
student["age"] = age
student["courses"] = course.split(" ")
print(student)
print("\n----Student Bio-Data----")
print(f"name:\t\t{student['name']}")
print(f"age:\t\t{student['age']}")
print(f"courses:\t{student['courses']}")


