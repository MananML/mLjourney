from tabulate import tabulate
import csv
import sys

def check_user_input():
    if len(sys.argv) == 2:
        if sys.argv[1].endswith(".csv"):
            return sys.argv[1]
        else:
            sys.exit("Not a CSV file.")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments.")

    else:
        sys.exit("Too many command-line arguments.")

def table():
    filename = check_user_input()
    data = []
    try:
        with open(filename) as file:
            reader = csv.DictReader(file)

            for row in reader:
                data.append(row)
            return data
        
    except FileNotFoundError:
        sys.exit("File not found.")

def main():
    data = table()
    
    print(tabulate(data, headers="keys", tablefmt="grid"))


main()