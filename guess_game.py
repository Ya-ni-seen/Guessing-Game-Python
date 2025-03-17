import random

def number_guessing_game():
    """A simple number guessing game."""
    print("🎲 Welcome to the Number Guessing Game!")
    
    while True:
        print("\nI am thinking of a number between 1 and 100.")
        number = random.randint(1, 100)  # The computer selects a random number
        attempts = 0

        while True:
            try:
                guess = int(input("Enter your guess: "))
                attempts += 1

                if guess < number:
                    print("🔽 Too low! Try again.")
                elif guess > number:
                    print("🔼 Too high! Try again.")
                else:
                    print(f"🎉 Correct! You guessed the number in {attempts} attempts.")
                    break
            except ValueError:
                print("⚠️ Please enter a valid number.")

        # Play again or exit options
        play_again = input("\nDo you want to play again? (y/n): ").strip().lower()
        if play_again != "y":
            print("👋 Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    number_guessing_game()
