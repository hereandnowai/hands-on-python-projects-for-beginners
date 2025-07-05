import random
secret_number = random.randint(0, 9)

def make_guess(user_guess):
    global secret_number
    if user_guess == secret_number:
        secret_number = random.randint(0, 9) # Reset for new game
        return "Correct! You win! Guess again!"
    return "Enter a higher number!" if user_guess < secret_number else "Enter a lower number!"

if __name__ == "__main__":
    print("Guess a number between 0 and 9!")
    while True:
        try:
            feedback = make_guess(int(input("Your guess: ")))
            print(feedback)
            if "Correct!" in feedback: break
        except ValueError: print("Invalid input. Please enter a number.")