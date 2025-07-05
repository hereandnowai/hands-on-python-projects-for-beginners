import random

def roll_die():
    die_number = random.randint(1, 6)
    return die_number

if __name__ == "__main__":
    print("\n===== Welcome to HERE AND NOW AI's Die Rolling Simulator =====")
    while True:
        choice = input("Do you want to roll a die? (y/n): ")
        if 'y' in choice.lower():
            print("Rolling the die...")
            number = roll_die()
            print("The die shows:", number, "\n")
        elif 'n' in choice.lower():
            print("Exiting...")
            break
        else:
            print("Invalid input. Please try again.")