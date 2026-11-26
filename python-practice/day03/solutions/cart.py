prices = []

while True:
    price = float(input("Price (0 to finish): "))
    if price == 0:
        break
    prices.append(price)

print(f"Items: {len(prices)}")
print(f"Total: {sum(prices):.2f}")
