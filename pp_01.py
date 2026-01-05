'''
      Challenge: CLI Contact Book (CSV -Powered)
     
      Create a teminal-based contract book tool that storers and 
      manage contacts using a CSV file.

      Program should:
        1. Ask the user to choose one of the following option:
            - Add a new contact
            - View all contacts
            - Search for a contact by name
            - Delete a contact by name
            - Exit the program   
        2. Store conntacts in a file called 'contact.csv' with
        column:
            - Name
            - Phone Number
            - Email Address 
        3. If the file doesnot exit, create it automativcally.
        4. keep the interface clean and clear.
    

'''

import csv
import os

FILE_NAME = "contact.csv"

# Check the file and make header
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Phone", "Email"])

# Add for new contact (Option 1)
def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, email])
    print("Contact added")

# Show total contacts (Option 2)
def view_contacts():
    print("\n--- Contact List ---")
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(f"Name: {row['Name']}, Phone: {row['Phone']}, Email: {row['Email']}")
    else:
        print("No contacts found.")

# For Contact search (Option 3)
def search_contact():
    search_name = input("Enter name to search: ")
    found = False
    with open(FILE_NAME, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Name'].lower() == search_name.lower():
                print(f"Found: {row['Name']} | {row['Phone']} | {row['Email']}")
                found = True
                break
    if not found:
        print("Contact not found.")

# The main function that displays the menu
def main():
    initialize_file()
    
    while True:
        # Bilkul aapki image jaisa menu structure
        print("\n  Contact Book")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid Option!")

if __name__ == "__main__":
    main()