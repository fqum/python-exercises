prices = [12.5, 30, 8.75, 45, 20]

total = 0
highest = prices[0]

for price in prices:
    total += price
    if price > highest:
        highest = price

average = total / len(prices)

print(f"Total: {total:.2f}")
print(f"Highest: {highest:.2f}")
print(f"Average: {average:.2f}")
