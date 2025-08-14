# collecting users shopping list
shoping_list1 = input("Enter items for your shoping list: ")
shoping_list2 = input("Enter items for your shoping list: ")
shoping_list3 = input("Enter items for your shoping list: ")

# converting users input into a list
result = shoping_list1,shoping_list2, shoping_list3
shop_lists = list(result)
print(shop_lists)

# collecting more items from users
shoping_list4 = input("Enter items for your shoping list: ")
shoping_list5 = input("Enter items for your shoping list: ")

# adding the other items to the other items
shop_lists.append(shoping_list4)
shop_lists.append(shoping_list5)
shop_lists = tuple(shop_lists)
print(" your shoping list items are " ,"|" .join(shop_lists)) 