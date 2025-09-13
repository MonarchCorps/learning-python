print("Welcome to the word guessing game!\n")

secret_word = "temple"
user_guess = ""
guess_count = 0

hint = "_ " * len(secret_word)
print("Your hint is:", hint.strip(), "\n")

while user_guess != secret_word:
    user_guess = input("What is your guess? ").lower()
    guess_count += 1

    if len(user_guess) != len(secret_word):
        print("Sorry, the guess must have the same number of letters as the secret word.\n")

    elif user_guess == secret_word:
        print("\nCongratulations! You guessed it!")
        print(f"It took you {guess_count} guesses.")

    else:
        hint = ""
        for i in range(len(secret_word)):
            if user_guess[i] == secret_word[i]:
                hint += user_guess[i].upper() + " "
            elif user_guess[i] in secret_word:
                hint += user_guess[i].lower() + " "
            else:
                hint += "_ "

        print("Your hint is:", hint.strip(), "\n")
