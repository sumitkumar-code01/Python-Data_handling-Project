"""
        Challenge: CSV-TO-JSON Converter Tool

"""



import os
import csv
import json

input_file = "raw_data.csv"
output_file = "converted_data.json"


def load_csv(file_name):
    # check if file exists or not
    if not os.path.exists(file_name):
        print("CSV file not found")
        return []

    data = []

    # open csv file and read data
    with open(file_name, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    return data


def save_json(data, file_name):
    # save data into json file
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)

    print("Converted", len(data), "records to JSON file")


def preview(data):
    # show first 3 records
    print("\nPreview of data:")
    for i in range(min(3, len(data))):
        print(json.dumps(data[i], indent=2))
    print("........")


def main():
    csv_data = load_csv(input_file)

    if len(csv_data) == 0:
        print("No data found")
        return

    save_json(csv_data, output_file)
    preview(csv_data)


if __name__ == "__main__":
    main()
