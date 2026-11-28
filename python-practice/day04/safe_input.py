def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number")


price = get_number("Price: ")
quantity = get_number("Quantity: ")

print(f"Total: {price * quantity:.2f}")
