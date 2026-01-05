'''
        Challenge: Offline Credential Manager

        Create a CLI tool to manage login credentials 
        (website, username, password) in an encoded 
        local file (`vault.txt`).

        program should:
            1. Add new credentials (website, username, password)
            2. Automatically rate password strength (weak/medium/strong)
            3. Encode the saved content using Base64 for simple offline 
            to confuse someone
            4. View all saved credentials (decoding them)
            5. Update password for any existing website entry (assignment)


'''

import base64
import os

VAULT_FILE = "vault.txt"


def encode(text):
    return base64.b64encode(text.encode()).decode()


def decode(text):
    return base64.b64decode(text.encode()).decode()


def password_strength(password):
    length = len(password) >= 8
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()_+-=" for c in password)

    score = sum([length, has_upper, has_digit, has_special])

    if score <= 1:
        return "Weak"
    elif score == 2:
        return "Medium"
    elif score == 3:
        return "Strong"
    else:
        return "Very Strong"


def add_credential():
    website = input("Website: ").strip()
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    strength = password_strength(password)
    print("Password strength:", strength)

    data = f"{website}||{username}||{password}"
    encoded_data = encode(data)

    with open(VAULT_FILE, "a", encoding="utf-8") as file:
        file.write(encoded_data + "\n")

    print("Credential saved successfully.")


def view_credentials():
    if not os.path.exists(VAULT_FILE):
        print("No credentials found.")
        return

    with open(VAULT_FILE, "r", encoding="utf-8") as file:
        print("\nSaved Credentials:")
        for line in file:
            decoded = decode(line.strip())
            website, username, password = decoded.split("||")
            masked_password = "*" * len(password)
            print(f"{website} | {username} | {masked_password}")


def update_password():
    if not os.path.exists(VAULT_FILE):
        print("No credentials found.")
        return

    website_to_update = input("Enter website name: ").strip()
    updated_lines = []
    found = False

    with open(VAULT_FILE, "r", encoding="utf-8") as file:
        for line in file:
            decoded = decode(line.strip())
            website, username, password = decoded.split("||")

            if website == website_to_update:
                new_password = input("Enter new password: ").strip()
                strength = password_strength(new_password)
                print("New password strength:", strength)
                updated_data = f"{website}||{username}||{new_password}"
                updated_lines.append(encode(updated_data))
                found = True
            else:
                updated_lines.append(line.strip())

    if found:
        with open(VAULT_FILE, "w", encoding="utf-8") as file:
            for line in updated_lines:
                file.write(line + "\n")
        print("Password updated successfully.")
    else:
        print("Website not found.")


def main():
    while True:
        print("\n Offline Credential Manager")
        print("1. Add credential")
        print("2. View credentials")
        print("3. Update password")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        match choice:
            case "1":
                add_credential()
            case "2":
                view_credentials()
            case "3":
                update_password()
            case "4":
                print("Exiting program.")
                break
            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
