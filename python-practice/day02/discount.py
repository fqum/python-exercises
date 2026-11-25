price = float(input("Price: "))
quantity = int(input("Quantity: "))

subtotal = price * quantity

if subtotal > 500:
    subtotal = subtotal * 0.9
    print("Discount applied")
else:
    print("No discount")

total = subtotal * 1.15
print(f"Final: {total:.2f}")
