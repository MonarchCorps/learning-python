menu = {
    "Pizza": 3.00,
    "Nachos": 4.50,
    "Popcorn": 5.00,
    "Fries": 6.70,
    "Chips": 1.50,
    "Suya": 2.30
}

cart = []
total = 0

print("------------ MENU -----------")

for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")

print("------------------------------")

while True:
    food = input("Select and item (q to quit): ").capitalize()
    if food.lower() == "q":
        break
    elif menu.get(food) is not None:
        if cart.__contains__(food):
            print(f"{food} is already in the cart.")
        else:
            cart.append(food)

print("------------ YOUR ORDER -------------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: ${total:.2f}")