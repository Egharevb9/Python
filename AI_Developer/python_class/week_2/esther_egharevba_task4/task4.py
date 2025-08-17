# collecting names from user 
names = input(" enter name \"separated by spaces\": ").lower()
names_list = names.split(" ")
names_list.sort()
print(names_list)
for name in range(len(names_list)):
    print(names_list[name])
print("second method")
for name in names_list:
    print(name)