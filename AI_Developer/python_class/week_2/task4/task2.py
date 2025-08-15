# created an empty list
shopping_list = []
# asking user to enter shopping items
shopping_item1 = input("enter your shopping item: ")
shopping_item2 = input("enter your shopping item: ")
shopping_item3 = input("enter your shopping item: ")
shopping_list.append(shopping_item1)
shopping_list.append(shopping_item2)
shopping_list.append(shopping_item3)
print(", ".join(shopping_list))