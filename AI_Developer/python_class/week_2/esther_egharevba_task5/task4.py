# collecting user detailes
first_name = input("pls enter your full name: ")
Age = int(input("pls enter your age: "))
favourite_color = input("pls enter your favourite color: ")
home_town = input("pls enter your home town: ")
store = first_name, Age, home_town
print(store)
result = tuple(store)
print(f"my name is {first_name}\n i'm {Age} years old\n my favourite color is {favourite_color}\n my home town is {home_town}")

