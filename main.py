import random

secret = random.randint(1, 30)
guess = None

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))

    if guess == secret:
        print(f"You've guessed it - congratulations! It's number {secret}.")
        break

    hint = None
    if guess > secret:
        hint = "smaller"
    else:
        hint = "bigger"

    print(f"Your guess is not correct... try something {hint}")
