# Thiss script was generated using ChatGPT.

import csv
import argparse
from datetime import datetime

def sort_csv_by_datetime(input_file, output_file):
    # Read the CSV data
    with open(input_file, mode='r', newline='') as infile:
        reader = csv.reader(infile)
        header = next(reader)  # Skip the header row
        rows = list(reader)

    # Sort the rows by the Date/Time column (index 9)
    rows.sort(key=lambda row: datetime.strptime(row[9], "%Y%m%d;%H%M%S"))

    # Write the sorted data to the output file
    with open(output_file, mode='w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)  # Write the header row
        writer.writerows(rows)   # Write the sorted rows

    print(f"Data has been sorted and saved to {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Sort a CSV file by Date/Time column.")
    parser.add_argument("input_file", help="Path to the input CSV file")
    parser.add_argument("output_file", help="Path to the output CSV file")

    args = parser.parse_args()
    sort_csv_by_datetime(args.input_file, args.output_file)

if __name__ == "__main__":
    main()
