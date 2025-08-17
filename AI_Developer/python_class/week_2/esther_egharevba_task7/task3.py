days_of_week = ("Sunday", "Monday","Tuesday","wednesday","Thursday","Friday","Saturday")
print("Seletct three activities days of the week using (1 - 7)")
days_of_activities = [
    days_of_week[int(input("Enter the first day (1 - 7): ")) - 1],
    days_of_week[int(input("Enter the second day (1 - 7): ")) - 1],
    days_of_week[int(input("Enter the third day (1 - 7): ")) - 1],
]

activities = [
    input(f"Enter your activity for {days_of_activities[0]}: "),
    input(f"Enter your activity for {days_of_activities[1]}: "),
    input(f"Enter your activity for {days_of_activities[2]}: ")
]
result = {day: activity for day, activity in zip(days_of_week, activities)}
print(result)


