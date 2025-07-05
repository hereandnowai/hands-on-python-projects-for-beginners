import random

ROCK = 'rock'
PAPER = 'paper'
SCISSOR = 'scissor'
choices = [ROCK, PAPER, SCISSOR]

# Define winning and losing conditions more explicitly
winning_conditions = {
    ROCK: SCISSOR,
    PAPER: ROCK,
    SCISSOR: PAPER
}

def get_computer_move():
    return random.choice(choices)

def play_round(user_move_str):
    user_move = user_move_str.lower()
    if user_move not in choices:
        return "Invalid move. Please choose Rock, Paper, or Scissor."

    computer_move = get_computer_move()

    result_message = f"You chose: {user_move.capitalize()}\nComputer chose: {computer_move.capitalize()}\n"

    if user_move == computer_move:
        result_message += "It's a Tie !!!"
    elif winning_conditions[user_move] == computer_move:
        result_message += "You Won !!!"
    else:
        result_message += "Computer Won !!!"
    
    return result_message

# --- Command-line Interface (for direct execution) ---
if __name__ == "__main__":
    print("===== Welcome to Rock, Paper And Scissor Game =====")
    while True:
        choice = input("Do you wanna play (y/n): ").strip().lower()
        if choice == 'y':
            while True:
                move = input("Select a move (rock/paper/scissor): ").strip().lower()
                if move in choices:
                    print(play_round(move))
                    break
                else:
                    print("Invalid input...please try again")
        elif choice == 'n':
            print("Exiting... Thanks for playing!")
            break
        else:
            print("Invalid input...please try again")
        print()