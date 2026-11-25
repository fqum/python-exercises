price = float(input("Price: "))
quantity = int(input("Quantity: "))

subtotal = price * quantity
total = subtotal * 1.15

print(f"Total with tax: {total:.2f}")
