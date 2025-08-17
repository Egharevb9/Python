# creating an empty dictionary
store_items = {}

lists = ("clothes", "bag" ,"jweries", "shoes" ,"belt")

store_items[lists[0]]= float(input(f"enter price for {lists[0]}: "))
store_items[lists[1]]= float(input(f"enter price for {lists[1]}: "))
store_items[lists[2]]= float(input(f"enter your price for {lists[2]}: "))
store_items[lists[3]]= float(input(f"enter your price for {lists[3]}: "))
store_items[lists[4]]= float(input(f"enter your price for {lists[4]}: "))
print(store_items)

# available items
all_items = store_items.keys()
print(all_items)

updated_items = input("enter the item that you want to update").lower()
print(store_items)
if updated_items in store_items.keys():
    store_items[updated_items] = float(input("enter your price: "))
else:
    print("invalide item")
print(store_items)    
