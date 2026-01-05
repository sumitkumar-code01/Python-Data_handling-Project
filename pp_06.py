'''
        Challenge : JSON Flattener

            {
            "user": {
                "id": 1,
                "name": "Sumit",
                "email": "sumitkumar@gmail.com",
                "address": {
                "city": "Delhi",
                "pincode": 843119
                }
            },
            "roles": ["admin", "editor"],
            "is_active": true
            }

            Flatten this to:

            {
            "user.id": 1,
            "user.name": "Sumit",
            "user.email": "sumitkumar@gmail.com",
            "user.address.city": "Delhi",
            "user.address.pincode": 843119,
            "roles.0": "admin",
            "roles.1": "editor",
            "is_active": true
            }


'''

import json
import os

# Input and output file names
INPUT_FILE = "nested_data.json"
OUTPUT_FILE = "flattened_data.json"

def flatten_json(data, parent_key="", sep="."):
    """
    This function converts nested JSON into a flattened JSON.
    """
    items = {}

    # If the data is a dictionary
    if isinstance(data, dict):
        for key, value in data.items():
            new_key = f"{parent_key}{sep}{key}" if parent_key else key
            items.update(flatten_json(value, new_key, sep))

    # If the data is a list
    elif isinstance(data, list):
        for index, value in enumerate(data):
            new_key = f"{parent_key}{sep}{index}" if parent_key else str(index)
            items.update(flatten_json(value, new_key, sep))

    # If the data is a single value
    else:
        items[parent_key] = data

    return items


def main():
  
    if not os.path.exists(INPUT_FILE):
        print("Input file not found.")
        return

    try:
        # Read JSON data from file
        with open(INPUT_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Take separator input from user
        sep = input("Enter separator like . or -: ").strip() or "."

        flattened_data = flatten_json(data, sep=sep)

        # Write flattened JSON to output file
        with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
            json.dump(flattened_data, file, indent=2)

        print("Flattened JSON saved successfully in", OUTPUT_FILE)

    except Exception as e:
        print("Failed to flatten the JSON data:", e)

if __name__ == "__main__":
    main()
