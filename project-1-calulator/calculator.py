def calculate(num1, op, num2):
    if op == "+": return num1 + num2
    elif op == "-": return num1 - num2
    elif op == "*": return num1 * num2
    elif op == "/":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2

if __name__ == "__main__":
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

        result = calculate(num1, choice, num2)
        print(f"Output: {result}")

