import random

lowest_number_to_guess = 1
highest_number_to_guess = 20
secret = random.randint(lowest_number_to_guess, highest_number_to_guess)
guess = None
attempts = 0
secret_number_file = "secret_number_best_score.txt"

with open(secret_number_file, "r") as attempts_file:
    attempts_from_file = int(attempts_file.read())
    print(f"Best score: {attempts_from_file} attempts.")

while True:
    guess = int(input(f"Guess the secret number (between {lowest_number_to_guess} and {highest_number_to_guess}): "))
    attempts += 1

    # Check guess within boundaries
    if guess < lowest_number_to_guess or guess > highest_number_to_guess:
        print(f"Number {guess} is not between {lowest_number_to_guess} and {highest_number_to_guess}.")
        continue

    # Correct answer
    if guess == secret:
        print(f"You've guessed it - congratulations! It's number {secret}.")
        print(f"Number of attempts: {attempts}")
        if attempts < attempts_from_file:
            with open(secret_number_file, "w") as attempts_file:
                attempts_file.write(str(attempts))
        break

    # Wrong answer
    hint = None
    if guess > secret:
        hint = "smaller"
    else:
        hint = "bigger"

    print(f"Your guess is not correct... try something {hint}")
