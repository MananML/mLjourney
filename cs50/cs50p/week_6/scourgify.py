import csv 
import sys

def check_user_input():
    if len(sys.argv) == 3:
        for file in sys.argv[1:3]:
            if not file.endswith(".csv"):
                sys.exit(f"{file} is not a CSV file.")
        else:
            return sys.argv[1], sys.argv[2]
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments.")

    else:
        sys.exit("Too many command-line arguments.")

def read():
    first_file, second_file = check_user_input()
    try:
        with open(first_file) as f_file, open(second_file, "w", newline="") as sec_file:
            reader = csv.DictReader(f_file)
            writer = csv.DictWriter(sec_file, fieldnames=["first", "last", "house"])

            writer.writeheader()

            for row in reader:
                last, first = row["name"].split(",")

                writer.writerow({
                    "first": first.strip(), "last": last, "house": row["house"]
                })
    except FileNotFoundError:
        sys.exit(f"Cannot read {first_file}.")

def main():
    read()


main()
