import random

# --- Constants ---
# Using constants makes the code more readable and less prone to typos.
ROCK = 'rock'
PAPER = 'paper'
SCISSOR = 'scissor'
choices = [ROCK, PAPER, SCISSOR]

# --- Winning Conditions ---
# A dictionary is a great way to define the winning logic.
# The key is the move, and the value is the move it defeats.
winning_conditions = {
    PAPER: ROCK,
    ROCK: SCISSOR,
    SCISSOR: PAPER
}

def get_computer_move():
    # 1. Use `random.choice()` to select a move from the `choices` list.
    # 2. Return the selected move.
    pass # Remove this line and add your code here

def play_round(user_move_str):
    # 3. Sanitize the user's input by converting it to lowercase.
    # 4. Validate the input: check if `user_move` is in the `choices` list.
    #    If not, return an error message.

    # 5. Get the computer's move by calling `get_computer_move()`.

    # 6. Start building a `result_message` string.
    #    - First, announce what the user and computer chose.

    # 7. Determine the winner:
    #    a. If `user_move` is the same as `computer_move`, it's a tie.
    #    b. Use the `winning_conditions` dictionary to check if the user won.
    #       - `if winning_conditions[user_move] == computer_move:`
    #    c. If neither of the above is true, the computer must have won.

    # 8. Append the outcome (win, lose, or tie) to the `result_message`.

    # 9. Return the final `result_message`.
    pass # Remove this line and add your code here

if __name__ == "__main__":
    # 10. Print a welcome message.
    # 11. Start a `while True` loop for the main game menu.
        # 12. Ask the user if they want to play (y/n).
        # 13. If 'y', start another `while True` loop for the current round.
            # 14. Get the user's move (rock, paper, or scissor).
            # 15. Validate the move. If it's valid:
            #     a. Call `play_round()` with the move.
            #     b. Print the result.
            #     c. `break` the inner loop to return to the main menu.
            # 16. If the move is invalid, print an error and let the inner loop continue.
        # 17. If 'n', print an exit message and `break` the main loop.
        # 18. Handle invalid 'y'/'n' input.
    pass # Remove this line and implement the CLI.
