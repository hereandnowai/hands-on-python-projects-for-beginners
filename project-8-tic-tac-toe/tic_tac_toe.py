board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
X = 'X'
O = 'O'
current_player = X
game_over = False

def get_board_display():
    display = ""
    display += f" {board[0][0]} | {board[0][1]} | {board[0][2]}\n"
    display += "-----------\n"
    display += f" {board[1][0]} | {board[1][1]} | {board[1][2]}\n"
    display += "-----------\n"
    display += f" {board[2][0]} | {board[2][1]} | {board[2][2]}\n"
    return display

def reset_game():
    global board, current_player, game_over
    board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    current_player = X
    game_over = False
    return get_board_display(), "Player X's turn."

def update_board_state(character, position):
    row = (position-1)//3
    column = (position-1)%3
    board[row][column] = character

def check_win_condition():
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            return True
    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        return True
    if board[0][2] == board[1][1] == board[2][0]:
        return True
    return False

def check_draw_condition():
    for row in board:
        for cell in row:
            if cell != X and cell != O:
                return False
    return True

def play_move(position):
    global current_player, game_over

    if game_over:
        return get_board_display(), "Game over! Click 'Reset Game' to play again."

    row = (position-1)//3
    column = (position-1)%3

    if board[row][column] == X or board[row][column] == O:
        return get_board_display(), "Position already occupied. Choose another."

    update_board_state(current_player, position)

    if check_win_condition():
        game_over = True
        return get_board_display(), f"Player {current_player} wins!"
    elif check_draw_condition():
        game_over = True
        return get_board_display(), "It's a draw!"
    else:
        current_player = O if current_player == X else X
        return get_board_display(), f"Player {current_player}'s turn."


# --- Command-line Interface (for direct execution) ---
if __name__ == "__main__":
    print("===== Welcome to Tic Tac Toe Game =====")
    reset_game()
    while not game_over:
        board_display, message = get_board_display(), f"Player {current_player}'s turn."
        print(board_display)
        print(message)
        try:
            choice = int(input(f"Player {current_player}, enter your position: "))
            if choice < 1 or choice > 9:
                print("Invalid input...please try again.")
                continue
            
            board_display, message = play_move(choice)
            print(message)
            if game_over:
                print(board_display)
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            print(f"An error occurred: {e}")