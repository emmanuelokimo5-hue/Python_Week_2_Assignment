# This program calculates the total cost of items purchased.

price = float(input("Enter the price of one item: "))
quantity = int(input("Enter the quantity you want: "))

total = price * quantity

print(f"{quantity} items at {price:.2f} each = {total:.2f}")
Enter the price of one item: 50
Enter the quantity you want: 3
3 items at 50.00 each = 150.00