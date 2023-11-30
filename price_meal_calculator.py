print("Welcome to the price meal calculator")

child_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of an adult's meal? "))
number_of_children = float(input("How many children are there? "))
number_of_adults = float(input("How many adults are there? "))
sales_tax = float(input("What is the sales tax rate? "))

subtotal_cost = child_meal * number_of_children + adult_meal * number_of_adults

total_cost = round(subtotal_cost + sales_tax, 2)

print()

print(f"Subtotal: ${subtotal_cost}")
print(f"Sales Tax: ${sales_tax}")
print(f"Total: ${round(subtotal_cost + sales_tax, 2)}")

print()

amount = float(input("What is the payment amount? "))
payment_amount = round(amount - total_cost, 2)

print(f"Change: ${payment_amount}")