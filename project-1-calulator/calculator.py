print("===== Welcome to The HERE AND NOW Calculator App =====\n")
while True:
    print("Operations: +, -, *, / or '0' to exit")
    choice = input("Enter your choice: ")

    if choice == '0':
        break

    if choice not in "+-*/":
        print("Invalid choice.")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '+':
        print(f"Output: {num1 + num2}")
    elif choice == '-':
        print(f"Output: {num1 - num2}")
    elif choice == '*':
        print(f"Output: {num1 * num2}")
    elif choice == '/':
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            print(f"Output: {num1 / num2}")
