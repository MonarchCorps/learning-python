child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))
number_of_children = int(input("How many children are there? "))
number_of_adults = int(input("How many adults are there? "))

adults_meal_total = adult_meal_price * number_of_adults
children_meal_total = child_meal_price *  number_of_children

subtotal_meal_price = adults_meal_total + children_meal_total

print(f"\nSubtotal: ${subtotal_meal_price:.2f}\n")

sales_tax_rate = float(input("What is the sales tax rate? "))
sales_tax = (sales_tax_rate / 100) * subtotal_meal_price
total = subtotal_meal_price + sales_tax

print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total: ${total:.2f}\n")

payment_amount = float(input("What is the payment amount? "))
change = payment_amount - total
print(f"Change: ${change:.2f}")