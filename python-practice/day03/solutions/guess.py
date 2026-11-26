secret = 7
attempts = 0

while True:
    guess = int(input("Guess: "))
    attempts += 1

    if guess == secret:
        print(f"Correct! Attempts: {attempts}")
        break
    elif guess > secret:
        print("Too high")
    else:
        print("Too low")
