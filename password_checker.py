while True:

    password = input("\nEnter your password: ")

    # Check password length
    if len(password) >= 8:
        print("Password is at least 8 characters long.")
    else:
        print("Password is too short.")

    # Check for uppercase letters
    if any(char.isupper() for char in password):
        print("Password contains an uppercase letter.")
    else:
        print("Password needs an uppercase letter.")

    # Check for lowercase letters
    if any(char.islower() for char in password):
        print("Password contains a lowercase letter.")
    else:
        print("Password needs a lowercase letter.")

    # Check for numbers
    if any(char.isdigit() for char in password):
        print("Password contains a number.")
    else:
        print("Password needs a number.")

    # List of special characters
    special_characters = "!@#$%^&*()-_=+[]{};:,.<>?/"

    # Check for special characters
    if any(char in special_characters for char in password):
        print("Password contains a special character.")
    else:
        print("Password needs a special character.")

    # Start the score at 0
    score = 0

    # Add points for each requirement
    if len(password) >= 8:
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(char in special_characters for char in password):
        score += 1

    # List of common passwords
    common_passwords = ["password", "123456", "qwerty", "admin", "letmein"]

    # Check if password is common
    if password.lower() in common_passwords:
        print("Warning: This is a common password.")

    # Display score
    print("Password score:", score, "/ 5")

    # Calculate percentage
    strength_percentage = (score / 5) * 100
    print("Strength percentage:", strength_percentage, "%")

    # Determine password strength
    if password.lower() in common_passwords:
        print("Password strength: Weak")
    elif score <= 2:
        print("Password strength: Weak")
    elif score <= 4:
        print("Password strength: Medium")
    else:
        print("Password strength: Strong")

    # Give suggestions
    print("\nSuggestions:")

    if len(password) < 8:
        print("- Use at least 8 characters.")

    if not any(char.isupper() for char in password):
        print("- Add an uppercase letter.")

    if not any(char.islower() for char in password):
        print("- Add a lowercase letter.")

    if not any(char.isdigit() for char in password):
        print("- Add a number.")

    if not any(char in special_characters for char in password):
        print("- Add a special character.")

    if score == 5 and password.lower() not in common_passwords:
        print("No suggestions, Password is strong!")

    # Ask if the user wants to check another password
    again = input("\nWould you like to check another password? (yes/no): ")

    if again.lower() != "yes":
        print("Password checker closed.")
        break