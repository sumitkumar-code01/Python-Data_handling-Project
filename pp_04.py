"""
        Challenge: JSON-to-Excel Converter Tool

        Create a Python utility that reads structured data (like you'd get from an API) from a `.json` file and converts it to a CSV file that can be opened in Excel.

        program should:

            1. Read from a file named `api_data.json` in the same folder.
            2. Convert the JSON content (a list of dictionaries) into `converted_data.csv`.
            3. Automatically extract field names as CSV headers.
            4. Handle nested structures by flattening or skipping them.

"""


import json
import csv
import os

# Input and     output file names
INPUT_FILE = "api_data.json"
OUTPUT_FILE = "converted_data.csv"


def load_json_data(filename):
    # Check if the JSON file exists or not
    if not os.path.exists(filename):
        print("JSON file not found")
        return []

    try:
        # Open the JSON file and read data
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except json.JSONDecodeError:
        # If JSON format is wrong
        print("Invalid JSON format")
        return []


def flatten_record(record):
    """
    This function removes nested data.
    It keeps only simple key and value pairs.
    """
    simple_record = {}

    for key, value in record.items():
        # If value is dictionary or list, skip it
        if isinstance(value, dict) or isinstance(value, list):
            continue
        else:
            simple_record[key] = value

    return simple_record


def convert_to_csv(data, output_file):
    # Check if data is empty
    if not data:
        print("No data to convert")
        return

    # Take keys from first record as CSV headers
    first_record = flatten_record(data[0])
    fieldnames = first_record.keys()

    # Create and write CSV file
    with open(output_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        # Write each record in CSV
        for record in data:
            simple_record = flatten_record(record)
            writer.writerow(simple_record)

    print(f"Converted {len(data)} records to {output_file}")


def main():
    print("Converting JSON to CSV...")
    data = load_json_data(INPUT_FILE)
    convert_to_csv(data, OUTPUT_FILE)


# Program starts from here
if __name__ == "__main__":
    main()
