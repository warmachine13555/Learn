prices = {
    "Banana": 1.50,
    "Apple": 0.75,
    "Orange": 0.90,
    # Add more items and their prices if needed
}


item_name = "Apple"
item_price = prices.get(item_name)  # Retrieve the price using the item name as the key


if item_price == 1.50:
    print("The price of Banana is 1.50.")
else:
    print("The price of Banana is not 1.50.")
