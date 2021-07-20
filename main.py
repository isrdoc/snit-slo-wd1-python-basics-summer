secret = 12
guess = None

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret) + ".")
        break

    print("Sorry, your guess is not correct... The secret number is not " + str(guess))
