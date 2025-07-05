def calculate(num1, op, num2):
    if op == "+": return num1 + num2
    elif op == "-": return num1 - num2
    elif op == "*": return num1 * num2
    elif op == "/":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2

if __name__ == "__main__":
    print("===== Welcome to HERE AND NOW AI's Calculator App =====\n")
    while True:
        print("Operators: +, -, *, / or exit")
        op = input("Enter an operator: ")

        if op == 'exit':
            break

        if op not in "+-*/":
            print("Invalid operator.")
            continue

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = calculate(num1, op, num2)
        print(f"Output: {result}")