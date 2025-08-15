# collects the names of people attending a seminar
attending_seminar = set()

attending_seminar. add("victoria")
attending_seminar. add("opyemi")
attending_seminar. add("victor")
print("people that attended the seminal:",attending_seminar)

name = "victoria"
if name in attending_seminar:
    print(f"{name} attended the seminar")
else:
    print(f"{name} did not attend the event")