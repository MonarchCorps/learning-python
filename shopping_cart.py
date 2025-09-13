print("Welcome to the Shopping Cart Program!")
actions = ["Add item", "View cart", "Remove item", "Compute total", "Quit"]

items = []
prices = []

action_to_perform = 0
item_to_add = ""
price_to_add = 0
item_to_remove_index = 0
total_price = 0

while action_to_perform != 5:
    print("\nPlease select one of the following: ")

    for i in range(len(actions)):
        print(f"{i + 1}. {actions[i]}")

    action_to_perform = int(input("Please enter an action: "))
    zero_base_action_to_perform = action_to_perform - 1

    if action_to_perform > len(actions) or action_to_perform < 0:
        print("\nSorry, that is not a valid item number.")

    elif zero_base_action_to_perform == 0:
        item_to_add = input("What item would you like to add? ")
        if item_to_add not in items:
            items.append(item_to_add)
            price_to_add = float(input(f"What is the price of '{item_to_add}'? "))
            prices.append(price_to_add)
            print(f"'{item_to_add}' has been added to the cart.")

        else:
            print(f'"{item_to_add}" is already in the cart.')

    elif zero_base_action_to_perform == 1 or zero_base_action_to_perform == 2:
        if len(items) == 0:
            print("Your shopping cart is empty.")
        else:
            print("The contents of the shopping cart are:\n")
            for i in range(len(items)):
                print(f"{i + 1}. {items[i]} - ${prices[i]:.2f}")

            if zero_base_action_to_perform == 2:
                item_to_remove_index = int(input("Which item would you like to remove? "))
                zero_base_item_to_remove = item_to_remove_index - 1

                if item_to_remove_index < 1 or item_to_remove_index > len(items):
                    print("\nSorry, that is not a valid item number.")
                else:
                    items.pop(zero_base_item_to_remove)
                    prices.pop(zero_base_item_to_remove)
                    print("Item removed.")

    elif zero_base_action_to_perform == 3:
        total_price = sum(prices)
        print(f"The total price of the items in the shopping cart is ${total_price:.2f}")
        total_price = 0

    else:
        print("Thank you. Goodbye.")