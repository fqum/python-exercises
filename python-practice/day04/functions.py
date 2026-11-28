def add(a, b):
    return a + b


def is_even(n):
    return n % 2 == 0


def final_price(price, quantity, tax=0.15):
    return price * quantity * (1 + tax)


print(add(2, 3))
print(is_even(4), is_even(7))
print(f"{final_price(20, 3):.2f}")
print(f"{final_price(20, 3, tax=0):.2f}")
