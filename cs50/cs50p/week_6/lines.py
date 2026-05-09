import sys

FILE_CONTENT = []

VALID_ROWS = 0
INVALID_ROWS = 0

def check_user_input():
    if len(sys.argv) == 2:
        if sys.argv[1].endswith(".py"):
            return sys.argv[1]
        else:
            sys.exit("Not a python file.")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments.")

    else:
        sys.exit("Too many command-line arguments.")

def check_file():
    file_name = check_user_input()
    try:
        with open(file_name) as file:
            global VALID_ROWS, INVALID_ROWS
            for row in file:
                if row.strip().startswith("#") or row.strip() == "":
                    INVALID_ROWS += 1
                else:
                    VALID_ROWS += 1

            return VALID_ROWS, INVALID_ROWS
    except FileNotFoundError:
        sys.exit("File not found.")

def main():
    valid, invalid = check_file()

    print(valid)


if __name__ == "__main__":
    main() 