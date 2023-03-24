class NotEnoughMoneyError(Exception):
    pass


class PurchaseLimitExceededError(Exception):
    pass


shop_items = {
    'Fruit Basket': 10,
    'Set of Harry Potter Books': 50,
    'TV': 150
}

available_money = 100

print("Welcome to our shop!")
print("Here are the items we have on sale today:")
for item, price in shop_items.items():
    print(f"{item}: £{price}")

purchase_limit = 3
purchased_items = []
while len(purchased_items) < purchase_limit:
    item_choice = input("Enter the item you want to purchase (or 'exit' to leave the shop): ")

    if item_choice not in shop_items and item_choice != 'exit':
        raise ValueError("Invalid item entered")

    if item_choice == 'exit':
        print("Thanks for visiting our shop!")
        break

    item_price = shop_items[item_choice]
    if item_price > available_money:
        print(f"You don't have enough money to purchase {item_choice}")
        additional_money = input("Do you have more money? If so, how much? ")
        try:
            additional_money = int(additional_money)
            available_money += additional_money
        except ValueError:
            print("Invalid amount entered, please try again.")
            continue

    try:
        if len(purchased_items) >= purchase_limit:
            raise PurchaseLimitExceededError("You have reached your purchase limit!")
        elif item_price > available_money:
            raise NotEnoughMoneyError("You don't have enough money to purchase this item")
        else:
            purchased_items.append(item_choice)
            available_money -= item_price
            print(f"Here's your {item_choice}!")
    except NotEnoughMoneyError as e:
        print(e)
    except PurchaseLimitExceededError as e:
        print(e)
        break

if purchased_items:
    print("Here are the items you purchased:")
    for item in purchased_items:
        print(item)
