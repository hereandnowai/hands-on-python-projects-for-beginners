import random
import os

# --- Global Game State Variables ---
# It's often helpful to have these at the top level for a simple game.
secret_word = ""
display_word = ""
chances_remaining = 0
guessed_letters = set()

def get_random_word_from_wordlist():
    # 1. Construct the full path to 'hangman_wordlist.txt'.
    #    - `os.path.dirname(__file__)` gets the directory of the current script.
    #    - `os.path.join()` combines paths safely.
    # 2. Open and read the file.
    # 3. Create a list of words, ensuring they are clean (stripped of whitespace, lowercase).
    # 4. Use `random.choice()` to select and return one word from the list.
    pass # Remove this line and add your code here

def get_hangman_drawing(chances):
    # 5. Create a list `stages` containing the 7 hangman drawings as multi-line strings.
    #    Start with the empty gallows and end with the full hangman.
    # 6. The index into the `stages` list will depend on `chances`.
    #    If you have 7 chances, you might use `stages[7 - chances]` to get the right drawing.
    # 7. Return the selected stage.
    pass # Remove this line and add your code here

def initialize_game():
    # 8. Use the `global` keyword for each variable you intend to modify.
    #    (secret_word, display_word, etc.)
    # 9. Set `secret_word` by calling `get_random_word_from_wordlist()`.
    # 10. Set `display_word` to a string of underscores `_` matching the length of the secret word.
    # 11. Set `chances_remaining` to 7.
    # 12. Reset `guessed_letters` to an empty set.
    # 13. Return the initial game state: display_word, chances, drawing, and a starting message.
    pass # Remove this line and add your code here

def process_guess(character):
    # 14. Use the `global` keyword for variables you'll modify.
    # 15. Validate the input: check if it's a single alphabet character.
    # 16. Check if the letter has already been guessed.
    # 17. If it's a new, valid guess:
    #     a. Add it to `guessed_letters`.
    #     b. If the letter is in `secret_word`:
    #        - Update `display_word` to reveal the letter.
    #        - Set a success message.
    #     c. If the letter is not in `secret_word`:
    #        - Decrement `chances_remaining`.
    #        - Set a failure message.
    # 18. Check for win/loss conditions:
    #     - If `_` is no longer in `display_word`, the player won.
    #     - If `chances_remaining` is 0, the player lost.
    #     - If the game is over, set an appropriate message and consider calling `initialize_game()` to reset for a potential new round.
    # 19. Return the updated game state (display_word, chances, drawing, message).
    pass # Remove this line and add your code here

if __name__ == "__main__":
    # 20. Set up the initial game state by calling `initialize_game()`.
    # 21. Start a `while True` loop for the game.
    # 22. Inside the loop, print the current `display_word`, `chances_remaining`, and the hangman `drawing`.
    # 23. Get a `character` guess from the user.
    # 24. Call `process_guess()` to update the game state.
    # 25. Print the message returned from `process_guess()`.
    # 26. If the game is won or lost, ask the user if they want to play again.
    #     - If yes, call `initialize_game()` and `continue`.
    #     - If no, `break` the loop.
    pass # Remove this line and implement the CLI.
