# Note: This project might require installing the 'requests' library.
# You can do this by running: pip install requests

import requests

# --- Temperature Conversion ---
def convert_celsius_to_fahrenheit(temp_celsius):
    # 1. Implement the formula to convert Celsius to Fahrenheit.
    #    Formula: (Celsius * 9/5) + 32
    pass # Remove this line and add your code here

def convert_fahrenheit_to_celsius(temp_fahrenheit):
    # 2. Implement the formula to convert Fahrenheit to Celsius.
    #    Formula: (Fahrenheit - 32) * 5/9
    pass # Remove this line and add your code here

# --- Currency Conversion ---
def convert_currency_api(amount, from_currency, to_currency):
    # 3. Use the `requests` library to get real-time exchange rates.
    #    a. Construct the API URL: f"https://open.er-api.com/v6/latest/{from_currency.upper()}"
    #    b. Make a GET request to the URL.
    #    c. Parse the JSON response to get the rates dictionary.
    #    d. Calculate the converted amount: amount * rates[to_currency.upper()]
    #    e. Return the result, formatted to 2 decimal places.
    #    f. Include error handling for network issues or invalid currency codes.
    pass # Remove this line and add your code here

# --- Length Conversion ---
def convert_cm_to_feet_inches(value_cm):
    # 4. Implement the logic to convert centimeters to feet and inches.
    #    a. 1 inch = 2.54 cm. First, convert cm to total inches.
    #    b. 1 foot = 12 inches. Calculate the number of feet.
    #    c. Calculate the remaining inches.
    #    d. Return a formatted string, e.g., "X feet and Y.YY inches".
    pass # Remove this line and add your code here

def convert_feet_inches_to_cm(feet, inches):
    # 5. Implement the logic to convert feet and inches to centimeters.
    #    a. Calculate the total number of inches from feet and inches.
    #    b. Convert the total inches to centimeters.
    #    c. Return the result, formatted to 2 decimal places.
    pass # Remove this line and add your code here

# --- Command-line Interface (for direct execution) ---
if __name__ == "__main__":
    # 6. Create a main menu using a `while True` loop.
    #    Display options for Temperature, Currency, Length conversion, and Exit.

    # 7. Based on user's choice, call a corresponding function to handle the sub-menu.
    #    For example, if user chooses '1', call `convert_temperature_cli()`.

    # 8. Implement the `_cli` functions (e.g., `convert_temperature_cli`).
    #    a. These functions will ask the user for specific inputs (e.g., temperature value).
    #    b. They will call the appropriate conversion function.
    #    c. They will print the final result to the user.
    #    d. Use try-except blocks to handle invalid numeric inputs.
    pass # Remove this line and implement the CLI structure.
