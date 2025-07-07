# --- Global Game State ---
# The board is represented as a 2D list (a list of lists).
board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
X = 'X'
O = 'O'
current_player = X
game_over = False

def get_board_display():
    # 1. Create a formatted string representing the current board state.
    #    Use f-strings to place board elements in a grid layout.
    #    Example line: f" {board[0][0]} | {board[0][1]} | {board[0][2]}"
    # 2. Return the formatted string.
    pass # Remove this line and add your code here

def reset_game():
    # 3. Use the `global` keyword to modify the global variables.
    # 4. Reset the `board` to its initial state with numbers 1-9.
    # 5. Reset `current_player` to 'X'.
    # 6. Reset `game_over` to False.
    # 7. Return the initial board display and a starting message.
    pass # Remove this line and add your code here

def update_board_state(character, position):
    # 8. Calculate the `row` and `column` from the `position` (1-9).
    #    - row = (position - 1) // 3
    #    - column = (position - 1) % 3
    # 9. Update the `board` at the calculated row and column with the `character` ('X' or 'O').
    pass # Remove this line and add your code here

def check_win_condition():
    # 10. Check all 8 win conditions:
    #     a. 3 rows (e.g., `board[0][0] == board[0][1] == board[0][2]`)
    #     b. 3 columns (e.g., `board[0][0] == board[1][0] == board[2][0]`)
    #     c. 2 diagonals
    # 11. If any condition is met, return `True`. Otherwise, return `False`.
    pass # Remove this line and add your code here

def check_draw_condition():
    # 12. Loop through every cell on the board.
    # 13. If you find any cell that is still a number (not 'X' or 'O'),
    #     it's not a draw yet, so return `False`.
    # 14. If the loop completes without finding any numbers, it's a draw. Return `True`.
    pass # Remove this line and add your code here

def play_move(position):
    # 15. Use the `global` keyword for `current_player` and `game_over`.
    # 16. Check if the chosen `position` is already taken ('X' or 'O').
    #     If so, return the current board and an error message.
    # 17. If the move is valid, call `update_board_state()`.
    # 18. Check for a win by calling `check_win_condition()`.
    #     If true, set `game_over = True` and return the board and a win message.
    # 19. Check for a draw by calling `check_draw_condition()`.
    #     If true, set `game_over = True` and return the board and a draw message.
    # 20. If the game is not over, switch the `current_player` ('X' to 'O' or 'O' to 'X').
    # 21. Return the updated board and a message for the next player's turn.
    pass # Remove this line and add your code here

if __name__ == "__main__":
    # 22. Print a welcome message and call `reset_game()`.
    # 23. Start a `while not game_over:` loop.
    # 24. Inside the loop, print the board and the current player's turn message.
    # 25. Get the `position` choice from the user.
    #     - Use a `try-except` block to handle non-numeric input.
    # 26. Call `play_move()` with the user's choice.
    # 27. Print the message returned by `play_move()`.
    # 28. If `game_over` becomes true, print the final board and break the loop.
    pass # Remove this line and implement the CLI.
