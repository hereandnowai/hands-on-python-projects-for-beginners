import string
import getpass

def check_password_strength(password):
    lower_alpha_count = upper_alpha_count = number_count = whitespace_count = special_char_count = 0
    for char in list(password):
        if char in string.ascii_lowercase:
            lower_alpha_count += 1
        elif char in string.ascii_uppercase:
            upper_alpha_count += 1
        elif char in string.digits:
            number_count += 1
        elif char == ' ':
            whitespace_count += 1
        else:
            special_char_count += 1
    strength = 0
    remarks = ''

    if lower_alpha_count >= 1:
        strength += 1
    if upper_alpha_count >= 1:
        strength += 1
    if number_count >= 1:
        strength += 1
    if whitespace_count >= 1:
        strength += 1
    if special_char_count >= 1:
        strength += 1

    if strength == 1:
        remarks = "That's a very bad password. Change it as soon as possible."
    elif strength == 2:
        remarks = "That's not a good password. You should consider making a tougher password."
    elif strength == 3:
        remarks = "Your password is okay, but it can be improved a lot"
    elif strength == 4:
        remarks = "Your password is hard to guess. But you can make it even more secure"
    elif strength == 5:
        remarks = "Now that's one hell of a strong password !!! Hackers don't have a chance guessing that password."

    result = "Your password has:-\n"
    result += f"{lower_alpha_count} lowercase letters\n"
    result += f"{upper_alpha_count} uppercase letters\n"
    result += f"{number_count} digits\n"
    result += f'{whitespace_count} whitespaces\n'
    result += f"{special_char_count} special characters\n"
    result += f"Password score: {strength}/5\n"
    result += f"Remarks: {remarks}"
    return result

if __name__ == "__main__":
    print("===== Welcome to Password Strength Checker =====")
    while True:
        choice = input("Do you want to check a password's strength (y/n) : ")
        if 'y' in choice.lower():
            password = getpass.getpass("Enter the password: ")
            print(check_password_strength(password))
        elif 'n' in choice.lower():
            print('Exiting...')
            break
        else:
            print('Invalid input...please try again.')
        print()
