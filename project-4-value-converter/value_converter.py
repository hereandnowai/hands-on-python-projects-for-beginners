import requests

def convert_celsius_to_fahrenheit(temp_celsius):
    return (temp_celsius * 9/5) + 32

def convert_fahrenheit_to_celsius(temp_fahrenheit):
    return (temp_fahrenheit - 32) * 5/9

def convert_currency_api(amount, from_currency, to_currency):
    try:
        response = requests.get(f"https://open.er-api.com/v6/latest/{from_currency.upper()}")
        data = response.json()

        if response.status_code == 200 and data["result"] == "success":
            rates = data["rates"]
            if from_currency.upper() not in rates or to_currency.upper() not in rates:
                return "Invalid currency code(s)."

            converted_amount = amount * rates[to_currency.upper()]
            return f"{converted_amount:.2f}"
        else:
            return f"Error fetching rates: {data.get('error-type', 'Unknown error')}"

    except requests.exceptions.ConnectionError:
        return "Network error. Check internet connection."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

def convert_cm_to_feet_inches(value_cm):
    inches = value_cm / 2.54
    feet = int(inches // 12)
    remaining_inches = inches % 12
    return f"{feet} feet and {remaining_inches:.2f} inches"

def convert_feet_inches_to_cm(feet, inches):
    total_inches = (feet * 12) + inches
    length_cm = total_inches * 2.54
    return f"{length_cm:.2f}"

# --- Command-line Interface (for direct execution) ---
if __name__ == "__main__":
    def convert_temperature_cli():
        print("\nWhich conversion do you want to choose:-")
        print("1. Celsius to Faranheit")
        print("2. Faranheit to Celsius")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                temp = float(input("Enter temperature in celsius: "))
                print(f"{temp} degree celsius is equal to {convert_celsius_to_fahrenheit(temp):.2f} degree faranheit.\n")
            elif choice == 2:
                temp = float(input("Enter temperature in faranheit: "))
                print(f"{temp} degree faranheit is equal to {convert_fahrenheit_to_celsius(temp):.2f} degree celsius.\n")
            else:
                print("Invalid input...please try again\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")

    def convert_currency_cli():
        print("\n--- Real-time Currency Converter ---")
        try:
            amount = float(input("Enter amount: "))
            from_currency = input("From currency (e.g., USD, EUR, GBP): ").upper()
            to_currency = input("To currency (e.g., USD, EUR, GBP): ").upper()
            result = convert_currency_api(amount, from_currency, to_currency)
            print(f"{amount} {from_currency} is equal to {result} {to_currency}\n")
        except ValueError:
            print("Invalid amount. Please enter a number.\n")

    def convert_lengths_cli():
        print("\nWhich conversion do you want to choose:-")
        print("1. Centimeters to foot and inches")
        print("2. Foot and inches to centimeter")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                value = float(input("Enter length in cm: "))
                print(f"{value} centimeters is equal to {convert_cm_to_feet_inches(value)}\n")
            elif choice == 2:
                feet = float(input("Enter length in feet: "))
                inches = float(input("Enter length in inches: "))
                print(f"{feet} feet and {inches} inches in centimeters will be {convert_feet_inches_to_cm(feet, inches)}\n")
            else:
                print("Invalid input...please try again\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")

    print("===== Welcome to Value Converter =====")
    while True:
        print("Which option would you like to choose:-")
        print("1. Convert temperature")
        print("2. Convert currency")
        print("3. Convert lengths")
        print("4. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                convert_temperature_cli()
            elif choice == 2:
                convert_currency_cli()
            elif choice == 3:
                convert_lengths_cli()
            elif choice == 4:
                print('Exiting...')
                break
            else:
                print("Invalid choice. Please select a valid option.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")