class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        print(f"{self.name}: {self.price:.2f}")


products = [
    Product("Keyboard", 25.5),
    Product("Mouse", 12),
    Product("Monitor", 140),
]

total = 0
for product in products:
    product.show()
    total += product.price

print(f"Total: {total:.2f}")
