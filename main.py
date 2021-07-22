import json
import random

lowest_number_to_guess = 1
highest_number_to_guess = 20
secret = random.randint(lowest_number_to_guess, highest_number_to_guess)
guess = None
attempts = 0
best_score_file_name = "secret_number_best_score.txt"
attempts_file_name = "secret_number_attempts.json"

# Print current best score
with open(best_score_file_name, "r") as best_score_file:
    best_score = int(best_score_file.read())
    print(f"Best score: {best_score} attempts.")

# Print all attempts
with open(attempts_file_name, "r") as attempts_file:
    logged_attempts = json.loads(attempts_file.read())
    print(f"All games attempts: {logged_attempts}.")

# Print three best scores
logged_attempts.sort()
print(f"Three best scores are: {logged_attempts[:3]}.")

while True:
    # User guesses the secret number
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
        if attempts < best_score:
            with open(best_score_file_name, "w") as best_score_file:
                best_score_file.write(str(attempts))

        with open(attempts_file_name, "w") as attempts_file:
            logged_attempts.append(attempts)
            next_log_of_attempts_str = json.dumps(logged_attempts)

            attempts_file.write(next_log_of_attempts_str)
        break

    # Wrong answer
    hint = None
    if guess > secret:
        hint = "smaller"
    else:
        hint = "bigger"

    print(f"Your guess is not correct... try something {hint}")
