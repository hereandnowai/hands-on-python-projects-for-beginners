import random
import os

# Global game state variables
secret_word = ""
display_word = ""
chances_remaining = 0
guessed_letters = set()

def get_random_word_from_wordlist():
    wordlist_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'hangman_wordlist.txt'))
    with open(wordlist_path, 'r') as file:
        words = [word.strip().lower() for word in file if word.strip()]
    return random.choice(words)

def get_hangman_drawing(chances):
    stages = [
        """
  +---+
      |
      |
      |
      |
      |
=========
        """,
        """
  +---+
  |   |
      |
      |
      |
      |
=========
        """,
        """
  +---+
  |   |
  O   |
      |
      |
      |
=========
        """,
        """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
        """,
        """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
        """,
        """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
        """,
        """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
        """
    ]
    return stages[7 - chances] # 7 chances initially, so 7-chances gives index

def initialize_game():
    global secret_word, display_word, chances_remaining, guessed_letters
    secret_word = get_random_word_from_wordlist()
    display_word = "_" * len(secret_word)
    chances_remaining = 7
    guessed_letters = set()
    return display_word, chances_remaining, get_hangman_drawing(chances_remaining), "Guess a letter!"

def process_guess(character):
    global secret_word, display_word, chances_remaining, guessed_letters

    message = ""
    if not character.isalpha() or len(character) != 1:
        message = "Please enter a single alphabet only."
    elif character in guessed_letters:
        message = f"You already guessed '{character}'. Try another letter."
    else:
        guessed_letters.add(character)
        if character in secret_word:
            new_display = list(display_word)
            for i, char in enumerate(secret_word):
                if char == character:
                    new_display[i] = char
            display_word = "".join(new_display)
            message = f"Good guess! '{character}' is in the word."
        else:
            chances_remaining -= 1
            message = f"Sorry, '{character}' is not in the word."

    # Check game status
    if "_" not in display_word:
        message = f"You won! The word was '{secret_word}'."
        # Reset game for next round
        display_word, chances_remaining, hangman_drawing, _ = initialize_game()
        return display_word, chances_remaining, hangman_drawing, message
    elif chances_remaining == 0:
        message = f"You lost! The word was '{secret_word}'."
        # Reset game for next round
        display_word, chances_remaining, hangman_drawing, _ = initialize_game()
        return display_word, chances_remaining, hangman_drawing, message

    return display_word, chances_remaining, get_hangman_drawing(chances_remaining), message


if __name__ == "__main__":
    print("===== Welcome to Hangman Game =====")
    current_display_word, current_chances, current_drawing, current_message = initialize_game()
    print(current_message)

    while True:
        print("\n=== Guess the word ===")
        print(current_display_word)
        print(f"Chances left: {current_chances}")
        print(current_drawing)
        
        if "You won!" in current_message or "You lost!" in current_message:
            print(current_message)
            play_again = input("Do you want to play again? (y/n): ")
            if play_again.lower() == 'y':
                current_display_word, current_chances, current_drawing, current_message = initialize_game()
                print("Starting a new game...")
                continue
            else:
                print("Exiting...")
                break

        character = input("Enter the character you think the word may have: ").lower()
        current_display_word, current_chances, current_drawing, current_message = process_guess(character)
        print(current_message)
