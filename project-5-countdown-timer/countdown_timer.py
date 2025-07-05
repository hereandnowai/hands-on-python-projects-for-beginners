import time

def set_countdown(seconds):
    yield "Countdown starts now..."
    for i in range(seconds, 0, -1):
        yield f'{i:02d}'
        time.sleep(1)
    yield "Countdown ended!"

if __name__ == "__main__":
    print("===== Welcome to HERE AND NOW AI's Countdown Timer =====")
    while True:
        try:
            choice = input("Do you want to set a countdown (y/n): ")
            if 'y' in choice.lower():
                seconds = int(input("Enter number of seconds: "))
                # For CLI, we need to consume the generator
                for msg in set_countdown(seconds):
                    # This part is a bit tricky for CLI to show real-time updates on one line
                    # For simplicity in CLI, we'll just print each step on a new line
                    # The UI will handle the single-line update better
                    print(msg)
            elif 'n' in choice.lower():
                print('Exiting...')
                break
            else:
                print('Invalid input...please try again')
        except ValueError:
            print("Invalid input. Please enter a number for seconds.")