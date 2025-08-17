#  Contact Quick Lookup
# storing three names and their phone number in a tuple
name = ("victor","esther","favour")
phone_no = ("08045328911", "08025328012", "08015308011")


#   combining name and phone number.
joint = list(zip(name, phone_no))

# creating an empty dictionary
dictionary = {}
dictionary[joint[0][0]] = joint[0][1]
dictionary[joint[1][0]] = joint[1][1]
dictionary[joint[2][0]] = joint[2][1]
users = input(f"Enter a name {", ".join(dictionary.keys())}: ").lower()


# Useing `.get()` for safe retrieval.
print(dictionary.get(users))

