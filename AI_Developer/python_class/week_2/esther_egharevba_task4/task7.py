# Creating a list of five cities.
list_city = ["ikeja", "lekki", "benin", "warri","abeokuta"]

# Replace the third city with a new one (entered by the user)
user = input("please enter a city: ")
list_city[2] = user

# Removing the last city
list_city.pop()

# Add a new city to the beginning of the list.
list_city.insert(0, "uyo")

# Print the updated list.
print(list_city)