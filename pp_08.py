"""
        Challenge: Offline Notes Locker

        Create a terminal-based app that allows users to save, view, and search 
        personal notes securely in an encrypted file.

        program should:
            1. Let users add notes with title and content.
            2. Automatically encrypt each note using Fernet (AES under the hood).
            3. Store all encrypted notes in a single `.vault` file (JSON format).
            4. Allow listing of titles and viewing/decrypting selected notes.
            5. Support searching by title or keyword.

        
"""

import json
import os
from cryptography.fernet import Fernet
from datetime import datetime

# Constants for file paths
VAULT_FILE = "notes_vault.json"
KEY_FILE = "vault.key"

def load_or_create_key():
    """
    Load the encryption key from a file, or create a new one if it doesn't exist.
    """
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
        print("[System] New encryption key generated and saved.")
    else:
        with open(KEY_FILE, "rb") as f:
            key = f.read()
    
    return Fernet(key)

# Initialize Fernet object globally
try:
    fernet = load_or_create_key()
except Exception as e:
    print(f"Error initializing encryption: {e}")
    exit()

def load_vault():
    """
    Load all notes from the vault file. Returns a list of notes.
    """
    if not os.path.exists(VAULT_FILE):
        return []  
    try:
        with open(VAULT_FILE, "r", encoding="utf-8") as f:
            content = f.read()
            if not content:
                return []
            return json.loads(content)
    except (json.JSONDecodeError, IOError):
        return []

def save_vault(data):
    """
    Save all notes to the vault file in JSON format.
    """
    with open(VAULT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def add_note():
    """
    Encrypts and adds a new note.
    """
    print("\n--- Create a New Note ---")
    title = input("Enter note title: ").strip()
    content = input("Enter note content: ").strip()

    if not title or not content:
        print("Error: Title and content cannot be empty.")
        return

    # Encrypt the content
    encrypted_content = fernet.encrypt(content.encode()).decode()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data = load_vault()
    data.append({
        "title": title,
        "content": encrypted_content,
        "timestamp": timestamp
    })

    save_vault(data)
    print("Success: Note encrypted and saved!")

def list_notes():
    """
    Displays all available titles.
    """
    data = load_vault()
    if not data:
        print("\n[Vault is empty]")
        return False
    
    print("\n--- Your Encrypted Notes ---")
    for i, note in enumerate(data, 1):
        print(f"{i}. {note['title']} (Added: {note['timestamp']})")
    return True

def view_note():
    """
    Decrypts and displays a specific note.
    """
    data = load_vault()
    if not list_notes():
        return

    try:
        choice = int(input("\nEnter the note number to decrypt and view: ")) - 1
        if 0 <= choice < len(data):
            encrypted_content = data[choice]["content"]
            # Decrypting the content back to readable text
            decrypted_content = fernet.decrypt(encrypted_content.encode()).decode()
            
            print("-" * 40)
            print(f"TITLE: {data[choice]['title']}")
            print(f"DATE:  {data[choice]['timestamp']}")
            print("-" * 40)
            print(decrypted_content)
            print("-" * 40)
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")
    except Exception as e:
        print(f"Decryption failed: {e}")

def search_notes():
    """
    Search for notes by title.
    """
    keyword = input("Search keyword: ").strip().lower()
    if not keyword:
        return

    data = load_vault()
    results = [n for n in data if keyword in n["title"].lower()]

    if not results:
        print("No matching notes found.")
    else:
        print(f"\n Search Results ({len(results)}) ")
        for note in results:
            print(f"- {note['title']} ({note['timestamp']})")

def main():
    while True:
        print("=== OFFLINE NOTES LOCKER ===")
        print("1. Add Note")
        print("2. List Notes")
        print("3. View Note")
        print("4. Search Titles")
        print("5. Exit")
        
        choice = input("\nSelect an option (1-5): ").strip()

        if choice == "1":
            add_note()
        elif choice == "2":
            list_notes()
        elif choice == "3":
            view_note()
        elif choice == "4":
            search_notes()
        elif choice == "5":
            print("Vault locked. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()