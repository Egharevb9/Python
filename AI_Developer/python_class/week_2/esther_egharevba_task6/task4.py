# ASKING VOTERS FOR THIER NAMES
voter_name1 = input("please enter your name: ")
voter_name2 = input("please enter your name: ")
voter_name3 = input("please enter your name: ")
names = voter_name1, voter_name2, voter_name3
voter_names = set(names)
print(voter_names)

for names in voter_names:
    print(f"Warning:{voter_names}already exist")
else:
    voter_names.add(voter_names)
    print(f"{voter_names} successfully registered") 