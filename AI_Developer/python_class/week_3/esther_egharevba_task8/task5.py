# creating a dictionary called stored
store = { "Book":10,"Pen":20,"Bag":5,}

# asking users to enter what they want to buy and the quantity
items_to_buy =input(f"Enter an item that you want to buy\n available items: {" ,".join (store.keys())} :").title()
quantity = int(input(f"Enter your quantity\navailable quantity: {store[items_to_buy]} :"))
print("Before purchase",store)
store[items_to_buy] -= quantity
print("After purchase:", store)