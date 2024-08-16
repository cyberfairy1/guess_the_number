from random import randint
from guess_number_art import logo

EASY_BREEZY_TURNS = 10
TOUGH_NUT_TURNS = 5

# Function to check the user's guess against the actual answer.
def evaluate_guess(player_guess, secret_number, remaining_attempts):
    """Compares player's guess with the secret number. Returns the updated attempts left."""
    if player_guess > secret_number:
        print("Whoa, that's too high! Aim lower.")
        return remaining_attempts - 1
    elif player_guess < secret_number:
        print("Oof, that's too low! Try aiming a bit higher.")
        return remaining_attempts - 1
    else:
        print(f"Boom! Nailed it. The magic number was {secret_number}.")

# Function to set the difficulty level.
def choose_difficulty():
    difficulty = input("Pick your poison: Type 'easy-peasy' for a chill vibe or 'hardcore' for a real challenge: ")
    if difficulty == "easy-peasy":
        return EASY_BREEZY_TURNS
    else:
        return TOUGH_NUT_TURNS

def number_guessing_game():
    print(logo)
    # Selecting a random number between 1 and 100.
    print("🎉 Welcome to the Epic Number Guessing Showdown! 🎉")
    print("I've got a number between 1 and 100 in mind. Can you guess it? 🤔")
    secret_number = randint(1, 100)

    attempts_left = choose_difficulty()
    # Start the guessing loop until the correct number is found.
    player_guess = 0
    while player_guess != secret_number:
        print(f"You're holding on with {attempts_left} guesses left. Time's ticking! ⏳")

        # Let the user make a guess.
        player_guess = int(input("Take a wild guess: "))

        # Check the guess and update the number of attempts left.
        attempts_left = evaluate_guess(player_guess, secret_number, attempts_left)
        if attempts_left == 0:
            print(f"Out of guesses! The correct number was {secret_number}. Better luck next time! 😅")
            return
        elif player_guess != secret_number:
            print("Not quite there. Give it another shot! 🔄")

number_guessing_game()

